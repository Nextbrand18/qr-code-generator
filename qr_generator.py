import qrcode
from PIL import Image, ImageDraw, ImageFont
import os

def generate_qr_with_text(data, text="Harvester Kent", filename="qr_with_text.png"):
    """
    Generate a QR code with custom text at the top border
    """
    
    print("Creating QR code...")
    
    # Create QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    qr.add_data(data)
    qr.make(fit=True)
    
    print("Generating QR image...")
    
    # Create QR image with fallback
    try:
        qr_img = qr.make_image(fill_color="black", back_color="white")
    except Exception as e:
        print(f"Warning: Couldn't set colors - {e}")
        qr_img = qr.make_image()
    
    # Convert to RGB if not already
    if qr_img.mode != 'RGB':
        qr_img = qr_img.convert('RGB')
    
    qr_width, qr_height = qr_img.size
    print(f"QR code size: {qr_width}x{qr_height}")
    
    # Calculate dimensions for the final image with text
    text_height = 80
    total_height = qr_height + text_height
    
    print("Creating canvas...")
    final_img = Image.new('RGB', (qr_width, total_height), "white")
    
    print("Positioning QR code...")
    # Fixed paste operation
    final_img.paste(qr_img, (0, text_height))
    
    print("Adding text...")
    draw = ImageDraw.Draw(final_img)
    font = load_font()
    
    # Get text dimensions
    try:
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height_actual = bbox[3] - bbox[1]
    except:
        # Fallback calculation
        text_width = len(text) * 15
        text_height_actual = 25
    
    # Calculate position to center text
    text_x = max(0, (qr_width - text_width) // 2)
    text_y = max(0, (text_height - text_height_actual) // 2)
    
    # Draw the text
    draw.text((text_x, text_y), text, fill="black", font=font)
    
    print("Saving image...")
    final_img.save(filename, 'PNG')
    print(f"✓ QR code with text saved as '{filename}'")
    
    return final_img

def load_font(font_size=28):
    """Load a font with multiple fallbacks for different systems"""
    font_paths = [
        # Windows
        "C:/Windows/Fonts/arial.ttf",
        "arial.ttf",
        # macOS  
        "/System/Library/Fonts/Arial.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
        # Linux
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/TTF/arial.ttf",
        "/usr/share/fonts/truetype/ubuntu/Ubuntu-R.ttf",
        "/usr/share/fonts/truetype/freefont/FreeSans.ttf",
    ]
    
    for font_path in font_paths:
        if os.path.exists(font_path):
            try:
                return ImageFont.truetype(font_path, font_size)
            except (IOError, OSError):
                continue
    
    # Final fallbacks
    try:
        return ImageFont.truetype("arial", font_size)  # Try system-resolved name
    except:
        try:
            return ImageFont.load_default()
        except:
            return None  # Explicit return None if all fails

def test_setup():
    """Test the setup before running main program"""
    print("Testing setup...")
    
    try:
        # Test basic imports
        import qrcode
        from PIL import Image, ImageDraw, ImageFont
        print("✓ All imports successful")
        
        # Test basic QR creation
        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data("test")
        qr.make(fit=True)
        
        # Test image creation with explicit factory
        #factory = qrcode.image.pil.PilImage
        factory = None  # Let qrcode use default image factory
        test_img = qr.make_image(
            image_factory=factory,
            fill_color=(0, 0, 0),
            back_color=(255, 255, 255)
        )
        print("✓ QR image creation successful")
        
        # Test PIL operations
        canvas = Image.new('RGB', (100, 100), (255, 255, 255))
        draw = ImageDraw.Draw(canvas)
        font = ImageFont.load_default()
        draw.text((10, 10), "Test", fill=(0, 0, 0), font=font)
        print("✓ PIL operations successful")
        
        return True
        
    except Exception as e:
        print(f"❌ Setup test failed: {e}")
        return False

def main():
    print("QR Code Generator with Custom Text")
    print("-" * 35)
    
    # Test setup first
    if not test_setup():
        print("\nSetup test failed. Please check your installation.")
        return
    
    print("\nSetup test passed! Proceeding with QR generation...\n")
    
    # Get data to encode from user
    data = input("Enter the data to encode in QR code (URL, text, etc.): ").strip()
    
    if not data:
        data = "https://example.com"
        print(f"Using default data: {data}")
    
    # Generate QR code with "Harvester Kent" text
    try:
        generate_qr_with_text(data, "Harvester Kent", "harvester_kent_qr.png")
        print("\n" + "="*50)
        print("✓ QR code generated successfully!")
        print(f"✓ File saved as: harvester_kent_qr.png")
        print(f"✓ QR code contains: {data}")
        print("✓ Text header: Harvester Kent")
        print("="*50)
        
    except Exception as e:
        print(f"\n❌ Error generating QR code: {e}")
        import traceback
        print("\nFull error details:")
        traceback.print_exc()

if __name__ == "__main__":
    main()