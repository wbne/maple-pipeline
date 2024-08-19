# maple-pipeline
## Version 1.1
 ETL pipeline to process videos of AH items and upload the results as a csv to gsuite

Notes:
- The video MUST be called 'video.mp4' AND be placed in the videos/ folder
- If setting this up for the first time, generate credentials.json via https://console.cloud.google.com/apis/credentials
- The images extracted from the video will be deleted after execution
- Currently the resolution is hardcoded so the resulting image/video processing is hardcoded with it
- Updates will slowly roll out cleaning up code, improving OCR accuracy, and streamlining the data pipeline