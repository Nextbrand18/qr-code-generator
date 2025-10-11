# Usage Guide

## Basic Usage
```bash
python qrGenerator.py

python qrGenerator.py \
  --data "YOUR_DATA" \
  --owner "OWNER_NAME" \
  --title "QR_TITLE" \
  --logo path/to/logo.png \
  --output custom_name.png


  Arguments
Flag	Description
--data	Data to encode in QR code (required)
--owner	Owner name text (optional)
--title	Title text (optional)
--logo	Path to logo image (optional)
--output	Output filename (optional)



# Basic QR example
python qrGenerator.py \
  --data "https://github.com/Nextbrand18/qr-code-generator" \
  --output examples/qrcode_example.png

# QR with text
python qrGenerator.py \
  --data "https://github.com" \
  --owner "Nextbrand" \
  --title "GitHub Access" \
  --output examples/qrcode_with_text.png

# QR with logo (only if you have a logo.jpg file)
python qrGenerator.py \
  --data "https://oriflame.com" \
  --logo assets/logo.jpg \
  --output examples/qrcode_with_logo.png

# QR with all entires
python qrGenerator.py \
  --data "https://github.com/Nextbrand18/qr-code-generator" \
  --owner "YourName" \
  --title "Project QR" \
  --logo "assets/logo.jpg" \
  --output "examples/qrcode_allentries.png"

  ## More about Usage ---------------------------------------------

  # QR Code Generator - Complete Usage Guide

A production-ready QR code generator with custom branding, logos, and an intuitive web interface.

![QR Code Generator](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

---

## 📋 Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Detailed Usage](#detailed-usage)
- [Configuration](#configuration)
- [Deployment](#deployment)
- [Troubleshooting](#troubleshooting)
- [FAQ](#faq)

---

## ✨ Features

- 🎨 **Modern Web Interface** - Beautiful, responsive design with animations
- 🔒 **Production Ready** - Input validation, error handling, security features
- 🖼️ **Logo Embedding** - Add your brand logo to QR codes
- 📝 **Custom Text** - Include owner name and title
- ♿ **Accessible** - WCAG 2.1 AA compliant, keyboard navigation, screen reader support
- 📱 **Responsive** - Works on desktop, tablet, and mobile
- 🚀 **Fast** - Generates QR codes in milliseconds
- 💾 **Download Ready** - One-click download of generated QR codes

---

## 📦 Prerequisites

Before you begin, ensure you have the following installed:

### Required Software

- **Python 3.8 or higher**
  - Check version: `python --version` or `python3 --version`
  - Download: [python.org](https://www.python.org/downloads/)

- **pip** (Python package manager)
  - Usually comes with Python
  - Check version: `pip --version` or `pip3 --version`

- **Git** (for cloning the repository)
  - Check version: `git --version`
  - Download: [git-scm.com](https://git-scm.com/downloads)

### Optional (Recommended)

- **Virtual Environment** (venv or virtualenv)
  - Keeps dependencies isolated
  - Comes with Python 3.3+

---

## 🚀 Installation

### Step 1: Clone the Repository

Open your terminal/command prompt and run:

```bash
# Clone the repository
git clone https://github.com/YOUR-USERNAME/qr-code-generator.git

# Navigate into the project directory
cd qr-code-generator
```

**Alternative:** Download the ZIP file from GitHub and extract it.

---

### Step 2: Create a Virtual Environment (Recommended)

This keeps your project dependencies separate from other Python projects.

**On Windows:**
```bash
# Create virtual environment
python -m venv venv

# Activate it
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate
```

**You'll know it's activated when you see `(venv)` in your terminal prompt.**

---

### Step 3: Install Dependencies

With your virtual environment activated:

```bash
# Install all required packages
pip install -r requirements.txt
```

**What gets installed:**
- Flask (web framework)
- Flask-CORS (cross-origin support)
- qrcode (QR code generation)
- Pillow (image processing)

**Verify installation:**
```bash
pip list
```

You should see Flask, Flask-CORS, qrcode, and Pillow in the list.

---

### Step 4: Verify Project Structure

Make sure your project directory looks like this:

```
qr-code-generator/
├── doc/                    # Documentation
│   ├── README.md
│   ├── API.md
│   └── USAGE.md           # This file
├── static/
│   └── qrcodes/           # Generated QR codes (auto-created)
├── uploads/               # Temp logo storage (auto-created)
├── index.html             # Frontend application
├── app.py                 # Backend server
├── qrGenerator.py         # QR generation logic
├── requirements.txt       # Python dependencies
└── .gitignore            # Git ignore rules
```

**Note:** `static/qrcodes/` and `uploads/` will be created automatically when you run the app.

---

## 🎯 Quick Start

### 1. Start the Server

```bash
# Make sure your virtual environment is activated
# You should see (venv) in your terminal

