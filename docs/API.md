# API Documentation

## Base URL
- **Local Development:** `http://localhost:5000`
- **Production:** `https://your-domain.com`

---

## Endpoints

### 1. GET `/`
**Description:** Serves the frontend application

**Response:**
- Returns `index.html` file

**Example:**
```bash
curl http://localhost:5000/
```

---

### 2. POST `/generate-qr`
**Description:** Generates a QR code with optional customizations

#### Request

**Content-Type:** `multipart/form-data`

**Form Fields:**

| Field | Type | Required | Max Length | Description |
|-------|------|----------|------------|-------------|
| `content` | string | ✅ Yes | 2000 chars | Text or URL to encode |
| `owner` | string | ❌ No | 100 chars | Owner name displayed above QR |
| `title` | string | ❌ No | 100 chars | Title displayed above QR |
| `logo` | file | ❌ No | 5MB | Logo image (PNG, JPG, WebP) |

**Example Request (JavaScript):**
```javascript
const formData = new FormData();
formData.append('content', 'https://example.com');
formData.append('owner', 'John Doe');
formData.append('title', 'My Website');
formData.append('logo', logoFile); // File object

const response = await fetch('http://localhost:5000/generate-qr', {
  method: 'POST',
  body: formData
});

const data = await response.json();
```

**Example Request (cURL):**
```bash
curl -X POST http://localhost:5000/generate-qr \
  -F "content=https://example.com" \
  -F "owner=John Doe" \
  -F "title=My Website" \
  -F "logo=@/path/to/logo.png"
```

**Example Request (Python):**
```python
import requests

files = {'logo': open('logo.png', 'rb')}
data = {
    'content': 'https://example.com',
    'owner': 'John Doe',
    'title': 'My Website'
}

response = requests.post(
    'http://localhost:5000/generate-qr',
    files=files,
    data=data
)

print(response.json())
```

#### Response

**Success Response (200 OK):**
```json
{
  "success": true,
  "image_url": "/static/qrcodes/a1b2c3d4e5f6.png"
}
```

**Error Response (200 OK with error):**
```json
{
  "success": false,
  "error": "Content cannot be empty"
}
```

**Response Fields:**

| Field | Type | Description |
|-------|------|-------------|
| `success` | boolean | Whether QR generation succeeded |
| `image_url` | string | Relative URL to generated QR code (only if success=true) |
| `error` | string | Error message (only if success=false) |

#### Status Codes

| Code | Meaning |
|------|---------|
| 200 | Request processed (check `success` field) |
| 500 | Server error (exception occurred) |

---

### 3. GET `/static/qrcodes/<filename>`
**Description:** Serves generated QR code images

**Parameters:**
- `filename` (string, required): Name of the QR code image file

**Response:**
- Returns PNG image file

**Example:**
```bash
curl http://localhost:5000/static/qrcodes/a1b2c3d4e5f6.png --output qrcode.png
```

**Browser Access:**
```
http://localhost:5000/static/qrcodes/a1b2c3d4e5f6.png
```

---

## Error Handling

### Common Error Messages

| Error Message | Cause | Solution |
|---------------|-------|----------|
| `Content cannot be empty` | No content provided | Provide content in the request |
| `Failed to generate QR code` | QR generation failed | Check logs for details |
| `File too large` | Logo exceeds 5MB | Use smaller image file |
| `Invalid file type` | Logo not PNG/JPG/WebP | Use supported image format |

### Error Response Format

All errors return JSON with this structure:
```json
{
  "success": false,
  "error": "Descriptive error message"
}
```

---

## Validation Rules

### Content Field
- ✅ Required
- ✅ Must not be empty or whitespace only
- ✅ Maximum 2000 characters
- ✅ Any text or URL format accepted

### Owner Field
- ❌ Optional
- ✅ Maximum 100 characters
- ✅ Rendered above QR code

### Title Field
- ❌ Optional
- ✅ Maximum 100 characters
- ✅ Rendered above QR code below owner

### Logo File
- ❌ Optional
- ✅ Must be PNG, JPG, JPEG, or WebP
- ✅ Maximum 5MB file size
- ✅ Will be resized to 20% of QR code size
- ✅ Centered on QR code with transparency support

---

## Rate Limiting

**Current:** No rate limiting implemented

**Recommended for Production:**
- 10 requests per minute per IP address
- 100 requests per hour per IP address
- Implement using Flask-Limiter or nginx

**Example Implementation:**
```python
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["100 per hour", "10 per minute"]
)
```

---

