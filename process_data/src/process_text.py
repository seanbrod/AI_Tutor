#Use tesseract OCR to create layout breakdown of articles, papers, etc. 
from pdf2image import convert_from_path
import os
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\Andrew\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'
OUTPUT_FOLDER = 'process_data\\data_text\\pages_temp'

#convert PDF of proposal to jpg
def convertPDF_to_JPG(pdfName):
    FILE_PATH = "process_data\\data_text\\{}".format(pdfName)
    global OUTPUT_FOLDER

    pages = convert_from_path(FILE_PATH, fmt='jpeg', output_file='page', paths_only=True, output_folder=OUTPUT_FOLDER)

#make tsv file from running tesseract on jpgs
def ocrTesseract():
    dir = "process_data\\data_text\\pages_temp" 
    text_store = []
    for filename in os.listdir(dir):
        try:
            file_path = dir + "\\"+filename
            image = Image.open(file_path)
            text = pytesseract.image_to_string(image, config="--psm 6")
            text_store.append(text)
        except Exception as e:
            print("Error:", e)
    return text_store

def main():

    fileName = input("Enter filename: ")
    output_path = "process_data\\output_text\\"
    convertPDF_to_JPG(fileName)
    ocr_proposal = ocrTesseract()
    with open(output_path + fileName[:-3] + "txt", "w") as f:
        for item in ocr_proposal:
            f.write(str(item)+"\n")
    print("complete")

if __name__=="__main__":
    main()