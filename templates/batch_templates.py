"""
QR Code Batch Generator Template

This template demonstrates how to generate multiple QR codes programmatically.
Customize the 'items' list with your own data and run the script.
"""


import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from qrGenerator import generate_qr_with_customizations

from datetime import datetime
import os

def generate_batch(output_dir="batch_output"):
    """Generate multiple QR codes in batch"""
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Customize this list with your actual data
    items = [
        {
            "data": "https://example.com",
            "title": "Example Site",
            "owner": "Your Company",
            "logo": "assets/logo.jpg"  # Set path to logo if needed
            
        },
        {
            "data": "https://github.com/yourusername",
            "title": "GitHub Profile",
            "owner": ""
        },
        {
            "data": "https://github.com/Nextbrand18/qr-code-generator",
            "title": "Project QR",
            "owner": "Your Company",
            "logo": "assets/logo.jpg"  # Set path to logo if needed
        }
    ]
    
    print(f"Generating {len(items)} QR codes...")
    
    for idx, item in enumerate(items, 1):
        try:
            # Generate filename from title and date
            clean_title = "".join(c if c.isalnum() else "_" for c in item["title"])
            filename = f"{datetime.now().strftime('%Y%m%d')}_{clean_title}.png"
            output_path = os.path.join(output_dir, filename)
            
            print(f"\n[{idx}/{len(items)}] Generating '{item['title']}'...")
            
            generate_qr_with_customizations(
                data=item["data"],
                owner_name=item.get("owner", ""),
                title=item["title"],
                logo_path=item.get("logo"),
                filename=output_path
            )
            
        except Exception as e:
            print(f"Error generating {item['title']}: {str(e)}")
            continue
    
    print("\nBatch generation complete!")

if __name__ == "__main__":
    generate_batch()