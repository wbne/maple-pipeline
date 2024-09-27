import cv2
import glob
import numpy as np
import pytesseract
import re
import csv

# Here we're hard coding since we know the height is gonna be 1100 pixels
# Usually there should be 50px of padding on the top and bottom
def page_to_item():
    images = [cv2.imread(file) for file in glob.glob("./images/*.png")]
    top_buffer = -5
    bottom_buffer = 5
    right_buffer = -1
    left_buffer = 50
    item_size = 55
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
    TIME_COMPLETED_SIZE = 150
    PER_ITEM_SIZE = 100
    TOTAL_ITEM_SIZE = 225
    UPPER_HALF = 20
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    images = [cv2.imread(file) for file in glob.glob("./items/*.png")]
    kernel = np.ones((3,3),np.uint8)
    with open('data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Item", "Total Price", "Per Price", "Date"])
        for image in images:
            date_image = image[:, -TIME_COMPLETED_SIZE:]
            image = image[:, :-TIME_COMPLETED_SIZE]

            per_item_image = image[:-UPPER_HALF, -PER_ITEM_SIZE:]
            image = image[:, :-PER_ITEM_SIZE]

            total_item_image = image[:-UPPER_HALF, -TOTAL_ITEM_SIZE:]
            name_image = image[:, :-TOTAL_ITEM_SIZE]

            date = read_date(date_image)
            price = pytesseract.image_to_string(per_item_image)
            price = price.replace(".", "").replace(",", "").replace("\n", "")
            total_price = pytesseract.image_to_string(total_item_image)
            total_price = total_price.replace(".", "").replace(",", "").replace("\n", "")
            name = pytesseract.image_to_string(name_image)
            name = name.replace("\n", "")

            # TODO: Make this logic better.
            if len(price) > 0 and len(date) > 0:
                if(price.isnumeric()):
                    writer.writerow([name, total_price, price, date])
                else:
                    print('\tIgnoring bad OCR: ' + str([name, total_price, price, date]))
            else:
                print('\tIgnoring bad OCR: ' + str([name, total_price, price, date]))

    print("-------- WROTE DATA TO CSV --------")
