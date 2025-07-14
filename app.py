from flask import Flask, request, render_template, send_file, jsonify, redirect, url_for
import os
import uuid
from datetime import datetime
from werkzeug.utils import secure_filename
from utils.image_processor import ScreenshotProcessor

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['PROCESSED_FOLDER'] = 'processed'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Create directories if they don't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['PROCESSED_FOLDER'], exist_ok=True)

processor = ScreenshotProcessor()

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        if 'file' not in request.files:
            return '''
                <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
                    <strong>Error:</strong> No file was selected.
                </div>
            ''', 400
        
        file = request.files['file']
        
        if file.filename == '':
            return '''
                <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
                    <strong>Error:</strong> No file was selected.
                </div>
            ''', 400
        
        if not allowed_file(file.filename):
            return '''
                <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
                    <strong>Error:</strong> Please upload a PNG or JPG file.
                </div>
            ''', 400
        
        # Generate unique filename
        unique_id = str(uuid.uuid4())
        filename = secure_filename(file.filename)
        file_extension = filename.rsplit('.', 1)[1].lower()
        
        input_filename = f"{unique_id}.{file_extension}"
        output_filename = f"{unique_id}_resized.png"
        
        input_path = os.path.join(app.config['UPLOAD_FOLDER'], input_filename)
        output_path = os.path.join(app.config['PROCESSED_FOLDER'], output_filename)
        
        # Save uploaded file
        file.save(input_path)
        
        # Process the screenshot
        result = processor.process_screenshot(input_path, output_path)
        
        # Clean up input file
        os.remove(input_path)
        
        if result['success']:
            return f'''
                <div class="bg-green-100 border border-green-400 text-green-700 px-4 py-3 rounded mb-4">
                    <strong>Success!</strong> Screenshot processed successfully.
                </div>
                <div class="bg-white rounded-lg shadow-md p-6 mb-4">
                    <h3 class="text-lg font-semibold mb-4">Processing Results</h3>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
                        <div>
                            <p class="text-sm text-gray-600">Original Size:</p>
                            <p class="font-medium">{result['original_dimensions'][0]} × {result['original_dimensions'][1]} pixels</p>
                        </div>
                        <div>
                            <p class="text-sm text-gray-600">Resized To:</p>
                            <p class="font-medium">{result['target_dimensions'][0]} × {result['target_dimensions'][1]} pixels</p>
                        </div>
                        <div>
                            <p class="text-sm text-gray-600">Target Device:</p>
                            <p class="font-medium">{result['device_name']}</p>
                        </div>
                        <div>
                            <p class="text-sm text-gray-600">Orientation:</p>
                            <p class="font-medium capitalize">{result['orientation']}</p>
                        </div>
                    </div>
                    <div class="text-center">
                        <a href="/download/{output_filename}" 
                           class="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded inline-flex items-center">
                            <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path>
                            </svg>
                            Download Resized Screenshot
                        </a>
                    </div>
                </div>
            '''
        else:
            return f'''
                <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
                    <strong>Error:</strong> {result['error']}
                </div>
            ''', 500
            
    except Exception as e:
        return f'''
            <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
                <strong>Error:</strong> {str(e)}
            </div>
        ''', 500


@app.route('/download/<filename>')
def download_file(filename):
    try:
        file_path = os.path.join(app.config['PROCESSED_FOLDER'], filename)
        if os.path.exists(file_path):
            return send_file(file_path, as_attachment=True, download_name=f'app-store-screenshot-{filename}')
        else:
            return "File not found", 404
    except Exception as e:
        return f"Error downloading file: {str(e)}", 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)