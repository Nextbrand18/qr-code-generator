import argparse
import sys
from typing import Optional, Tuple

import qrcode
from PIL import Image, ImageDraw, ImageFont
import os
import re
from datetime import datetime

__version__ = "1.0.0"

# def parse_arguments():
#     parser = argparse.ArgumentParser(description='Generate customized QR codes')
#     parser.add_argument('--data', help='Data to encode in QR code')
#     parser.add_argument('--owner', help='Owner name text', default="")
#     parser.add_argument('--title', help='Title text', default="")
#     parser.add_argument('--logo', help='Path to logo image', default="")
#     parser.add_argument('--output', help='Output filename', default=None)
#     return parser.parse_args()

def parse_arguments():
    """Enhanced argument parser with version flag"""
    parser = argparse.ArgumentParser(
        description='Generate customized QR codes with logos and text headers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        '--data', 
        help='Data to encode in QR code (URL/text)',
        default=None
    )
    parser.add_argument(
        '--owner',
        help='Owner name text',
        default=""
    )
    parser.add_argument(
        '--title',
        help='Title text',
        default=""
    )
    parser.add_argument(
        '--logo',
        help='Path to logo image',
        default=None
    )
    parser.add_argument(
        '--output',
        help='Output filename',
        default=None
    )
    parser.add_argument(
        '--version',
        action='version',
        version=f'QR Generator {__version__}',
        help='Show version and exit'
    )
    return parser.parse_args()

def generate_qr_with_customizations(data, owner_name="", title="", logo_path=None, filename=None):
    """
    Generate a QR code with custom branding elements.
    
    Args:
        data (str): Data to encode in QR code (required)
        owner_name (str): Owner name text (optional)
        title (str): Title text (optional)
        logo_path (str): Path to logo image (optional)
        filename (str): Output filename (optional)
        
    Returns:
        tuple: (PIL.Image object, output filename) or None on failure
        
    Raises:
        ValueError: If input validation fails
        IOError: If file operations fail
    """
    try:
        # Validate inputs
        if not data or not isinstance(data, str):
            raise ValueError("Data must be a non-empty string")
            
        if logo_path and not isinstance(logo_path, str):
            raise ValueError("Logo path must be a string")
            
        # Create QR code with dynamic version sizing
        qr = qrcode.QRCode(
            version=None,  # Auto-detect version
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        
        try:
            qr.make(fit=True)
        except qrcode.exceptions.DataOverflowError:
            raise ValueError("Too much data for QR code. Consider using shorter text or a URL shortener")
        
        # Generate QR image with configurable colors
        qr_img = qr.make_image(
            fill_color="black",
            back_color="white",
            embeded_image_path=logo_path if logo_path else None
        ).convert('RGB')
        
        # Calculate dynamic header space
        header_height = calculate_header_height(owner_name, title)
        
        # Create canvas with space for header and QR code
        final_img = Image.new('RGB', (qr_img.width, qr_img.height + header_height), "white")
        final_img.paste(qr_img, (0, header_height))
        
        # Add text elements if specified
        if owner_name or title:
            draw = ImageDraw.Draw(final_img)
            font = load_font()
            
            # Add owner name with shadow effect
            if owner_name:
                add_text_with_effects(draw, owner_name, font, qr_img.width, 10)
            
            # Add title with smaller font
            if title:
                smaller_font = get_smaller_font(font)
                add_text_with_effects(draw, title, smaller_font, qr_img.width, 50 if owner_name else 10)
        
        # Add logo if specified
        if logo_path:
            add_logo(final_img, logo_path, header_height, qr_img.size)
        
        # Generate filename
        filename = generate_filename(filename)
        
        # Save with quality settings
        final_img.save(filename, quality=95, optimize=True)
        print(f"✓ QR code successfully saved as {filename}")
        return final_img, filename
        
    except Exception as e:
        print(f"❌ Error generating QR code: {str(e)}")
        return None

def calculate_header_height(owner_name, title):
    """Calculate appropriate header height based on text elements"""
    if not owner_name and not title:
        return 0
    return 100 if owner_name and title else 60

def add_text_with_effects(draw, text, font, canvas_width, y_pos):
    """Add text with visual enhancements"""
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    x_pos = (canvas_width - text_width) // 2
    
    # Text shadow effect
    draw.text((x_pos+1, y_pos+1), text, fill="#444444", font=font)
    # Main text
    draw.text((x_pos, y_pos), text, fill="black", font=font)

def get_smaller_font(font, reduction=4):
    """Get a smaller version of the current font"""
    if hasattr(font, 'path'):
        try:
            return ImageFont.truetype(font.path, font.size-reduction)
        except:
            return font
    return font

def add_logo(image, logo_path, header_height, qr_size):
    """Add centered logo to QR code"""
    try:
        logo = Image.open(logo_path).convert("RGBA")
        logo_size = int(qr_size[0] * 0.2)  # 20% of QR width
        logo.thumbnail((logo_size, logo_size))
        
        position = (
            (qr_size[0] - logo.width) // 2,
            header_height + (qr_size[1] - logo.height) // 2
        )
        
        logo_mask = logo.split()[3] if logo.mode == 'RGBA' else None
        image.paste(logo, position, logo_mask)
    except Exception as e:
        raise IOError(f"Failed to add logo: {str(e)}")

def generate_filename(filename):
    """Generate proper output filename"""
    if not filename:
        current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"qrcode_{current_time}.png"
    
    if not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        return f"{filename}.png"
    return filename

def load_font(font_size=28):
    """Load font with comprehensive fallback system"""
    font_paths = [
        "arial.ttf",
        "/System/Library/Fonts/Arial.ttf",
        "/Library/Fonts/Arial.ttf",
        "C:/Windows/Fonts/arial.ttf",
        "/usr/share/fonts/truetype/freefont/FreeSans.ttf"
    ]
    
    for path in font_paths:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, font_size)
            except IOError:
                continue
                
    return ImageFont.load_default()


