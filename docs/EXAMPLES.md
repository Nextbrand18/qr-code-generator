# QR Code Generator Examples

## Basic QR Code
```bash
python qrGenerator.py --data "https://example.com"
```

## QR with Contact Information
```bash
python qrGenerator.py \
  --data "BEGIN:VCARD\nVERSION:3.0\nFN:John Doe\nTEL:+1234567890\nEND:VCARD" \
  --owner "John Doe" \
  --title "Business Card"
```

## WiFi QR Code
```bash
python qrGenerator.py \
  --data "WIFI:T:WPA;S:MyNetwork;P:MyPassword;;" \
  --title "WiFi Access" \
  --output wifi_qr.png
```

## Batch Generation Script
Create `generate_batch.py`:
```python
from qrGenerator import generate_qr_with_customizations
urls = {
    "website": "https://example.com",
    "facebook": "https://facebook.com/page",
    "promo": "https://example.com/special-offer"
}
for name, url in urls.items():
    generate_qr_with_customizations(url, title=name.capitalize(), filename=f"{name}_qr.png")
```