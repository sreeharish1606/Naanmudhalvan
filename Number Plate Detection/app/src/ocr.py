import easyocr

reader = easyocr.Reader(['en'])

def extract_text(image):
    result = reader.readtext(image)
    return " ".join([text for _, text, _ in result])