# Start the Flask server
python app.py
```

**Expected output:**
```
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.x.x:5000
Press CTRL+C to quit
```

---

### 2. Open the Application

Open your web browser and go to:
```
http://localhost:5000
```

**Or:**
```
http://127.0.0.1:5000
```

You should see the QR Code Generator interface! 🎉

---

### 3. Generate Your First QR Code

1. **Enter Content** (required)
   - Type a URL: `https://github.com/yourusername`
   - Or any text: `Hello World!`

2. **Add Custom Details** (optional)
   - Owner Name: `Your Name`
   - Title: `My GitHub Profile`

3. **Upload Logo** (optional)
   - Click "Choose File"
   - Select a PNG, JPG, or WebP image (max 5MB)

4. **Click "Generate QR Code"**
   - Wait a moment while it processes
   - Your QR code appears on the right!

5. **Download**
   - Click "Download QR Code"
   - Save the PNG file to your computer

---

## 📖 Detailed Usage

### Understanding the Interface

The application has two main sections:

#### Left Panel: QR Code Settings ⚙️

1. **Content Field** (Required)
   - What the QR code will contain
   - Can be a URL, text, phone number, etc.
   - Maximum 2000 characters
   - Examples:
     ```
     https://mywebsite.com
     mailto:hello@example.com
     tel:+1234567890
     This is plain text
     ```

2. **Owner Name** (Optional)
   - Displayed above the QR code
   - Maximum 100 characters
   - Use for branding or attribution
   - Example: `Acme Corporation`

3. **Title** (Optional)
   - Displayed below owner name
   - Maximum 100 characters
   - Describe what the QR code is for
   - Example: `Product Manual`

4. **Logo Image** (Optional)
   - Upload your company logo or icon
   - Accepted formats: PNG, JPG, WebP
   - Maximum size: 5MB
   - Will be centered on the QR code
   - Automatically resized to 20% of QR code size
   - **Tip:** Use PNG with transparency for best results

#### Right Panel: Your QR Code 🎨

- **QR Code Preview**
  - Shows generated QR code
  - Hover to see border animation
  - Click "Download" to save

- **Console Log**
  - Shows real-time status updates
  - Timestamps for each action
  - Color-coded messages:
    - 🔵 Blue (Info): Normal operations
    - 🟢 Green (Success): Completed actions
    - 🔴 Red (Error): Problems or failures

---

### Advanced Features

#### Keyboard Shortcuts

- **Ctrl/Cmd + Enter** - Generate QR code (when form is focused)
- **Tab** - Navigate between fields
- **Space/Enter** - Activate buttons

#### Validation & Error Messages

The app validates your input in real-time:

- ✅ **Content is required** - You'll see an error if it's empty
- ✅ **File size check** - Logo must be under 5MB
- ✅ **File type check** - Only PNG, JPG, WebP accepted
- ✅ **Character limits** - Enforced on all text fields

#### Network Reliability

- **Automatic Retry** - If generation fails, it retries 3 times
- **Timeout Handling** - Requests timeout after 30 seconds
- **Connection Status** - Shows if backend is reachable

---

## ⚙️ Configuration

### Changing the Server Port

Edit `app.py` (bottom of file):

```python
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # Change 5000 to your port
```

### Adjusting File Limits

Edit `index.html` (in the `<script>` section):

```javascript
const CONFIG = {
    API_URL: ...,
    MAX_FILE_SIZE: 5 * 1024 * 1024, // Change this (in bytes)
    REQUEST_TIMEOUT: 30000,          // Change this (in milliseconds)
    MAX_RETRIES: 3,                  // Number of retry attempts
    ...
};
```

