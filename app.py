from flask import Flask, request, jsonify, send_from_directory, render_template
from flask_cors import CORS
import os
import uuid
from qrGenerator import generate_qr_with_customizations

app = Flask(__name__)
CORS(app)

# Ensure folders exist
os.makedirs('static/qrcodes', exist_ok=True)
os.makedirs('uploads', exist_ok=True)

# Serve the frontend
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')  # Serve index.html from root folder

@app.route('/generate-qr', methods=['POST'])
def generate_qr():
    try:
        content = request.form.get('content', '').strip()
        owner = request.form.get('owner', '').strip()
        title = request.form.get('title', '').strip()
        logo_file = request.files.get('logo')

        if not content:
            return jsonify({'success': False, 'error': 'Content cannot be empty'})

        logo_path = None
        if logo_file:
            logo_ext = os.path.splitext(logo_file.filename)[1]
            logo_path = os.path.join('uploads', f"{uuid.uuid4().hex}{logo_ext}")
            logo_file.save(logo_path)

        filename = f"{uuid.uuid4().hex}.png"
        output_path = os.path.join('static', 'qrcodes', filename)

        result = generate_qr_with_customizations(
            data=content,
            owner_name=owner,
            title=title,
            logo_path=logo_path,
            filename=output_path
        )

        if logo_path and os.path.exists(logo_path):
            os.remove(logo_path)

        if result:
            return jsonify({'success': True, 'image_url': f"/static/qrcodes/{filename}"})
        else:
            return jsonify({'success': False, 'error': 'Failed to generate QR code'})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route("/static/qrcodes/<path:filename>")
def serve_qr(filename):
    return send_from_directory("static/qrcodes", filename)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
