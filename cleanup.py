import os
import glob

def delete_images():
    directories = ['./images/', './items/']
    for dir in directories:
        removing_files = glob.glob(dir + '*.png')
        for file in removing_files:
            os.remove(file)
    os.remove("data.csv")