### Customizing QR Code Quality

Edit `qrGenerator.py`:

```python
qr = qrcode.QRCode(
    version=None,                                    # Auto-size
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Highest (for logos)
    box_size=10,                                     # Size of each box (increase for larger QR)
    border=4,                                        # White border size
)
```

**Error Correction Levels:**
- `ERROR_CORRECT_L` - Low (7% recovery)
- `ERROR_CORRECT_M` - Medium (15% recovery)
- `ERROR_CORRECT_Q` - Quartile (25% recovery)
- `ERROR_CORRECT_H` - High (30% recovery) - **Recommended for logos**

---

## 🌐 Deployment

### Local Network Access

To access from other devices on your network:

1. **Find your IP address:**

   **Windows:**
   ```bash
   ipconfig
   ```
   Look for "IPv4 Address"

   **macOS/Linux:**
   ```bash
   ifconfig
   # or
   ip addr show
   ```
   Look for your local IP (usually 192.168.x.x)

2. **Access from another device:**
   ```
   http://YOUR-IP-ADDRESS:5000
   ```
   Example: `http://192.168.1.100:5000`

---

### Production Deployment

⚠️ **Warning:** The built-in Flask server is NOT suitable for production!

#### Option 1: Using Gunicorn (Recommended)

```bash
# Install Gunicorn
pip install gunicorn

# Run with Gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

#### Option 2: Using uWSGI

```bash
# Install uWSGI
pip install uwsgi

# Run with uWSGI
uwsgi --http 0.0.0.0:5000 --wsgi-file app.py --callable app --processes 4
```

#### Option 3: Using Docker

Create `Dockerfile`:
```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt gunicorn

COPY . .
RUN mkdir -p static/qrcodes uploads

EXPOSE 5000
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
```

Build and run:
```bash
docker build -t qr-generator .
docker run -p 5000:5000 qr-generator
```

#### Production Checklist

Before deploying:
- [ ] Set `debug=False` in `app.py`
- [ ] Use a production WSGI server (Gunicorn/uWSGI)
- [ ] Enable HTTPS with SSL certificate
- [ ] Implement rate limiting
- [ ] Set up proper CORS origins
- [ ] Configure firewall rules
- [ ] Set up automated backups
- [ ] Implement monitoring/logging
- [ ] Add authentication if needed

---

## 🐛 Troubleshooting

### Problem: "Port 5000 is already in use"

**Solution 1:** Stop the process using port 5000
```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# macOS/Linux
lsof -ti:5000 | xargs kill -9
```

**Solution 2:** Use a different port
```bash
# Edit app.py and change port to 5001 (or any available port)
python app.py
```

---

### Problem: "ModuleNotFoundError: No module named 'flask'"

**Cause:** Dependencies not installed or virtual environment not activated

**Solution:**
```bash
# Make sure virtual environment is activated
# You should see (venv) in your prompt

# Install dependencies
pip install -r requirements.txt
```

---

### Problem: "Connection refused" or "Cannot connect to backend"

**Cause:** Backend server is not running

**Solution:**
1. Check if `app.py` is running
2. Look for error messages in the terminal
3. Restart the server: `python app.py`
4. Check the console in your browser (F12) for error details

---

### Problem: "Failed to add logo" or logo not appearing

**Possible Causes:**
1. **File too large** - Must be under 5MB
2. **Wrong format** - Only PNG, JPG, WebP supported
3. **Corrupted file** - Try a different image
4. **No transparency** - Use PNG with transparency for best results

**Solution:**
- Resize your logo to under 5MB
- Convert to PNG format
- Try a simpler logo design

---

### Problem: QR code won't scan

**Possible Causes:**
1. **Too much content** - QR codes have size limits
2. **Logo too large** - Covering too much of the QR code
3. **Low quality print** - Printed too small or blurry

**Solutions:**
- Shorten the URL (use a URL shortener)
- Use a smaller logo
- Print larger (at least 2cm x 2cm)
- Increase error correction in `qrGenerator.py`

---

### Problem: "Permission denied" errors

**Cause:** No write permissions for directories

**Solution:**
```bash
# Linux/macOS
chmod 755 static/qrcodes
chmod 755 uploads

