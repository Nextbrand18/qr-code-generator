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