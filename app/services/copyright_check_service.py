
# The service will only help you to detect any watermark, logo, text with copyright symbol present
# in the image. It will not remove the watermark or logo from the image.
import cv2
import easyocr
import numpy as np
import requests
import difflib

from app.utils.copyright_utils import restricted_keywords

reader = easyocr.Reader(['en'])

class CopyrightCheckerService:
   @staticmethod
   def detect_copyrighted_text(image_path):
       # load image
      
       response = requests.get(image_path)
       response.raise_for_status() 

       if not response.content:
        raise ValueError("Image download failed: response content is empty")

       img_array = np.array(bytearray(response.content), dtype=np.uint8) # to convert raw data into existing array
       image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

       if image is None:
          raise ValueError("Failed to decode image")
       # convert image to grayscale
        # Preprocess image: grayscale + thresholding
       gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
       _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
       #Improve text detection
       gray = cv2.GaussianBlur(gray, (3,3), 0)

       
       # perform OCR on the image
       
       # data = pytesseract.image_to_data(gray, output_type=Output.DICT)
       data = reader.readtext(gray)

       # Define some predefine keyword and try to find the match
       detected_keywords = []
       full_text =[]
       for (bbox, text, prob) in data:
         full_text.append(text)
         for keyword in restricted_keywords:
            #print(keyword.lower())
            #print(text.lower())
            similarity = difflib.SequenceMatcher(None, keyword.lower(), text.lower()).ratio()
            if similarity > 0.8:  # 80% similar — tweak this if needed
              detected_keywords.append({
                "text": text,
                "confidence": prob,
                # "bbox": bbox
               })
            # Draw rectangle around detected text
            top_left = tuple(map(int, bbox[0]))
            bottom_right = tuple(map(int, bbox[2]))
            cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)

       
       if detected_keywords:
            return {
                "copyrighted_content": detected_keywords,
                "copyright_found": True,
                "extracted_text": " ".join(full_text) # Now it also returns the information extracted from the image
            }
       else:
            return {
                "detected_keywords": [],
                "copyright_found": False,
                "extracted_text": " ".join(full_text) # Now it also returns the information extracted from the image
            }
       
    