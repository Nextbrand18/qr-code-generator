import qrcode
from PIL import Image, ImageDraw, ImageFont

def generate_simple_qr(data, text="Harvester Kent", filename="simple_qr.png"):
    """
    Simplified QR generator to isolate the issue
    """
    print("Step 1: Creating QR code...")
    
    # Create QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    qr.add_data(data)
    qr.make(fit=True)
    
    print("Step 2: Generating QR image...")
    qr_img = qr.make_image(fill_color="black", back_color="white")
    qr_width, qr_height = qr_img.size
    print(f"QR size: {qr_width}x{qr_height}")
    
    print("Step 3: Creating canvas...")
    text_height = 80
    total_height = qr_height + text_height
    final_img = Image.new('RGB', (qr_width, total_height), 'white')
    print(f"Canvas size: {qr_width}x{total_height}")
    
    print("Step 4: Pasting QR code...")
    final_img.paste(qr_img, (0, text_height))
    
    print("Step 5: Adding text...")
    draw = ImageDraw.Draw(final_img)
    
    # Use default font and simple positioning
    font = ImageFont.load_default()
    
    # Simple text positioning without bbox calculation
    text_x = 20  # Fixed position from left edge
    text_y = 20  # Fixed position from top edge
    
    print(f"Drawing text '{text}' at position ({text_x}, {text_y})")
    draw.text((text_x, text_y), text, fill="black", font=font)
    
    print("Step 6: Saving image...")
    final_img.save(filename)
    print(f"✓ Success! Saved as '{filename}'")
    
    return final_img

def main():
    print("=== SIMPLE QR GENERATOR - DEBUG VERSION ===")
    
    data = input("Enter data to encode: ").strip()
    if not data:
        data = "https://example.com"
    
    try:
        generate_simple_qr(data, "Harvester Kent", "debug_qr.png")
        print("\n✓ QR code created successfully!")
        print("✓ Check 'debug_qr.png' in your current directory")
        
    except Exception as e:
        print(f"\n❌ Error at step: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()