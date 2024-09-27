counter=1
for video in videos/*
do
	ffmpeg -y -i $video -vf "select=gt(scene\,0.0075)" -vsync 0 images/page_$counter-%03d.png
	counter=counter+1
done
echo "FINISHED PROCESSING VIDEO"
