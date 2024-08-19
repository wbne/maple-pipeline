from video_segmenter import execute_script
from ah_item_extractor import *
from upload_to_gsuite import upload_csv
from cleanup import delete_images
'''
Notes:
    The video MUST be called 'video.mp4' AND be placed in the videos/ folder
    If setting this up for the first time, generate credentials.json via https://console.cloud.google.com/apis/credentials
    The images extracted from the video will be deleted after execution

    Currently the resolution is hardcoded so the resulting image/video processing is hardcoded with it
    Updates will slowly roll out cleaning up code, improving OCR accuracy, and streamlining the data pipeline
'''

def main():
    execute_script()
    page_to_item()
    item_to_text()
    upload_csv()
    delete_images()

if __name__ == "__main__": main()