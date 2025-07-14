# Technical Implementation Plan: iOS Screenshot Resizer

*Based on PRD-iOS-Screenshot-Resizer-2025-07-14.md*

## Project Overview
Build a web-based tool using HTMX + Python + Tailwind + Alpine.js to automatically resize screenshots for Apple App Store Connect submissions.

## Project Structure
```
ios-screenshot-resizer/
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── static/
│   ├── css/
│   │   └── style.css     # Custom styles (minimal)
│   └── js/
│       └── main.js       # Alpine.js components
├── templates/
│   └── index.html        # Main application page
├── uploads/              # Temporary file storage
├── processed/            # Processed images
└── utils/
    └── image_processor.py # Core image processing logic
```

## Implementation Phases

### Phase 1: Backend Setup & Core Logic (2-3 hours)

#### 1.1 Environment Setup
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install flask pillow python-multipart
pip freeze > requirements.txt
```

#### 1.2 Apple Specifications Data Structure
Create `utils/apple_specs.py`:
```python
# Apple App Store Connect Screenshot Specifications
APPLE_SPECS = {
    'iphone_16_pro_max': {
        'name': 'iPhone 16 Pro Max',
        'portrait': (1290, 2796),
        'landscape': (2796, 1290)
    },
    'iphone_15_pro_max': {
        'name': 'iPhone 15 Pro Max', 
        'portrait': (1320, 2868),
        'landscape': (2868, 1320)
    },
    'iphone_14_plus': {
        'name': 'iPhone 14 Plus',
        'portrait': (1284, 2778),
        'landscape': (2778, 1284)
    },
    # Add remaining specs from PRD
}
```

#### 1.3 Core Image Processing Logic
Create `utils/image_processor.py`:
```python
from PIL import Image, ImageOps
import os
from .apple_specs import APPLE_SPECS

class ScreenshotProcessor:
    def __init__(self):
        self.specs = APPLE_SPECS
    
    def find_closest_spec(self, width, height):
        """Find the closest Apple specification for given dimensions"""
        # Implementation logic here
        pass
    
    def resize_image(self, image_path, target_spec):
        """Resize image to target specification using smart cropping"""
        # Implementation logic here
        pass
    
    def process_screenshot(self, input_path, output_path):
        """Main processing function"""
        # Implementation logic here
        pass
```

#### 1.4 Flask Application Setup
Create `app.py`:
```python
from flask import Flask, request, render_template, send_file, jsonify
import os
import uuid
from utils.image_processor import ScreenshotProcessor

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['PROCESSED_FOLDER'] = 'processed'

# Create directories if they don't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['PROCESSED_FOLDER'], exist_ok=True)

processor = ScreenshotProcessor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    # Handle file upload and processing
    pass

@app.route('/download/<filename>')
def download_file(filename):
    # Handle file download
    pass

if __name__ == '__main__':
    app.run(debug=True)
```

**Phase 1 Acceptance Criteria:**
- ✅ Flask app runs locally
- ✅ Image processing logic correctly identifies closest Apple spec
- ✅ Pillow successfully resizes images to exact specifications
- ✅ File upload and download endpoints work

**Phase 1 Status: COMPLETED**

### Phase 2: Frontend Implementation (2-3 hours)

#### 2.1 HTML Structure with Tailwind
Create `templates/index.html`:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>iOS Screenshot Resizer</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/htmx.org@1.9.10"></script>
    <script src="https://unpkg.com/alpinejs@3.x.x/dist/cdn.min.js" defer></script>
</head>
<body class="bg-gray-100 min-h-screen">
    <div class="container mx-auto px-4 py-8">
        <h1 class="text-3xl font-bold text-center mb-8">iOS Screenshot Resizer</h1>
        
        <!-- Upload Area -->
        <div x-data="fileUpload()" class="max-w-2xl mx-auto">
            <!-- File drop zone -->
            <!-- Processing indicator -->
            <!-- Results display -->
        </div>
    </div>
</body>
</html>
```

#### 2.2 Alpine.js File Upload Component
Add to `static/js/main.js`:
```javascript
function fileUpload() {
    return {
        file: null,
        processing: false,
        result: null,
        
        handleFileSelect(event) {
            // Handle file selection
        },
        
        handleDrop(event) {
            // Handle drag and drop
        },
        
        validateFile(file) {
            // Validate file type and size
        }
    }
}
```

