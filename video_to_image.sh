ffmpeg -y -i videos/video.mp4 -vf "crop=1500:1100:500:300, select=gt(scene\,0.0075)" -vsync 0 images/page-%03d.png
echo "FINISHED PROCESSING VIDEO"