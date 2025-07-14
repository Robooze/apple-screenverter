# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python Flask web application that automatically resizes screenshots to Apple App Store Connect specifications. The tool helps developers avoid App Store rejections due to incorrect screenshot dimensions.

## Development Setup

```bash
# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

The application runs on `http://localhost:5001`.

## Architecture

### Backend Structure
- **app.py**: Flask application with three main routes:
  - `/` - Serves the main application page
  - `/upload` - Handles file processing and returns results
  - `/download/<filename>` - Serves processed images
- **utils/image_processor.py**: Core image processing logic using Pillow
- **utils/apple_specs.py**: Centralized Apple device specifications

### Frontend Architecture
- Single-page application using HTMX for dynamic updates
- Alpine.js for client-side interactivity
- Tailwind CSS for styling (loaded via CDN)
- No build process - all assets embedded in templates/index.html

### Image Processing Workflow
1. File upload validation (PNG/JPG/JPEG, max 16MB)
2. Image analysis to determine closest Apple App Store specification
3. Center-crop resizing using Pillow's ImageOps.fit()
4. Processed file saved to `processed/` directory
5. Download link provided to user

## Key Technical Concepts

### Device Specifications
Apple App Store Connect requires specific dimensions for different device types. The application:
- Maintains specifications in `utils/apple_specs.py`
- Supports iPhone models from iPhone XR to iPhone 16 Pro Max
- Automatically selects closest matching specification based on aspect ratio

### Image Processing Logic
- Uses Pillow (PIL) for image manipulation
- Implements center-crop resizing to maintain aspect ratio
- Preserves image quality while meeting exact pixel requirements
- Handles various input formats and converts to appropriate output

## Development Guidelines

### Code Organization
- Keep Flask routes simple and focused
- Separate business logic into utils/ modules
- Maintain clear separation between image processing and web handling
- Use descriptive variable names for image dimensions and specifications

### Testing Approach
- Manual testing with real App Store Connect screenshots
- Validate against actual App Store submission requirements
- Test edge cases: very wide/tall images, minimum/maximum sizes
- Verify processed images meet exact pixel specifications

### Adding New Device Support
1. Research Apple's official screenshot specifications
2. Add new device entry to `APPLE_SPECS` in `utils/apple_specs.py`
3. Test with real screenshots from that device
4. Update frontend device list if needed

## Common Development Tasks

### Debugging Image Processing
- Check image dimensions before/after processing
- Verify aspect ratio calculations
- Test with various image formats and sizes
- Use Pillow's image.info for debugging metadata

### Frontend Updates
- Modify templates/index.html for UI changes
- HTMX attributes control dynamic behavior
- Alpine.js handles client-side state management
- No build process required - changes are immediate

### Performance Considerations
- File uploads are limited to 16MB
- Images are processed synchronously
- Temporary files are stored in uploads/ and processed/ directories
- Consider cleanup of old processed files for production use

## Technology Stack Notes

- **Flask 2.3.3**: Web framework with development server
- **Pillow 10.0.1**: Image processing library
- **HTMX**: Dynamic HTML updates without JavaScript
- **Alpine.js**: Lightweight JavaScript framework
- **Tailwind CSS**: Utility-first CSS framework
- **python-multipart**: File upload handling

## File Structure Context

```
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── templates/index.html   # Single-page application UI
├── utils/
│   ├── apple_specs.py     # Device specifications
│   └── image_processor.py # Image processing logic
├── uploads/              # Temporary upload storage
├── processed/            # Processed image output
└── venv/                # Python virtual environment
```

## Educational Approach

When working with this codebase, focus on:
- Understanding the relationship between image dimensions and App Store requirements
- Learning how Pillow handles image manipulation
- Grasping the Flask request/response cycle
- Exploring how HTMX creates dynamic web experiences without complex JavaScript

Always explain the reasoning behind image processing decisions and help build understanding of web application architecture patterns.