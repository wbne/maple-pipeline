from video_segmenter import execute_script
from ah_item_extractor import *
from upload_to_gsuite import upload_csv
from cleanup import delete_images
'''
Notes:
    The video MUST be called 'video.mp4' AND be placed in the videos/ folder

'''

def main():
    execute_script()
    page_to_item()
    item_to_text()
    upload_csv()
    delete_images()

if __name__ == "__main__": main()