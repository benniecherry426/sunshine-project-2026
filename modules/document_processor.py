# Document Processor

This module provides functionalities for processing PDFs, images, and documents.

## Features
- **PDF Processing:** Extract text and metadata from PDF files.
- **Image Processing:** Convert images between formats and perform basic operations.
- **Document Processing:** Handle different document formats and convert to consistent types.

## Usage

### PDF Processing
```python
from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ''
    for page in reader.pages:
        text += page.extract_text() + '\n'
    return text
```

### Image Processing
```python
from PIL import Image

def convert_image(input_image_path, output_image_path, output_format='JPEG'):
    with Image.open(input_image_path) as img:
        img.convert('RGB').save(output_image_path, format=output_format)
```

### Document Processing
```python
def read_document(doc_path):
    with open(doc_path, 'r') as file:
        return file.read()
```