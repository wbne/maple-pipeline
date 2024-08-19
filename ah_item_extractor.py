import cv2
import glob
import numpy as np
import pytesseract
import re
import csv

# Here we're hard coding since we know the height is gonna be 1100 pixels
# Usually there should be 50px of padding on the tip and bottom
def page_to_item():
    images = [cv2.imread(file) for file in glob.glob("./images/*.png")]
    top_buffer = -50
    bottom_buffer = 50
    right_buffer = -55
    left_buffer = 150
    item_size = 111
    counter = 0
    for image in images:
        image = image[bottom_buffer:top_buffer, :]
        image = image[:, left_buffer:right_buffer]
        for i in range(0, 9):
            lower = i * item_size
            upper = (i + 1) * item_size
            slice = image[lower:upper, :, :]
            slice_name = f"item{counter}.png"
            cv2.imwrite('./items/' + slice_name, slice)
            counter += 1
    print("-------- SPLIT AH PAGE TO ITEMS --------")

def read_date(image):
    raw_text = pytesseract.image_to_string(image)
    text = re.sub("[\\n\"]", "", raw_text)
    return text

def item_to_text():
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    images = [cv2.imread(file) for file in glob.glob("./items/*.png")]
    kernel = np.ones((3,3),np.uint8)
    with open('data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Item", "Total Price", "Per Price", "Date"])
        for image in images:
            date_image = image[:, -220:]
            image = image[:, :-220]
            raw_text = pytesseract.image_to_string(image)
            date = read_date(date_image)
            num_newlines = len(raw_text.split("\n")) - 1
            text = re.split("\\n", raw_text)[num_newlines - 1]
            split = re.split("([A-Za-z])\\s([0-9(])", text)
            try:
                item_name = split[0] + split[1]
                prices = re.split("\\)\\s\\(", (split[2] + split[3]).replace(".", ","))
                if len(prices) > 1:
                    total_price = re.sub("[^0-9]", "", prices[0])
                    per_price = re.sub("[^0-9]", "", prices[1])
                else:
                    total_price = re.sub("[^0-9]", "", prices[0])
                    per_price = ''
                writer.writerow([item_name, total_price, per_price, date])
            except:
                print('\tIgnoring bad OCR: ' + raw_text, split)
    print("-------- WROTE DATA TO CSV --------")
