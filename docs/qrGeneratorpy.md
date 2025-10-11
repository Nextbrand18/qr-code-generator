# qrGenerator.py - Complete Code Explanation

This document explains every line of code in `qrGenerator.py`, the core QR code generation module.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Imports](#imports)
- [Module Metadata](#module-metadata)
- [Main Function](#main-function)
- [Helper Functions](#helper-functions)
- [Code Flow Diagram](#code-flow-diagram)
- [Complete Annotated Code](#complete-annotated-code)

---

## 🎯 Overview

**File:** `qrGenerator.py`  
**Purpose:** Generate QR codes with optional customizations (owner text, title, logo)  
**Type:** Pure Python module (no web dependencies)  
**Can be used:** Standalone or imported by other scripts

**Main Function:**
```python
generate_qr_with_customizations(data, owner_name, title, logo_path, filename)
```

**Returns:** `(PIL.Image object, filename)` or `None` on failure

---

## 📦 Imports

### Line 1: `import qrcode`

```python
import qrcode
```

**What it does:**
- Imports the `qrcode` library
- This library creates QR code images from text/data

**Why we need it:**
- Core functionality - without this, we can't generate QR codes
- Provides the `QRCode` class with all QR generation logic

**Documentation:** https://pypi.org/project/qrcode/

---

### Line 2: `from PIL import Image, ImageDraw, ImageFont`

```python
from PIL import Image, ImageDraw, ImageFont
```

**What it does:**
- Imports specific classes from the PIL (Pillow) library
- PIL = Python Imaging Library (fork called Pillow)

**Breaking it down:**
- `Image` - Create, open, save, and manipulate images
- `ImageDraw` - Drawing functions (text, shapes, lines)
- `ImageFont` - Font handling for text rendering

**Why we need it:**
- `Image` - Create the final canvas, paste QR code, add logo
- `ImageDraw` - Add owner name and title text
- `ImageFont` - Load fonts to make text look good

**Documentation:** https://pillow.readthedocs.io/

---

### Line 3: `import os`

```python
import os
```

**What it does:**
- Imports the operating system interface module

**Why we need it:**
- Check if font files exist (`os.path.exists()`)
- Handle file paths correctly across Windows/Mac/Linux
- File system operations

**Example usage in our code:**
```python
if os.path.exists(path):  # Check if Arial font file exists
```

---

### Line 4: `from datetime import datetime`

```python
from datetime import datetime
```

**What it does:**
- Imports the `datetime` class from the datetime module

**Why we need it:**
- Generate unique filenames with timestamps
- Example: `qrcode_20231011_143059.png`

**Used in:** `generate_filename()` function

---

## 🏷️ Module Metadata

### Line 6: `__version__ = "1.0.0"`

```python
__version__ = "1.0.0"
```

**What it does:**
- Defines the version number of this module
- Standard Python convention using double underscores

**Why we need it:**
- Version tracking
- Can be accessed by other code: `import qrGenerator; print(qrGenerator.__version__)`
- Helps with debugging ("Which version am I using?")
- Semantic versioning: MAJOR.MINOR.PATCH

**When to update:**
- MAJOR (1.x.x) - Breaking changes
- MINOR (x.1.x) - New features, backwards compatible
- PATCH (x.x.1) - Bug fixes

---

## 🎯 Main Function

### Lines 8-20: Function Definition and Docstring

```python
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
```

**Breaking it down:**

**Line 8:** Function signature
```python
def generate_qr_with_customizations(data, owner_name="", title="", logo_path=None, filename=None):
```

- `def` - Define a function
- `generate_qr_with_customizations` - Function name (descriptive)
- **Parameters:**
  - `data` - **Required** (no default value) - The content to encode
  - `owner_name=""` - Optional (defaults to empty string)
  - `title=""` - Optional (defaults to empty string)
  - `logo_path=None` - Optional (defaults to None = no logo)
  - `filename=None` - Optional (auto-generated if not provided)

**Lines 9-20:** Docstring (documentation)
- Triple quotes `"""..."""` = multi-line string
- Explains what the function does
- Lists all parameters with types
- Describes return value
- **Best practice** - Always document your functions!

---

### Lines 21-23: Try Block and Input Validation

```python
    try:
        if not data or not isinstance(data, str):
            raise ValueError("Data must be a non-empty string")
```

**Line 21:** `try:`
- Start a try-except block for error handling
- Any errors inside will be caught by `except` at the end

**Line 22:** Input validation
```python
if not data or not isinstance(data, str):
```

Breaking down the condition:
- `not data` - Checks if data is empty, None, or falsy
  - Empty string: `""` → `True` (not data)
  - None: `None` → `True` (not data)
  - Valid data: `"hello"` → `False` (not data)

- `or` - If EITHER condition is true, execute the block

- `not isinstance(data, str)` - Checks if data is NOT a string
  - `isinstance(data, str)` checks type
  - `not` reverses it
  - Example: `isinstance(123, str)` → `False`

**Line 23:** Raise error if validation fails
```python
raise ValueError("Data must be a non-empty string")
```
- `raise` - Throw an exception
- `ValueError` - Type of exception (built-in)
- Error message explains what went wrong
- Function stops here if this runs

---

### Lines 25-30: QR Code Configuration

```python
        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
```

**Line 25:** Create QR code object
```python
qr = qrcode.QRCode(...)
```
- Creates an instance of the QRCode class
- Stores it in variable `qr`
- We'll use `qr` to generate the actual image

**Line 26:** `version=None`
```python
version=None,
```
- **Version** = QR code size (1-40)
- `None` = Auto-detect based on data length
- Smaller data = smaller QR code
- Larger data = bigger QR code (more squares)
- **Best practice:** Use `None` for flexibility

**Line 27:** Error correction level
```python
error_correction=qrcode.constants.ERROR_CORRECT_H,
```
- **Error correction** = How much damage QR can tolerate and still scan
- `ERROR_CORRECT_H` = **Highest** (30% recovery)
- Other options:
  - `ERROR_CORRECT_L` - Low (7%)
  - `ERROR_CORRECT_M` - Medium (15%)
  - `ERROR_CORRECT_Q` - Quartile (25%)
  - `ERROR_CORRECT_H` - High (30%) ← **We use this**

**Why HIGH?**
- We're adding logos in the center
- Logo covers some QR code squares
- High error correction allows this
- QR code still scans even with logo

**Line 28:** Box size
```python
box_size=10,
```
- **Box size** = Size of each black/white square in pixels
- `10` = Each square is 10x10 pixels
- Larger number = bigger QR code image
- Default is usually 10
- Increase for higher resolution

**Line 29:** Border size
```python
border=4,
```
- **Border** = White space around QR code
- `4` = 4 boxes of white border
- QR spec requires minimum of 4
- Helps scanners detect the QR code edges
- Don't set lower than 4

---

### Lines 31-32: Add Data and Generate

```python
        qr.add_data(data)
        qr.make(fit=True)
```

**Line 31:** Add data to encode
```python
qr.add_data(data)
```
- Takes the `data` parameter (URL, text, etc.)
- Adds it to the QR code object
- Doesn't generate the image yet (just stores the data)
- Can call multiple times to add more data

**Line 32:** Generate the QR code
```python
qr.make(fit=True)
```
- `make()` - Actually generates the QR code
- `fit=True` - Automatically chooses best version for data length
- Calculates optimal size
- Creates the QR code matrix (grid of black/white squares)
- Still not an image yet - just the data structure

---

### Line 33: Create QR Image

```python
        qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
```

**Breaking down this complex line:**

1. `qr.make_image(...)` - Convert QR matrix to actual image
   - Takes the QR data structure
   - Creates a PIL Image object

2. `fill_color="black"` - Color of QR code squares
   - The dark squares in QR code
   - Could be any color: "red", "#FF0000", etc.

3. `back_color="white"` - Background color
   - The light squares
   - Could be any color

4. `.convert("RGB")` - Convert to RGB color mode
   - QR code is initially 1-bit (black/white)
   - RGB = 3 channels (Red, Green, Blue)
   - **Why?** We'll add colored text and logo later
   - RGB mode supports full color

5. `qr_img =` - Store the result
   - Now we have an actual image object
   - Can manipulate, save, display it

---

### Lines 35-37: Calculate Header Height

```python
        # Header height for text
        header_height = 100 if owner_name or title else 0
        final_img = Image.new("RGB", (qr_img.width, qr_img.height + header_height), "white")
```

**Line 36:** Calculate header space
```python
header_height = 100 if owner_name or title else 0
```

**Ternary operator:** `value_if_true if condition else value_if_false`

Breaking it down:
- `owner_name or title` - Check if either exists
  - If owner_name has text: `True`
  - If title has text: `True`
  - If both empty: `False`

- `if ... else` - Conditional assignment
  - If True: `header_height = 100` (pixels)
  - If False: `header_height = 0` (no header needed)

**Why 100 pixels?**
- Enough space for two lines of text
- Owner name: ~40 pixels
- Title: ~30 pixels
- Spacing: ~30 pixels
- Total: ~100 pixels

**Line 37:** Create final canvas
```python
final_img = Image.new("RGB", (qr_img.width, qr_img.height + header_height), "white")
```

Breaking it down:
- `Image.new()` - Create a new blank image
- `"RGB"` - Color mode (Red, Green, Blue)
- `(qr_img.width, qr_img.height + header_height)` - Size tuple
  - Width: Same as QR code
  - Height: QR code height + header space
  - `+` adds header space at top
- `"white"` - Background color
- `final_img =` - Store the new canvas

**Visual representation:**
```
┌─────────────────┐
│   Header (100px)│ ← Space for text (if needed)
├─────────────────┤
│                 │
│   QR Code       │ ← Original QR code
│                 │
└─────────────────┘
```

---

### Line 38: Paste QR Code

```python
        final_img.paste(qr_img, (0, header_height))
```

**What it does:**
- Takes the QR code image (`qr_img`)
- Pastes it onto the final canvas (`final_img`)
- At position `(0, header_height)`

**Position explained:**
- `(x, y)` coordinates
- `x=0` - Left edge (no offset)
- `y=header_height` - Below the header
  - If header is 100px, QR starts at y=100
  - If no header (0px), QR starts at y=0

**Visual:**
```
(0,0) ─────────────> x
  │   ┌─────────────┐
  │   │  Header     │
  y   ├─────────────┤ ← (0, header_height) paste here
  │   │   QR Code   │
  ↓   └─────────────┘
```

---

### Lines 40-48: Add Text to Header

```python
        # Draw text
        if owner_name or title:
            draw = ImageDraw.Draw(final_img)
            font = load_font()

            if owner_name:
                add_text(draw, owner_name, font, qr_img.width, 10)
            if title:
                add_text(draw, title, get_smaller_font(font), qr_img.width, 50 if owner_name else 10)
```

**Line 41:** Check if text is needed
```python
if owner_name or title:
```
- Only run if we have owner name OR title
- Skip all text drawing if both are empty
- Saves processing time

**Line 42:** Create drawing context
```python
draw = ImageDraw.Draw(final_img)
```
- `ImageDraw.Draw()` - Creates a drawing object
- Linked to `final_img` - anything we draw appears on this image
- `draw` object has methods like `.text()`, `.line()`, `.rectangle()`

**Line 43:** Load font
```python
font = load_font()
```
- Calls our helper function (defined later)
- Tries to load Arial font
- Falls back to default if Arial not found
- Returns a font object

**Line 45-46:** Draw owner name
```python
if owner_name:
    add_text(draw, owner_name, font, qr_img.width, 10)
```
- Only if owner_name has value
- Calls our helper function `add_text()`
- Parameters:
  - `draw` - Drawing context
  - `owner_name` - Text to draw
  - `font` - Font to use
  - `qr_img.width` - Canvas width (for centering)
  - `10` - Y position (10 pixels from top)

**Line 47-48:** Draw title
```python
if title:
    add_text(draw, title, get_smaller_font(font), qr_img.width, 50 if owner_name else 10)
```
- Only if title has value
- Uses `get_smaller_font(font)` - Slightly smaller than owner name
- Y position: `50 if owner_name else 10`
  - If owner name exists: y=50 (below owner name)
  - If no owner name: y=10 (at top)

---

### Lines 50-52: Add Logo

```python
        # Add logo
        if logo_path:
            add_logo(final_img, logo_path, header_height, qr_img.size)
```

**Line 51:** Check if logo provided
```python
if logo_path:
```
- Only run if user provided a logo path
- `logo_path` could be `None` or empty string

**Line 52:** Add logo to QR code
```python
add_logo(final_img, logo_path, header_height, qr_img.size)
```
- Calls our helper function
- Parameters:
  - `final_img` - Image to modify (passed by reference)
  - `logo_path` - File path to logo
  - `header_height` - Offset for positioning
  - `qr_img.size` - QR code dimensions

---

### Lines 54-56: Save Image

```python
        # Generate filename
        filename = filename or generate_filename()
        final_img.save(filename, quality=95, optimize=True)
```

**Line 55:** Generate filename if needed
```python
filename = filename or generate_filename()
```
- **or operator with assignment**
- If `filename` was provided: use it
- If `filename` is `None`: call `generate_filename()`
- Example:
  ```python
  filename = "custom.png"  # Use this
  # or
  filename = None  # Generate: qrcode_20231011_143059.png
  ```

**Line 56:** Save the image
```python
final_img.save(filename, quality=95, optimize=True)
```
- `.save()` - Write image to disk
- `filename` - Where to save
- `quality=95` - JPEG quality (0-100, higher=better)
  - Even for PNG, affects size vs quality tradeoff
  - 95 is very high quality
- `optimize=True` - Compress file size without quality loss
  - Takes slightly longer but smaller file
  - Good for web use

---

### Lines 57-58: Return Success

```python
        return final_img, filename
```

**What it returns:**
- A **tuple** (two values)
- `final_img` - The PIL Image object (in memory)
  - Can be displayed, modified, saved again
- `filename` - The path where it was saved
  - String like "qrcode_20231011.png"

**Why return both?**
- Flexibility
- Caller can display the image (use `final_img`)
- Caller knows where file was saved (use `filename`)

**Example usage:**
```python
img, path = generate_qr_with_customizations("Hello")
print(f"Saved to: {path}")
img.show()  # Display the image
```

---

### Lines 60-62: Error Handling

```python
    except Exception as e:
        print(f"Error generating QR: {e}")
        return None
```

**Line 60:** Catch all exceptions
```python
except Exception as e:
```
- `except` - Catches errors from `try` block
- `Exception` - Base class for all errors (catches everything)
- `as e` - Store the error in variable `e`

**Line 61:** Print error message
```python
print(f"Error generating QR: {e}")
```
- `f"..."` - F-string (formatted string literal)
- `{e}` - Inserts the error message
- Prints to console for debugging
- Example output: `Error generating QR: File not found`

**Line 62:** Return None on failure
```python
return None
```
- Signals that function failed
- Caller should check: `if result is None:`
- Alternative: Could raise the exception instead
- **Design choice:** Graceful failure vs. propagate error

---

## 🔧 Helper Functions

### Lines 64-65: Comment Separator

```python
# ---------------------- Helper functions ----------------------
```

**Purpose:**
- Visual separator in code
- Makes code more readable
- Groups related functions together
- **Best practice:** Use comments to organize code

---

## 🔤 Font Loading Function

### Lines 67-78: `load_font()` Function

```python
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
```

**Line 67:** Function definition
```python
def load_font(size=28):
```
- `size=28` - Default font size in points
- Larger number = bigger text
- Can be changed: `load_font(36)` for bigger font

**Lines 68-71:** Define font paths
```python
paths = [
    "arial.ttf",
    "C:/Windows/Fonts/arial.ttf"
]
```
- **List of possible locations** for Arial font
- `"arial.ttf"` - Current directory (Linux/Mac)
- `"C:/Windows/Fonts/arial.ttf"` - Windows location
- Tries in order

**Why multiple paths?**
- Cross-platform compatibility
- Windows stores fonts differently than Linux/Mac
- If one fails, try the next

**Line 72:** Loop through paths
```python
for path in paths:
```
- Try each path in the list
- Stops when one works

**Line 73:** Check if file exists
```python
if os.path.exists(path):
```
- `os.path.exists()` - Returns True if file found
- Avoids errors from trying to open missing files
- Only try to load if file is actually there

**Lines 74-77:** Try to load font
```python
try:
    return ImageFont.truetype(path, size)
except:
    continue
```

- **Line 75:** Load TrueType font
  - `ImageFont.truetype()` - Load font from file
  - `path` - Font file location
  - `size` - Font size in points
  - Returns font object if successful

- **Line 76-77:** Handle errors
  - `except:` - Catch ANY error (not best practice, but simple)
  - `continue` - Try next path
  - Errors might occur if file is corrupted or wrong format

**Line 78:** Fallback font
```python
return ImageFont.load_default()
```
- Only reached if all paths fail
- Loads PIL's built-in default font
- Not pretty, but always works
- Small, bitmap font

**Function flow:**
```
1. Try current directory
   ↓ (if not found)
2. Try Windows Fonts folder
   ↓ (if not found)
3. Use default font
   ✓ (always works)
```

---

## 📏 Font Size Adjustment Function

### Lines 80-84: `get_smaller_font()` Function

```python
def get_smaller_font(font, reduction=4):
    try:
        return ImageFont.truetype(font.path, font.size - reduction)
    except:
        return font
```

**Line 80:** Function definition
```python
def get_smaller_font(font, reduction=4):
```
- `font` - Existing font object to make smaller
- `reduction=4` - How many points smaller (default 4)
- Example: 28pt font → 24pt font

**Lines 81-82:** Try to create smaller font
```python
try:
    return ImageFont.truetype(font.path, font.size - reduction)
```

- `font.path` - Path to the font file
- `font.size` - Current size in points
- `font.size - reduction` - New size
  - If size=28 and reduction=4: 28-4=24
- `ImageFont.truetype()` - Load same font, different size

**Lines 83-84:** Error handling
```python
except:
    return font
```
- If anything fails, return original font
- **Why might it fail?**
  - Font is the default font (has no `.path` attribute)
  - Font file was deleted
  - Permissions issue
- Better to use original than crash

**Usage:**
```python
big_font = load_font(28)          # 28pt font
small_font = get_smaller_font(big_font)  # 24pt font
```

---

## ✍️ Text Drawing Function

### Lines 86-92: `add_text()` Function

```python
def add_text(draw, text, font, canvas_width, y_pos):
    bbox = draw.textbbox((0,0), text, font=font)
    text_width = bbox[2] - bbox[0]
    x_pos = (canvas_width - text_width)//2
    # Shadow
    draw.text((x_pos+1, y_pos+1), text, fill="#444", font=font)
    # Main text
    draw.text((x_pos, y_pos), text, fill="black", font=font)
```

**Line 86:** Function definition
```python
def add_text(draw, text, font, canvas_width, y_pos):
```
- `draw` - ImageDraw object (where to draw)
- `text` - String to display
- `font` - Font object to use
- `canvas_width` - Width of image (for centering)
- `y_pos` - Vertical position (pixels from top)

**Line 87:** Get text dimensions
```python
bbox = draw.textbbox((0,0), text, font=font)
```
- `textbbox()` - Calculate text bounding box
- `(0,0)` - Reference position (doesn't matter, we calculate size)
- Returns tuple: `(left, top, right, bottom)`
- Example: `(0, 0, 150, 32)` for 150px wide, 32px tall text

**Line 88:** Calculate text width
```python
text_width = bbox[2] - bbox[0]
```
- `bbox[2]` - Right edge (x coordinate)
- `bbox[0]` - Left edge (x coordinate)
- Difference = width in pixels
- Example: `150 - 0 = 150px`

**Line 89:** Calculate centered X position
```python
x_pos = (canvas_width - text_width)//2
```
- `canvas_width - text_width` - Remaining space
- `//2` - Integer division (divide by 2, drop decimals)
- Centers the text horizontally

**Example:**
```
Canvas: 400px wide
Text: 150px wide
Remaining: 400 - 150 = 250px
x_pos: 250 // 2 = 125px

┌────────────────────────────────────┐
│       ┌──────────┐                 │
│ 125px │   Text   │      125px      │
│       └──────────┘                 │
└────────────────────────────────────┘
```

**Line 91:** Draw shadow text
```python
draw.text((x_pos+1, y_pos+1), text, fill="#444", font=font)
```
- `(x_pos+1, y_pos+1)` - Offset by 1 pixel right and down
- `fill="#444"` - Dark gray color (hex code)
- Creates shadow effect
- Drawn FIRST (behind main text)

**Line 93:** Draw main text
```python
draw.text((x_pos, y_pos), text, fill="black", font=font)
```
- `(x_pos, y_pos)` - Exact position
- `fill="black"` - Text color
- Drawn SECOND (on top of shadow)
- Creates depth effect

**Visual result:**
```
Regular text:  Hello
With shadow:   Hello (with slight gray offset)
```

---

## 🖼️ Logo Adding Function

### Lines 94-104: `add_logo()` Function

```python
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
```

**Line 94:** Function definition
```python
def add_logo(image, logo_path, header_height, qr_size):
```
- `image` - Final image to modify (passed by reference)
- `logo_path` - Path to logo file
- `header_height` - Offset for Y position
- `qr_size` - QR code dimensions `(width, height)`

**Line 95:** Start error handling
```python
try:
```
- Logo loading can fail many ways
- File not found, corrupt file, wrong format, etc.

**Line 96:** Open and convert logo
```python
logo = Image.open(logo_path).convert("RGBA")
```
- `Image.open()` - Read image from file
- `.convert("RGBA")` - Convert to RGBA mode
  - R = Red channel
  - G = Green channel
  - B = Blue channel
  - **A = Alpha channel (transparency)**
- **Why RGBA?** Preserve logo transparency

**Line 97:** Calculate logo size
```python
size = int(qr_size[0]*0.2)
```
- `qr_size[0]` - QR code width
- `*0.2` - 20% of QR code width
- `int()` - Convert to integer (pixels must be whole numbers)
- Example: 400px QR → 80px logo

**Why 20%?**
- Large enough to see
- Small enough not to break QR code
- With HIGH error correction, 30% can be covered
- 20% is safe margin

**Line 98:** Resize logo
```python
logo.thumbnail((size, size))
```
- `.thumbnail()` - Resize preserving aspect ratio
- `(size, size)` - Maximum dimensions
- If logo is rectangular, fits within this square
- **Modifies logo in-place** (doesn't return new image)
- Example: 1000x500 logo → fits in 80x80 → becomes 80x40

**Line 99:** Calculate centered position
```python
pos = ((qr_size[0]-logo.width)//2, header_height + (qr_size[1]-logo.height)//2)
```

Breaking down this tuple:
- **X position:** `(qr_size[0]-logo.width)//2`
  - QR width minus logo width = remaining space
  - Divide by 2 = center horizontally
  
- **Y position:** `header_height + (qr_size[1]-logo.height)//2`
  - Start after header: `header_height`
  - Center in QR code: `(qr_size[1]-logo.height)//2`
  - Add them together

**Visual:**
```
┌──────────────────┐
│    Header        │
├──────────────────┤
│                  │
│    ┌──────┐      │  ← Logo centered
│    │ LOGO │      │     in QR code area
│    └──────┘      │
│                  │
└──────────────────┘
```

**Line 100:** Get transparency mask
```python
mask = logo.split()[3] if logo.mode=="RGBA" else None
```

**Complex line! Breaking it down:**

1. `logo.split()` - Split image into separate channels
   - Returns list: `[R, G, B, A]`
   - Each is a separate grayscale image

2. `[3]` - Get 4th element (index 3)
   - This is the Alpha (transparency) channel
   - Shows where logo is transparent vs opaque

3. `if logo.mode=="RGBA"` - Only if logo has transparency
   - Some images don't have alpha channel (JPG)
   - Check mode first to avoid errors

4. `else None` - If no alpha channel, use None
   - Will paste entire rectangle (no transparency)

**What is a mask?**
- Tells PIL which pixels to paste
- White (255) = paste this pixel
- Black (0) = don't paste (keep background)
- Gray = partial transparency

**Line 101:** Paste logo onto image
```python
image.paste(logo, pos, mask)
```
- `image` - Destination (our final QR image)
- `logo` - Source (what to paste)
- `pos` - Position tuple `(x, y)`
- `mask` - Transparency information
  - If mask is None: paste entire rectangle
  - If mask provided: respect transparency

**Why mask matters:**
```
Without mask:        With mask:
┌─────────┐         ┌─────────┐
│ ░░░░░░░ │         │ ▓▓▓▓▓▓▓ │
│ ░LOGO░  │         │ ▓LOGO▓  │  ← Transparent areas
│ ░░░░░░░ │         │ ▓▓▓▓▓▓▓ │     show QR code
└─────────┘         └─────────┘
White box visible   Transparent!
```

**Lines 102-103:** Error handling
```python
except Exception as e:
    print(f"Failed to add logo: {e}")
```
- Catch any errors
- Print descriptive message
- **Don't crash the whole function**
- QR code still works without logo

**Common errors:**
- File not found
- Invalid image format
- Corrupted file
- Permission denied
- Out of memory (huge images)

---

## 📝 Filename Generation Function

### Lines 106-108: `generate_filename()` Function

```python
def generate_filename():
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"qrcode_{now}.png"
```

**Line 106:** Function definition
```python
def generate_filename():
```
- No parameters needed
- Always generates a new unique filename
- Uses current date/time

**Line 107:** Create timestamp string
```python
now = datetime.now().strftime("%Y%m%d_%H%M%S")
```

**Breaking it down:**

1. `datetime.now()` - Get current date and time
   - Returns datetime object
   - Example: `2023-10-11 14:30:59.123456`

2. `.strftime(...)` - Format as string
   - "string format time"
   - Takes format codes

3. Format codes:
   - `%Y` - 4-digit year (2023)
   - `%m` - 2-digit month (10)
   - `%d` - 2-digit day (11)
   - `_` - Underscore separator
   - `%H` - 2-digit hour, 24h format (14)
   - `%M` - 2-digit minute (30)
   - `%S` - 2-digit second (59)

**Example output:** `"20231011_143059"`

**Line 108:** Return formatted filename
```python
return f"qrcode_{now}.png"
```
- F-string: `f"...{variable}..."`
- `{now}` - Inserts the timestamp
- Final result: `"qrcode_20231011_143059.png"`

**Why this format?**
- ✅ Always unique (unless generated same second)
- ✅ Sorts chronologically by name
- ✅ Easy to identify when created
- ✅ No spaces (web-safe)
- ✅ Includes file extension

**Example sequence:**
```
qrcode_20231011_143000.png
qrcode_20231011_143001.png
qrcode_20231011_143059.png
qrcode_20231011_144530.png
```

---

## 📊 Code Flow Diagram

```
START: generate_qr_with_customizations()
  │
  ├─► Validate input (data must be string)
  │   └─► If invalid → raise ValueError
  │
  ├─► Create QR code object with settings
  │   ├─ version=None (auto-size)
  │   ├─ error_correction=HIGH (30%)
  │   ├─ box_size=10 pixels
  │   └─ border=4 boxes
  │
  ├─► Add data to QR code
  │
  ├─► Generate QR code matrix
  │
  ├─► Convert to RGB image (black & white)
  │
  ├─► Calculate header height
  │   ├─ If owner_name OR title → 100px
  │   └─ Else → 0px
  │
  ├─► Create final canvas
  │   └─ Size: QR width × (QR height + header)
  │
  ├─► Paste QR code onto canvas
  │   └─ Position: (0, header_height)
  │
  ├─► If owner_name or title exists:
  │   ├─► Create drawing context
  │   ├─► Load font (Arial or default)
  │   ├─► If owner_name:
  │   │   └─► Draw centered text at y=10
  │   └─► If title:
  │       └─► Draw centered text at y=50 or y=10
  │
  ├─► If logo_path provided:
  │   ├─► Open logo image
  │   ├─► Convert to RGBA (transparency)
  │   ├─► Resize to 20% of QR width
  │   ├─► Calculate center position
  │   ├─► Extract alpha mask
  │   └─► Paste logo onto QR code center
  │
  ├─► Generate filename (if not provided)
  │   └─ Format: qrcode_YYYYMMDD_HHMMSS.png
  │
  ├─► Save image to file
  │   ├─ quality=95 (high quality)
  │   └─ optimize=True (compress)
  │
  └─► Return (image_object, filename)

If ANY error occurs:
  ├─► Print error message
  └─► Return None
```

---

## 🎨 Visual Representation

### What the Code Creates

```
┌─────────────────────────────────────┐
│         Acme Corporation             │ ← owner_name (28pt font)
│                                      │
│          Product Manual              │ ← title (24pt font)
├──────────────────────────────────────┤
│  ▓▓▓▓▓▓▓▓      ▓▓  ▓▓▓▓▓▓▓▓        │
│  ▓      ▓  ▓▓  ▓▓  ▓      ▓        │
│  ▓ ▓▓▓▓ ▓  ▓▓      ▓ ▓▓▓▓ ▓        │ ← QR Code
│  ▓ ▓▓▓▓ ▓      ▓▓  ▓ ▓▓▓▓ ▓        │   (version auto)
│  ▓ ▓▓▓▓ ▓  ┌───┐   ▓ ▓▓▓▓ ▓        │   (error correction HIGH)
│  ▓      ▓  │   │   ▓      ▓        │   (box_size 10px)
│  ▓▓▓▓▓▓▓▓  │ L │   ▓▓▓▓▓▓▓▓        │   (border 4 boxes)
│      ▓▓    └───┘         ▓▓        │
│  ▓▓  ▓▓  ▓▓  ▓▓  ▓▓  ▓▓            │
│        ▓▓▓▓      ▓▓  ▓▓  ▓▓        │
└─────────────────────────────────────┘
         │                  │
         └──────┬───────────┘
                │
            Logo in center
         (20% of QR width)
       (with transparency)
```

---

## 📝 Complete Annotated Code

Here's the entire file with inline comments:

```python
# Line 1: Import QR code generation library
import qrcode

# Line 2: Import image manipulation tools from PIL (Pillow)
from PIL import Image, ImageDraw, ImageFont

# Line 3: Import OS utilities for file operations
import os

# Line 4: Import datetime for timestamp generation
from datetime import datetime

# Line 6: Module version number (semantic versioning)
__version__ = "1.0.0"

# Lines 8-20: Main function that generates customized QR codes
def generate_qr_with_customizations(data, owner_name="", title="", logo_path=None, filename=None):
    """
    Generate a QR code with optional owner, title, and logo.
    
    This function creates a QR code image with customizations:
    - Adds header text (owner name and/or title) above QR code
    - Embeds a logo in the center of the QR code
    - Saves the result to a file
    
    Args:
        data (str): Content to encode in QR code (URL, text, etc.) - REQUIRED
        owner_name (str): Text displayed at top of image - OPTIONAL
        title (str): Text displayed below owner name - OPTIONAL
        logo_path (str): File path to logo image to embed - OPTIONAL
        filename (str): Output filename (auto-generated if None) - OPTIONAL

    Returns:
        tuple: (PIL.Image object, filename string) on success
        None: On failure (with error message printed)
    
    Example:
        img, path = generate_qr_with_customizations(
            data="https://example.com",
            owner_name="My Company",
            title="Product Page",
            logo_path="logo.png"
        )
    """
    
    # Line 21: Start error handling block
    try:
        # Line 22-23: Validate that data is a non-empty string
        if not data or not isinstance(data, str):
            # Raise exception if validation fails
            raise ValueError("Data must be a non-empty string")

        # Lines 25-30: Configure QR code parameters
        qr = qrcode.QRCode(
            version=None,  # Auto-detect size based on data length
            error_correction=qrcode.constants.ERROR_CORRECT_H,  # 30% recovery (allows logos)
            box_size=10,  # Each square is 10x10 pixels
            border=4,  # 4 boxes of white space around QR (minimum required)
        )
        
        # Line 31: Add the data to encode
        qr.add_data(data)
        
        # Line 32: Generate the QR code matrix
        qr.make(fit=True)  # fit=True chooses optimal version
        
        # Line 33: Convert QR matrix to RGB image (black squares on white background)
        qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

        # Lines 35-37: Create canvas with optional header space
        # Line 36: Calculate header height (100px if text, 0px if no text)
        header_height = 100 if owner_name or title else 0
        
        # Line 37: Create new white canvas (width × height+header)
        final_img = Image.new("RGB", (qr_img.width, qr_img.height + header_height), "white")
        
        # Line 38: Paste QR code onto canvas below header
        final_img.paste(qr_img, (0, header_height))

        # Lines 40-48: Add text to header if provided
        if owner_name or title:
            # Line 42: Create drawing context for adding text
            draw = ImageDraw.Draw(final_img)
            
            # Line 43: Load Arial font or fallback to default
            font = load_font()

            # Lines 45-46: Draw owner name at top (y=10)
            if owner_name:
                add_text(draw, owner_name, font, qr_img.width, 10)
            
            # Lines 47-48: Draw title below owner (y=50) or at top if no owner (y=10)
            if title:
                add_text(draw, title, get_smaller_font(font), qr_img.width, 50 if owner_name else 10)

        # Lines 50-52: Add logo to center of QR code if provided
        if logo_path:
            add_logo(final_img, logo_path, header_height, qr_img.size)

        # Lines 54-56: Save the final image
        # Line 55: Use provided filename or generate timestamp-based name
        filename = filename or generate_filename()
        
        # Line 56: Save with high quality and optimization
        final_img.save(filename, quality=95, optimize=True)
        
        # Line 57: Return both the image object and filename
        return final_img, filename

    # Lines 60-62: Handle any errors gracefully
    except Exception as e:
        # Print error message for debugging
        print(f"Error generating QR: {e}")
        # Return None to indicate failure
        return None

# Line 64: Visual separator comment
# ---------------------- Helper functions ----------------------

# Lines 67-78: Load Arial font with fallback to default
def load_font(size=28):
    """
    Attempt to load Arial font, fall back to default if unavailable.
    
    Tries multiple paths for cross-platform compatibility:
    1. Current directory (Linux/Mac)
    2. Windows Fonts directory
    3. PIL default font (last resort)
    
    Args:
        size (int): Font size in points (default 28)
    
    Returns:
        ImageFont object: Arial font or default font
    """
    # Line 68-71: List of possible Arial font locations
    paths = [
        "arial.ttf",  # Current directory or system fonts (Mac/Linux)
        "C:/Windows/Fonts/arial.ttf"  # Windows fonts directory
    ]
    
    # Line 72: Try each path in order
    for path in paths:
        # Line 73: Check if font file exists
        if os.path.exists(path):
            # Lines 74-77: Try to load the font
            try:
                # Load TrueType font at specified size
                return ImageFont.truetype(path, size)
            except:
                # If loading fails, try next path
                continue
    
    # Line 78: Last resort - use PIL's built-in default font
    return ImageFont.load_default()

# Lines 80-84: Create a smaller version of a font
def get_smaller_font(font, reduction=4):
    """
    Create a smaller version of the given font.
    
    Used to make title text slightly smaller than owner name text.
    
    Args:
        font (ImageFont): Original font object
        reduction (int): How many points smaller (default 4)
    
    Returns:
        ImageFont object: Smaller font, or original if sizing fails
    """
    # Lines 81-82: Try to create smaller font
    try:
        # Load same font file at reduced size
        return ImageFont.truetype(font.path, font.size - reduction)
    # Lines 83-84: Return original font if any errors occur
    except:
        # Errors might occur if font is default (no .path attribute)
        return font

# Lines 86-92: Draw centered text with shadow effect
def add_text(draw, text, font, canvas_width, y_pos):
    """
    Draw centered text with a subtle shadow effect.
    
    Text is horizontally centered on the canvas and drawn with
    a 1-pixel dark gray shadow offset for depth.
    
    Args:
        draw (ImageDraw): Drawing context
        text (str): Text to display
        font (ImageFont): Font to use
        canvas_width (int): Canvas width for centering
        y_pos (int): Vertical position (pixels from top)
    """
    # Line 87: Calculate text dimensions (bounding box)
    bbox = draw.textbbox((0,0), text, font=font)
    
    # Line 88: Extract text width from bounding box
    text_width = bbox[2] - bbox[0]  # right - left
    
    # Line 89: Calculate X position to center text
    x_pos = (canvas_width - text_width)//2  # Integer division
    
    # Line 91: Draw shadow (1px offset, dark gray)
    draw.text((x_pos+1, y_pos+1), text, fill="#444", font=font)
    
    # Line 93: Draw main text (black, on top of shadow)
    draw.text((x_pos, y_pos), text, fill="black", font=font)

# Lines 94-104: Add logo to center of QR code
def add_logo(image, logo_path, header_height, qr_size):
    """
    Embed a logo image in the center of the QR code.
    
    Logo is resized to 20% of QR code width and centered.
    Transparency is preserved if logo has alpha channel.
    
    Args:
        image (Image): Final image to modify (modified in-place)
        logo_path (str): Path to logo image file
        header_height (int): Header offset for Y positioning
        qr_size (tuple): QR code dimensions (width, height)
    """
    # Line 95: Start error handling
    try:
        # Line 96: Open logo and convert to RGBA (preserve transparency)
        logo = Image.open(logo_path).convert("RGBA")
        
        # Line 97: Calculate logo size (20% of QR width)
        size = int(qr_size[0]*0.2)
        
        # Line 98: Resize logo maintaining aspect ratio
        logo.thumbnail((size, size))  # Modifies logo in-place
        
        # Line 99: Calculate centered position in QR code area
        pos = ((qr_size[0]-logo.width)//2,  # Center horizontally
               header_height + (qr_size[1]-logo.height)//2)  # Center vertically in QR
        
        # Line 100: Extract transparency mask from alpha channel
        mask = logo.split()[3] if logo.mode=="RGBA" else None
        
        # Line 101: Paste logo onto image with transparency
        image.paste(logo, pos, mask)
        
    # Lines 102-103: Handle errors gracefully (don't crash)
    except Exception as e:
        # Print error but continue (QR code still works without logo)
        print(f"Failed to add logo: {e}")

# Lines 106-108: Generate timestamp-based filename
def generate_filename():
    """
    Generate a unique filename using current timestamp.
    
    Format: qrcode_YYYYMMDD_HHMMSS.png
    Example: qrcode_20231011_143059.png
    
    Returns:
        str: Filename with timestamp
    """
    # Line 107: Create timestamp string (year/month/day_hour/minute/second)
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Line 108: Return formatted filename
    return f"qrcode_{now}.png"
```

---

## 🔬 Technical Details

### QR Code Parameters Explained

**Version (Size):**
- Versions 1-40 (1 = 21×21, 40 = 177×177 modules)
- `None` = Auto-select based on data length
- More data = higher version needed

**Error Correction Levels:**
- **L (Low):** 7% of codewords can be restored
- **M (Medium):** 15% can be restored
- **Q (Quartile):** 25% can be restored
- **H (High):** 30% can be restored ← **We use this**

**Box Size:**
- Pixels per module (black/white square)
- Larger = bigger final image
- 10 is a good balance

**Border:**
- White margin around QR code
- Measured in modules
- QR spec requires minimum of 4

### Image Modes

**RGB:**
- 3 channels: Red, Green, Blue
- 8 bits per channel (0-255)
- 24 bits per pixel total
- No transparency

**RGBA:**
- 4 channels: Red, Green, Blue, Alpha
- Alpha = transparency (0=transparent, 255=opaque)
- 32 bits per pixel
- Used for logos to preserve transparency

### PIL Coordinate System

```
(0,0) ──────────> X (width)
  │
  │
  │
  ↓
  Y (height)
```

- Origin is top-left corner
- X increases rightward
- Y increases downward
- All coordinates are pixels

---

## 🎓 Key Concepts

### 1. Error Handling Philosophy
```python
try:
    # Attempt operation
    risky_operation()
except:
    # Handle gracefully
    return_safe_default()
```
- **Defensive programming**
- **Fail gracefully** rather than crash
- **Log errors** for debugging
- **Return sensible defaults**

### 2. Function Modularity
- Each function has **one clear purpose**
- **Helper functions** keep code clean
- **Reusable** components
- **Easy to test** individually

### 3. Cross-Platform Compatibility
```python
paths = [
    "arial.ttf",  # Mac/Linux
    "C:/Windows/Fonts/arial.ttf"  # Windows
]
```
- Check **multiple locations**
- **Fallback options**
- Works on any OS

### 4. Optional Parameters
```python
def function(required, optional="default"):
```
- **Required first**, optional after
- **Sensible defaults**
- **Flexible usage**

---

## 💡 Best Practices Demonstrated

### ✅ Input Validation
```python
if not data or not isinstance(data, str):
    raise ValueError("Data must be a non-empty string")
```

### ✅ Documentation
```python
"""
Complete docstring with:
- Purpose
- Parameters
- Return values
- Examples
"""
```

### ✅ Error Handling
```python
try:
    operation()
except Exception as e:
    print(f"Error: {e}")
    return None
```

### ✅ Magic Numbers as Variables
```python
header_height = 100  # Named constant
size = int(qr_size[0] * 0.2)  # Calculation with context
```

### ✅ Type Hints (Could be Added)
```python
def generate_qr_with_customizations(
    data: str,
    owner_name: str = "",
    title: str = "",
    logo_path: Optional[str] = None,
    filename: Optional[str] = None
) -> Optional[Tuple[Image.Image, str]]:
```

---

## 🔍 Common Questions

### Q: Why use `//` instead of `/` for division?

**A:** Floor division vs regular division
```python
x = 100 / 2   # Result: 50.0 (float)
y = 100 // 2  # Result: 50 (integer)
```
Pixels must be integers, so we use `//`

### Q: What's the difference between `except:` and `except Exception:`?

**A:**
- `except:` - Catches EVERYTHING (even system exits)
- `except Exception:` - Catches normal errors only (better practice)
- `except ValueError:` - Catches specific error type (most specific)

### Q: Why return a tuple instead of just the image?

**A:** Flexibility
```python
img, path = generate_qr(...)  # Get both
img, _ = generate_qr(...)     # Ignore filename
```

### Q: Could logo_path be a file object instead of string?

**A:** Yes! Could be improved:
```python
if hasattr(logo_path, 'read'):  # File object
    logo = Image.open(logo_path)
else:  # File path string
    logo = Image.open(logo_path)
```

---

## 🚀 Possible Improvements

### 1. Add Type Hints
```python
from typing import Optional, Tuple

def generate_qr_with_customizations(
    data: str,
    owner_name: str = "",
    title: str = "",
    logo_path: Optional[str] = None,
    filename: Optional[str] = None
) -> Optional[Tuple[Image.Image, str]]:
```

### 2. More Specific Error Handling
```python
except FileNotFoundError:
    print("Logo file not found")
except PermissionError:
    print("No permission to read file")
except Exception as e:
    print(f"Unexpected error: {e}")
```

### 3. Configurable Colors
```python
def generate_qr_with_customizations(
    ...,
    qr_color="black",
    background_color="white",
    text_color="black"
):
```

### 4. Custom Font Support
```python
def generate_qr_with_customizations(
    ...,
    font_path=None,
    font_size=28
):
```

### 5. Return Metadata
```python
return {
    'image': final_img,
    'filename': filename,
    'size': final_img.size,
    'qr_version': qr.version,
    'logo_included': logo_path is not None
}
```

---

## 📚 Further Reading

- **QR Code Spec:** https://www.qrcode.com/en/about/standards.html
- **Pillow Documentation:** https://pillow.readthedocs.io/
- **qrcode Library:** https://github.com/lincolnloop/python-qrcode
- **Python Best Practices:** https://pep8.org/

---

**Document Created:** October 2025  
**Module Version:** 1.0.0  
**Author:** [Your Name]

---

**This completes the line-by-line explanation of qrGenerator.py! 🎉**