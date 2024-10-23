"""
Unit tests for OCR Processor module
"""

import unittest
import numpy as np
from unittest.mock import patch, MagicMock
from pathlib import Path
from ocr_processor import OCRProcessor, OCRConfig, ImageProcessingConfig

class TestOCRProcessor(unittest.TestCase):
    def setUp(self):
        """Set up test cases"""
        self.ocr_config = OCRConfig(
            tesseract_cmd='mock_tesseract_path',
            debug_mode=True
        )
        self.img_config = ImageProcessingConfig()
        self.processor = OCRProcessor(self.ocr_config, self.img_config)
        
        # Create mock image
        self.mock_image = np.zeros((100, 100, 3), dtype=np.uint8)
        self.mock_binary = np.zeros((100, 100), dtype=np.uint8)
    
    @patch('cv2.imread')
    def test_load_image(self, mock_imread):
        """Test image loading"""
        mock_imread.return_value = self.mock_image
        result = self.processor.load_image('test.jpg')
        self.assertIsNotNone(result)
        mock_imread.assert_called_once()
        
    def test_preprocess_image(self):
        """Test image preprocessing"""
        result = self.processor.preprocess_image(self.mock_image)
        self.assertEqual(result.shape[:2], self.mock_image.shape[:2])
    
    def test_detect_text_regions(self):
        """Test text region detection"""
        # Create a mock binary image with a rectangle
        binary = np.zeros((100, 100), dtype=np.uint8)
        binary[20:40, 20:60] = 255
        
        regions = self.processor.detect_text_regions(binary)
        self.assertTrue(len(regions) > 0)
    
    @patch('pytesseract.image_to_string')
    def test_ocr_on_box(self, mock_image_to_string):
        """Test OCR on image region"""
        mock_image_to_string.return_value = "test text"
        result = self.processor._ocr_on_box((self.mock_image, (0, 0, 50, 50)))
        self.assertIsNotNone(result)
        self.assertEqual(result[1], "test text")

if __name__ == '__main__':
    unittest.main()
