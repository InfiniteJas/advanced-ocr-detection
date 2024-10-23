# Advanced OCR Text Detection

A Python-based OCR (Optical Character Recognition) solution that combines computer vision techniques with Tesseract OCR to detect and extract text from images. The system supports multiple languages including English, Russian, and Kazakh.

## Features

- Multi-language text detection (English, Russian, Kazakh)
- Advanced image preprocessing for better recognition
- Threaded processing for improved performance
- Text region detection and visualization
- Detailed logging and error handling
- Output results in both visual and text formats

## Prerequisites

- Python 3.8+
- Tesseract OCR engine installed
- OpenCV
- Required Python packages (see requirements.txt)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/InfiniteJas/advanced-ocr-detection.git
cd advanced-ocr-detection
```

2. Install Tesseract OCR:
- Windows: Download and install from [Tesseract GitHub](https://github.com/UB-Mannheim/tesseract/wiki)
- Linux: `sudo apt-get install tesseract-ocr`
- Mac: `brew install tesseract`

3. Install required Python packages:
```bash
pip install -r requirements.txt
```

4. Download required language data for Tesseract:
```bash
# Windows: Copy these files to Tesseract installation directory
# Linux/Mac:
sudo apt-get install tesseract-ocr-rus
sudo apt-get install tesseract-ocr-kaz
```

## Usage

1. Basic usage:
```python
from east_ocr_adv import process_image

# Process a single image
results, processed_image = process_image(
    image_path='path/to/your/image.jpg',
    output_path='path/to/save/output.jpg'
)
```

2. Command line usage (upcoming feature):
```bash
python app.py --input path/to/image.jpg --output path/to/output.jpg
```

## Output

The script produces three types of output:
1. Annotated image with detected text regions (green rectangles)
2. Text file containing extracted text with coordinates
3. Debug binary image for troubleshooting

## Configuration

You can modify the following parameters in the script:
- Tesseract path
- Language settings
- Preprocessing parameters
- Text region detection thresholds

## Project Structure

```
advanced-ocr-detection/
│
├── app.py                # Main script
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── .gitignore           # Git ignore file
├── LICENSE              # License file
│
├── examples/            # Example images and outputs
│   ├── input/
│   └── output/
│
└── tests/              # Test files (upcoming)
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [OpenCV](https://opencv.org/)
- [Python](https://www.python.org/)

---
