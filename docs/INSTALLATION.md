# Installation Guide

## Requirements
- Python 3.6+
- pip package manager

## Quick Install
```bash
git clone https://github.com/Nextbrand18/qr-code-generator.git
cd qr-code-generator
pip install -r requirements.txt
```

## Platform-Specific Notes

### Windows
```bash
python -m pip install --upgrade pip
python -m venv venv
venv\Scripts\activate
```

### macOS/Linux
```bash
python3 -m pip install --user --upgrade pip
python3 -m venv venv
source venv/bin/activate
```

## Common Issues

### "ModuleNotFoundError"
Solution: Reinstall requirements
```bash
pip install -r requirements.txt
```

### "Could not load font"
Solution: Install system fonts or specify path:
```bash
sudo apt-get install ttf-mscorefonts-installer  # Ubuntu/Debian
brew install --cask font-microsoft  # macOS
```