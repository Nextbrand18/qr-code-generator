import qrcode
from PIL import Image, ImageDraw, ImageFont
import os
import re
from datetime import datetime

def generate_qr_with_customizations(data, owner_name="", title="", logo_path=None, filename=None):
    """
    Generate a QR code with:
    - Custom owner name at the top
    - Custom title below owner name
    - Optional logo in the center
    - Automatic filename based on current date/time if not specified
    """
    
    # Create QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction for logo
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    # Generate QR image
    qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
    
    # Calculate header space based on text elements
    header_height = 0
    if owner_name or title:
        header_height = 100 if owner_name and title else 60
    
    # Create canvas with space for header and QR code
    final_img = Image.new('RGB', (qr_img.width, qr_img.height + header_height), "white")
    final_img.paste(qr_img, (0, header_height))
    
    # Add text elements if specified
    if owner_name or title:
        draw = ImageDraw.Draw(final_img)
        font = load_font() or ImageFont.load_default()
        
        # Add owner name
        if owner_name:
            bbox = draw.textbbox((0, 0), owner_name, font=font)
            text_width = bbox[2] - bbox[0]
            text_x = (qr_img.width - text_width) // 2
            draw.text((text_x, 10), owner_name, fill="black", font=font)
        
        # Add title
        if title:
            smaller_font = ImageFont.truetype(font.path, font.size-4) if hasattr(font, 'path') else font
            bbox = draw.textbbox((0, 0), title, font=smaller_font)
            text_width = bbox[2] - bbox[0]
            text_x = (qr_img.width - text_width) // 2
            text_y = 50 if owner_name else 10
            draw.text((text_x, text_y), title, fill="black", font=smaller_font)
    
    # Add logo if specified
    if logo_path and os.path.exists(logo_path):
        try:
            logo = Image.open(logo_path).convert("RGBA")
            
            # Resize logo to 20% of QR code size
            logo_size = int(qr_img.width * 0.2)
            logo.thumbnail((logo_size, logo_size))
            
            # Calculate position to center logo
            position = (
                (qr_img.width - logo.width) // 2,
                header_height + (qr_img.height - logo.height) // 2
            )
            
            # Create a transparent background for the logo
            logo_mask = logo.split()[3] if logo.mode == 'RGBA' else None
            final_img.paste(logo, position, logo_mask)
            
        except Exception as e:
            print(f"Could not add logo: {e}")
    
    # Generate filename with current date/time if not specified
    if not filename:
        current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"qrcode_{current_time}.png"
    
    final_img.save(filename)
    print(f"QR code saved as {filename}")
    return final_img, filename

def load_font(font_size=28):
    """Load a font with multiple fallbacks"""
    font_paths = [
        "arial.ttf",
        "/System/Library/Fonts/Arial.ttf",
        "C:/Windows/Fonts/arial.ttf"
    ]
    
    for path in font_paths:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, font_size)
            except:
                continue
    return ImageFont.load_default()

def main():
    print("Advanced QR Code Generator")
    print("-" * 35)
    
    data = input("Enter data to encode (URL/text): ").strip() or "https://example.com"
    owner = input("Owner name (leave blank to skip): ").strip()
    title = input("Title (leave blank to skip): ").strip()
    logo = input("Logo path (leave blank to skip): ").strip()
    custom_filename = input("Custom filename (leave blank to auto-generate): ").strip()
    
    generate_qr_with_customizations(
        data=data,
        owner_name=owner,
        title=title,
        logo_path=logo if logo else None,
        filename=custom_filename if custom_filename else None
    )

if __name__ == "__main__":
    main()