import qrcode
from PIL import Image, ImageDraw, ImageFont
import os
from datetime import datetime

__version__ = "1.0.0"

def generate_qr_with_customizations(data, owner_name="", title="", logo_path=None, filename=None):
    """
    Generate a QR code with optional owner, title, and logo.

    Args:
        data (str): Data to encode (required)
        owner_name (str): Owner text (optional)
        title (str): Title text (optional)
        logo_path (str): Path to logo image (optional)
        filename (str): Output filename (optional)

    Returns:
        tuple: (PIL.Image object, filename) or None on failure
    """
    try:
        if not data or not isinstance(data, str):
            raise ValueError("Data must be a non-empty string")

        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

        # Header height for text
        header_height = 100 if owner_name or title else 0
        final_img = Image.new("RGB", (qr_img.width, qr_img.height + header_height), "white")
        final_img.paste(qr_img, (0, header_height))

        # Draw text
        if owner_name or title:
            draw = ImageDraw.Draw(final_img)
            font = load_font()

            if owner_name:
                add_text(draw, owner_name, font, qr_img.width, 10)
            if title:
                add_text(draw, title, get_smaller_font(font), qr_img.width, 50 if owner_name else 10)

        # Add logo
        if logo_path:
            add_logo(final_img, logo_path, header_height, qr_img.size)

        # Generate filename
        filename = filename or generate_filename()
        final_img.save(filename, quality=95, optimize=True)
        return final_img, filename

    except Exception as e:
        print(f"Error generating QR: {e}")
        return None

# ---------------------- Helper functions ----------------------

def load_font(size=28):
    paths = [
        "arial.ttf",
        "C:/Windows/Fonts/arial.ttf"
    ]
    for path in paths:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except:
                continue
    return ImageFont.load_default()

def get_smaller_font(font, reduction=4):
    try:
        return ImageFont.truetype(font.path, font.size - reduction)
    except:
        return font

def add_text(draw, text, font, canvas_width, y_pos):
    bbox = draw.textbbox((0,0), text, font=font)
    text_width = bbox[2] - bbox[0]
    x_pos = (canvas_width - text_width)//2
    # Shadow
    draw.text((x_pos+1, y_pos+1), text, fill="#444", font=font)
    # Main text
    draw.text((x_pos, y_pos), text, fill="black", font=font)

def add_logo(image, logo_path, header_height, qr_size):
    try:
        logo = Image.open(logo_path).convert("RGBA")
        size = int(qr_size[0]*0.2)
        logo.thumbnail((size, size))
        pos = ((qr_size[0]-logo.width)//2, header_height + (qr_size[1]-logo.height)//2)
        mask = logo.split()[3] if logo.mode=="RGBA" else None
        image.paste(logo, pos, mask)
    except Exception as e:
        print(f"Failed to add logo: {e}")

def generate_filename():
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"qrcode_{now}.png"
