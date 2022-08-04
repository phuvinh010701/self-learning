from google.cloud import vision
import io
import os
from docx import Document

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "capable-gasket-351808-34da05d096c1.json"

def process_string(block_text):
    # print(block_text[0])
    if block_text[0][0].islower():
        block_text[0] = " " + block_text[0]
    else:
        block_text[0] = "\t" + block_text[0]
    
    for i in range(1, len(block_text)):
        block_text[i] = "\t" + block_text[i]
    
    text = '\n'.join(block_text)
    return text
       
client = vision.ImageAnnotatorClient()    
def detect_text(path):
    """Detects text in the file."""
    
    # client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)

    response = client.document_text_detection(image=image)

    for page in response.full_text_annotation.pages:
        for block in page.blocks:

            block_text = []
            for paragraph in block.paragraphs:
                
                paragraph_text = []
                for word in paragraph.words:
                    word_text = ''.join([
                        symbol.text for symbol in word.symbols
                    ])
                    paragraph_text.append(word_text)
                block_text.append(' '.join(paragraph_text))
            print(block_text)
            with open('result.txt', mode='a', encoding='utf-8') as f:
                f.write(process_string(block_text))
            f.close()
          
path_folder = "target3/"
file_name = os.listdir(path_folder)
for name in file_name:
    detect_text(path_folder + name)
