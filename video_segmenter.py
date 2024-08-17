import subprocess

def execute_script():
    video2image = './video_to_image.sh'
    video_dir = './videos/'
    video_filename = 'movie.mp4'
    image_dir = './images/'
    subprocess.call(['C:\\Program Files\\Git\\bin\\sh.exe', video2image])