# Windows - Run as Administrator or check folder permissions
```

---

## ❓ FAQ

### Q: Can I generate multiple QR codes at once?

**A:** The current version generates one QR code at a time. For batch generation, you can:
1. Use the API endpoint programmatically (see `doc/API.md`)
2. Write a script to call the API multiple times
3. Implement a batch feature (future enhancement)

---

### Q: What's the maximum size for QR codes?

**A:** QR codes can encode up to ~2000 characters, but scanning reliability decreases with more data. For best results:
- URLs: Keep under 100 characters (use URL shorteners)
- Text: Keep under 500 characters
- Use high error correction for logos

---

### Q: Can I customize the QR code colors?

**A:** Currently, QR codes are black and white. To add colors:
1. Edit `qrGenerator.py`
2. Change `fill_color` and `back_color` in the QR generation:
   ```python
   qr_img = qr.make_image(fill_color="blue", back_color="white")
   ```

---

### Q: How do I stop the server?

**A:** Press `Ctrl + C` in the terminal where `app.py` is running.

---

### Q: Are the generated QR codes saved permanently?

**A:** Yes, they're saved in `static/qrcodes/` until you delete them. Consider:
- Implementing automatic cleanup for old files
- Backing up important QR codes
- Adding a delete feature

---

### Q: Can I use this commercially?

**A:** Check the LICENSE file in the repository. Most open-source licenses allow commercial use with attribution.

---

### Q: How secure is this application?

**A:** The current version has basic security:
- ✅ Input validation
- ✅ File type/size checks
- ✅ XSS prevention
- ❌ No rate limiting
- ❌ No authentication

For production, add:
- Rate limiting
- HTTPS/SSL
- Authentication
- Content Security Policy headers

---

### Q: My logo looks pixelated in the QR code

**A:** Use a higher resolution logo:
- Minimum: 500x500 pixels
- Recommended: 1000x1000 pixels
- Format: PNG with transparency
- Keep it simple (complex logos don't work well)

---

## 📞 Support

### Getting Help

1. **Check the documentation:**
   - `doc/README.md` - Complete overview
   - `doc/API.md` - API reference
   - This file - Usage guide

2. **Enable debug mode:**
   - Check browser console (F12)
   - Check server terminal for errors
   - Look at the console log in the app

3. **Common issues:**
   - Review the Troubleshooting section above
   - Search GitHub issues

4. **Still stuck?**
   - Open an issue on GitHub
   - Include error messages
   - Describe steps to reproduce
   - Share screenshots if relevant

---

## 🎓 Learning Resources

### Understanding QR Codes
- [QR Code Wikipedia](https://en.wikipedia.org/wiki/QR_code)
- [How QR Codes Work](https://www.qrcode.com/en/about/)

### Flask Documentation
- [Flask Official Docs](https://flask.palletsprojects.com/)
- [Flask Tutorial](https://flask.palletsprojects.com/tutorial/)

### Python Resources
- [Python Official Tutorial](https://docs.python.org/3/tutorial/)
- [Real Python](https://realpython.com/)

---

## 🤝 Contributing

Want to improve this project?

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Test thoroughly
5. Commit: `git commit -m "Add feature"`
6. Push: `git push origin feature-name`
7. Open a Pull Request

---

## 📄 License

[Add your license here - e.g., MIT, GPL, etc.]

---

## 🙏 Acknowledgments

- **qrcode library** - For QR code generation
- **Pillow** - For image processing
- **Flask** - For the web framework
- All contributors and users!

---

## 📊 Version History

### v1.0.0 (Current)
- Initial release
- Single QR code generation
- Logo embedding support
- Custom owner/title text
- Production-ready frontend
- Full accessibility support

---

**Made with ❤️ by [Your Name]**

**Last Updated:** October 2025

---

## 🚀 Next Steps

Now that you're set up:

1. ✅ Generate your first QR code
2. ✅ Experiment with logos and text
3. ✅ Test on mobile devices
4. ✅ Share with others on your network
5. ✅ Consider deploying to production
6. ✅ Customize for your needs
7. ✅ Contribute improvements back!

**Happy QR coding! 📱✨**