# def main():
#     args = parse_arguments()
    
#     print("Advanced QR Code Generator")
#     print("-" * 35)
    
#     # Get data - command line argument takes priority
#     data = args.data if args.data else input("Enter data to encode (URL/text): ").strip() or "https://example.com"
    
#     # Only prompt for inputs that weren't provided via command line
#     owner = args.owner if args.owner != "" else input("Owner name (leave blank to skip): ").strip()
#     title = args.title if args.title != "" else input("Title (leave blank to skip): ").strip()
#     logo = args.logo if args.logo != "" else input("Logo path (leave blank to skip): ").strip()
#     filename = args.output if args.output else input("Custom filename (leave blank to auto-generate): ").strip()
    
#     generate_qr_with_customizations(
#         data=data,
#         owner_name=owner,
#         title=title,
#         logo_path=logo if logo else None,
#         filename=filename if filename else None
#     )

def main():
    args = parse_arguments()
    
    print("=== QR Code Generator ===")
    print(f"Version {__version__}")
    print("-" * 30)
    
    try:
        print("Initializing...", end='', flush=True)
        # Get inputs
        data = args.data if args.data else input("Enter data to encode (URL/text): ").strip()
        if not data:
            print("\nError: Data cannot be empty")
            sys.exit(1)
            
        print("\rCollecting inputs...", end='', flush=True)
        owner = args.owner if args.owner != "" else input("Owner name (leave blank to skip): ").strip()
        title = args.title if args.title != "" else input("Title (leave blank to skip): ").strip()
        logo = args.logo if args.logo else input("Logo path (leave blank to skip): ").strip()
        filename = args.output if args.output else input("Custom filename (leave blank to auto-generate): ").strip()
        
        print("\rGenerating QR code...", end='', flush=True)
        result = generate_qr_with_customizations(
            data=data,
            owner_name=owner,
            title=title,
            logo_path=logo if logo else None,
            filename=filename if filename else None
        )
        
        if result:
            print(f"\r✔ QR code generated successfully! Saved as: {result[1]}")
        else:
            print("\r✖ Failed to generate QR code")
            
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
        sys.exit(0)
    except Exception as e:
        print(f"\nError: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()