## CORS Configuration

**Current Settings:**
```python
CORS(app)  # Allows all origins
```

**Production Recommendation:**
```python
CORS(app, resources={
    r"/generate-qr": {
        "origins": ["https://yourdomain.com"],
        "methods": ["POST"],
        "allow_headers": ["Content-Type"]
    }
})
```

---

## Authentication

**Current:** No authentication required

**Recommended for Production:**
- API key authentication
- JWT tokens
- OAuth 2.0

**Example with API Key:**
```python
@app.before_request
def check_api_key():
    if request.endpoint == 'generate_qr':
        api_key = request.headers.get('X-API-Key')
        if not api_key or api_key != os.getenv('API_KEY'):
            return jsonify({'error': 'Invalid API key'}), 401
```

**Usage:**
```bash
curl -X POST http://localhost:5000/generate-qr \
  -H "X-API-Key: your-secret-key" \
  -F "content=https://example.com"
```

---

## Performance

### Response Times (Typical)
- Simple QR (text only): ~100-200ms
- QR with text customizations: ~150-250ms
- QR with logo: ~200-400ms

### Optimization Tips
1. Use smaller logo images
2. Implement caching for repeated requests
3. Use async workers for batch processing
4. Enable gzip compression

---

## Code Examples

### JavaScript (Fetch API)
```javascript
async function generateQR(content, owner = '', title = '', logoFile = null) {
  const formData = new FormData();
  formData.append('content', content);
  if (owner) formData.append('owner', owner);
  if (title) formData.append('title', title);
  if (logoFile) formData.append('logo', logoFile);

  try {
    const response = await fetch('http://localhost:5000/generate-qr', {
      method: 'POST',
      body: formData
    });
    
    const data = await response.json();
    
    if (data.success) {
      console.log('QR Code URL:', data.image_url);
      return data.image_url;
    } else {
      console.error('Error:', data.error);
      return null;
    }
  } catch (error) {
    console.error('Network error:', error);
    return null;
  }
}

// Usage
const url = await generateQR('https://example.com', 'John Doe', 'My Site');
```

### Python (Requests)
```python
import requests

def generate_qr(content, owner='', title='', logo_path=None):
    url = 'http://localhost:5000/generate-qr'
    
    data = {
        'content': content,
        'owner': owner,
        'title': title
    }
    
    files = {}
    if logo_path:
        files['logo'] = open(logo_path, 'rb')
    
    try:
        response = requests.post(url, data=data, files=files)
        result = response.json()
        
        if result.get('success'):
            return result.get('image_url')
        else:
            print(f"Error: {result.get('error')}")
            return None
    except Exception as e:
        print(f"Request failed: {e}")
        return None
    finally:
        if files:
            files['logo'].close()

# Usage
image_url = generate_qr('https://example.com', 'John Doe', 'My Site', 'logo.png')
```

### cURL
```bash
# Simple QR code
curl -X POST http://localhost:5000/generate-qr \
  -F "content=https://example.com"

# QR with all options
curl -X POST http://localhost:5000/generate-qr \
  -F "content=https://example.com" \
  -F "owner=John Doe" \
  -F "title=My Website" \
  -F "logo=@logo.png" \
  | jq .

# Download generated QR code
curl -X POST http://localhost:5000/generate-qr \
  -F "content=https://example.com" \
  | jq -r '.image_url' \
  | xargs -I {} curl http://localhost:5000{} -o qrcode.png
```

---

## Testing

### Unit Tests
```python
import unittest
from app import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
    
    def test_generate_qr_success(self):
        response = self.client.post('/generate-qr', data={
            'content': 'https://example.com'
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertTrue(data['success'])
        self.assertIn('image_url', data)
    
    def test_generate_qr_empty_content(self):
        response = self.client.post('/generate-qr', data={
            'content': ''
        })
        data = response.get_json()
        self.assertFalse(data['success'])
        self.assertIn('error', data)
```

### Integration Tests
```bash
# Test with httpie
http POST localhost:5000/generate-qr content="https://example.com"

# Test with wget
wget --post-data "content=https://example.com" \
  http://localhost:5000/generate-qr -O response.json
```

---

## Changelog

### v1.0.0 (Current)
- Initial API release
- POST /generate-qr endpoint
- Support for content, owner, title, logo
- JSON responses
- CORS enabled

---

## Support

For issues or questions:
- Check TROUBLESHOOTING.md
- Review error messages in console
- Check server logs
- Open an issue on GitHub

---

**Last Updated:** October 2025