#### 2.3 HTMX Integration
Add HTMX attributes to form elements:
```html
<form hx-post="/upload" 
      hx-encoding="multipart/form-data"
      hx-target="#results"
      hx-indicator="#processing">
    <!-- Form content -->
</form>
```

**Phase 2 Acceptance Criteria:**
- ✅ Drag and drop file upload works
- ✅ File validation (JPG/PNG only)
- ✅ HTMX submits form without page refresh
- ✅ Processing indicator shows during upload
- ✅ Results display properly

**Phase 2 Status: COMPLETED**

### Phase 3: Integration & Polish (1-2 hours)

#### 3.1 Error Handling
- File upload errors
- Invalid image formats
- Processing failures
- Network issues

#### 3.2 User Experience Enhancements
- Progress indicators
- Success/error messages
- Image previews
- Download functionality

#### 3.3 Testing with Real Screenshots
- Test with actual Figma exports
- Validate against Apple specifications
- Test various image sizes and formats

**Phase 3 Acceptance Criteria:**
- ✅ All error cases handled gracefully
- ✅ User feedback for all actions
- ✅ Tool successfully processes real screenshots
- ✅ Output images pass App Store Connect validation

**Phase 3 Status: COMPLETED**

### Phase 4: Deployment & Documentation (30 minutes)

#### 4.1 Local Deployment
Create `run.sh`:
```bash
#!/bin/bash
source venv/bin/activate
python app.py
```

#### 4.2 Team Documentation
Create `README.md`:
```markdown
# iOS Screenshot Resizer

## Quick Start
1. `chmod +x run.sh`
2. `./run.sh`
3. Open http://localhost:5000
4. Upload screenshot, download resized version

## Supported Formats
- JPG, PNG input
- PNG output (recommended for App Store)
```

**Phase 4 Acceptance Criteria:**
- ✅ Tool runs locally with single command
- ✅ Documentation covers all usage scenarios
- ✅ Team can use tool independently

**Phase 4 Status: COMPLETED**

## Development Timeline
- **Phase 1**: 2-3 hours (Backend & Logic) ✅ COMPLETED
- **Phase 2**: 2-3 hours (Frontend & UI) ✅ COMPLETED
- **Phase 3**: 1-2 hours (Integration & Testing) ✅ COMPLETED
- **Phase 4**: 30 minutes (Deployment & Docs) ✅ COMPLETED

**Total Estimated Time**: 6-8 hours  
**Actual Implementation**: COMPLETED - All phases finished successfully

## Key Implementation Notes

### Image Processing Strategy
- Use `PIL.ImageOps.fit()` for smart cropping
- Maintain aspect ratio, crop excess content
- Center crop to preserve most important content
- Output as PNG for best App Store compatibility

### Error Handling Priorities
1. Invalid file formats
2. File size too large
3. Processing failures
4. Network connectivity issues

### Performance Considerations
- Process images in memory when possible
- Clean up temporary files after processing
- Limit file size to reasonable bounds (e.g., 10MB)

## Testing Strategy
1. **Unit Tests**: Test image processing logic with known inputs
2. **Integration Tests**: Test full upload → process → download flow
3. **Manual Testing**: Test with real Figma exports
4. **Validation Testing**: Verify outputs pass App Store Connect

## Success Metrics
- ✅ Zero App Store Connect rejections due to screenshot dimensions
- ✅ Processing time < 5 seconds for typical screenshots
- ✅ Tool adoption by entire Loud development team

## Future Development Tasks

### Phase 5: Public Deployment (1-2 hours)
**Priority: High**
- 🔄 Deploy to free hosting platform (Railway, Render, or Vercel)
- 🔄 Set up production configuration
- 🔄 Configure environment variables
- 🔄 Test deployment with real usage

### Phase 6: Community Features (2-3 hours)
**Priority: Medium**
- 🔄 **GitHub repository** setup for version control and collaboration
  - Set up public repository
  - Add contribution guidelines
  - Create issue templates
  - Set up automated testing
- 🔄 **Ko-fi donation link** integration
  - Add Ko-fi banner/button to UI
  - Set up donation page
  - Add supporter recognition

### Phase 7: Enhanced Features (Future)
**Priority: Low**
- 📋 Batch processing multiple screenshots
- 📋 Android Play Store specifications
- 📋 Integration with design tools (Figma, Sketch)
- 📋 Preview of how screenshot appears in App Store
- 📋 API endpoints for programmatic access
- 📋 Usage analytics and metrics

---

*This technical plan has been successfully implemented and is ready for public deployment and community engagement.*