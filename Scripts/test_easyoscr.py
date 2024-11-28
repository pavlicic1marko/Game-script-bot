import easyocr

from Scripts.logging_commands import log_info

# Create an OCR reader object
reader = easyocr.Reader(['en'])

# Read text from an image
result = reader.readtext(' screenshot.png')

# Print the extracted text
for detection in result:
    print(detection[1])
    log_info(detection[1])