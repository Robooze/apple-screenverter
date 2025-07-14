# PRD: iOS Screenshot Resizer Tool

## Overview
Internal tool to automatically resize screenshots to Apple App Store Connect specifications, eliminating manual resizing work and submission rejections.

## Problem Statement
- App Store Connect rejects screenshots that don't match exact pixel dimensions
- Manual resizing is time-consuming and error-prone
- Current Figma exports don't align with Apple's specific requirements
- Blocking in-app purchase submissions due to "missing metadata" errors

## Target Users
- Loud development team
- Anyone submitting screenshots to App Store Connect

## Core Functionality

### Input
- Single screenshot upload (JPG or PNG)
- Drag-and-drop or file picker interface

### Processing
- Analyze input image dimensions
- Find closest matching Apple specification from approved sizes:
  - iPhone 16 Pro Max: 1290x2796 (portrait) / 2796x1290 (landscape)
  - iPhone 15 Pro Max: 1320x2868 (portrait) / 2868x1320 (landscape)
  - iPhone 14 Plus: 1284x2778 (portrait) / 2778x1284 (landscape)
  - [All other iPhone specs as per Apple documentation]

### Output
- Resized screenshot matching exact Apple specifications
- Download as PNG (recommended for App Store Connect)
- Display which iPhone model specification was used

## Technical Requirements

### Platform
- Web application (accessible to entire team)
- Simple, single-page interface

### Technology Stack
- **Frontend**: HTMX + Tailwind CSS + Alpine.js (or Hyperscript)
- **Backend**: Python (Flask or FastAPI)
- **Image Processing**: Pillow (PIL) for Python
- **Hosting**: Can be hosted locally or on internal server
- **File Upload**: HTML5 file upload with HTMX for seamless UX

### Resizing Strategy
- **Crop to fit**: Maintain aspect ratio, crop excess content
- **Center crop**: Keep most important content in center
- **Preserve quality**: Use Pillow's high-quality resizing algorithms
- **Smart cropping**: Pillow's `ImageOps.fit()` with centering

## User Experience

### Interface
1. Upload area with drag-and-drop (Alpine.js for file handling)
2. Preview of original image with dimensions
3. HTMX-powered processing (no page refresh)
4. Preview of resized image with target specifications
5. Download button for processed image

### Workflow
1. User uploads screenshot (Alpine.js handles file selection)
2. HTMX sends file to Python backend
3. Python/Pillow analyzes dimensions and resizes
4. HTMX updates page with results (no refresh)
5. User downloads properly sized screenshot
6. User uploads to App Store Connect (success!)

## Success Metrics
- Zero screenshot rejections due to dimension issues
- Reduced time from design to App Store submission
- Team adoption and regular usage

## Technical Considerations
- Handle both portrait and landscape orientations
- Maintain image quality during resizing with Pillow
- Support common image formats (JPG, PNG) via Pillow
- Fast processing (< 5 seconds for typical screenshots)
- HTMX for smooth, no-refresh user experience
- Alpine.js for client-side file validation and UI interactions
- Tailwind for rapid, responsive styling

## Future Enhancements (Not Required for MVP)
- Batch processing multiple screenshots
- Android Play Store specifications
- Integration with design tools
- Preview of how screenshot appears in App Store

## Acceptance Criteria
- ✅ Accepts JPG and PNG files
- ✅ Automatically detects closest Apple specification
- ✅ Outputs properly sized screenshot
- ✅ Processed images pass App Store Connect validation
- ✅ Simple, intuitive interface requiring no training

## Implementation Status
**COMPLETED** - All core functionality implemented and working.

### What's Been Built
- ✅ **Flask web application** with Python backend
- ✅ **Modern minimalist UI** with Tailwind CSS, HTMX, and Alpine.js
- ✅ **Drag-and-drop file upload** with visual feedback
- ✅ **Smart image processing** using Pillow with center-crop resizing
- ✅ **Apple device specifications** for iPhone XR through iPhone 16 Pro Max
- ✅ **Real-time processing** with HTMX (no page refreshes)
- ✅ **Responsive design** optimized for readability
- ✅ **File validation** (16MB limit, PNG/JPG formats)
- ✅ **Download functionality** for processed screenshots

### Current Capabilities
- Supports all modern iPhone models (XR to 16 Pro Max)
- Automatically selects closest matching Apple specification
- Center-crop resizing maintains image quality
- Clean, professional interface suitable for developer use
- Works locally for immediate team use

## Future Enhancements
- 🔄 **Deployment** to free hosting platform (Railway, Render, or Vercel)
- 🔄 **GitHub repository** setup for version control and collaboration
- 🔄 **Ko-fi donation link** for community support
- 📋 Batch processing multiple screenshots
- 📋 Android Play Store specifications
- 📋 Integration with design tools
- 📋 Preview of how screenshot appears in App Store

## Development Priority
**COMPLETED** - Tool is ready for immediate use and deployment.

---

*This tool successfully solves the App Store Connect screenshot submission issue and is ready for team use.*