````markdown
## Examples

### Basic QR Code
![Basic QR](examples/qrcode_example.png)

### QR with Text Header
![Text QR](examples/qrcode_with_text.png)

### QR with Logo
![Logo QR](examples/qrcode_with_logo.png)

### QR with all entries
![Entries QR](examples/qrcode_allentries.png)

## Documentation
- [Usage Guide](docs/USAGE.md)
- [Customization Options](docs/CUSTOMIZATION.md)


# qr-code-generator
Python script to generate customized QR codes with logos and text
# QR Code Generator with Custom Branding

![Example QR Code](examples/qrcode_example.png)

A Python script to generate customized QR codes with:
- Owner name/title text
- Centered logo
- Automatic filename generation

## Features
- 📝 Add custom text headers
- 🖼️ Embed company logos
- ⏱️ Automatic date-based filenames
- 🖌️ Customizable colors and sizes
- 📁 Multiple output formats (PNG/JPG)

## Requirements
- Python 3.6+
- Pillow (`pip install pillow`)
- qrcode (`pip install qrcode[pil]`)

## Installation
```bash
git clone https://github.com/YOURUSERNAME/qr-code-generator.git
cd qr-code-generator
pip install -r requirements.txt
```

## Usage
```bash
python qr_generator.py
```
Follow the interactive prompts to:
1. Enter URL/text to encode
2. Add owner name (optional)
3. Add title text (optional)
4. Specify logo path (optional)
5. Set custom filename (optional)

## Examples
### Basic QR Code
```bash
python qr_generator.py
> Enter data: https://example.com
```

### With Custom Branding
```bash
python qr_generator.py
> Enter data: https://example.com
> Owner name: Acme Corp
> Title: Summer Sale 2023
> Logo path: logo.png
```

## Output Files
- Default: `qrcode_YYYYMMDD_HHMMSS.png`
- Custom: Will use specified filename

## Contributing
Pull requests welcome! For major changes, please open an issue first.

## License
[MIT](LICENSE)