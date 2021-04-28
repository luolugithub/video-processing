# Image processing on a video stream

Reads a stream off a video input, applies image processing on each frame, and shows it on-screen real-time.
Requires: Python, Numpy, Scipy, OpenCV.

### Installation
Assuming you have `pip` installed (python's package manager). To install the requirements use:
```
pip install -r requirements.txt
```

G.Sfikas, Nov 2017


##  Video split and restore
# ffmpeg -framerate 30.00 -pattern_type glob -i '*.jpg' -c:v libx264 -r 30 -pix_fmt yuv420p jdd_video.mp4
# ffmpeg -i video.mp4 -i audio.wav -c:v copy -c:a aac output.mp4

## Insert frame into video
ffmpeg -i need_process_video.mp4 -loop 1 -i insert_frame.png -filter_complex "[0][1]overlay=enable='if(gt(n,0),not(mod(n,20)),0)':shortest=1[v]" -map "[v]" -map 0:a -c:a copy out.mp4


## convert avi to mp4
 ffmpeg -i infile.avi youroutput.mp4
 
## speed mp4 to gif
ffmpeg -i Rec0001.mp4 -filter:v "setpts=0.15*PTS" -r 30 lubs12.gif
