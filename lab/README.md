# Producer Consumer Lab
**Author:** Stephanie Galvan <br />
**Python version:** 3.6.5
## Description
In this lab, a colorized video is turned into a grayscale video with the use of semaphores
## Used libraries

    sudo zypper -n install python3-devel
    sudo zypper -n install ffmpeg ffmpeg-3
    sudo zypper -n install gstreamer gstreamer-devel
    sudo zypper -n install python3-numpy
    sudo pip install --upgrade pip
    sudo pip install opencv-python

## Inside DisplayGrayscale.py
### Class List
#### ThreadQueue
ThreadQueue is a class that represents a queue handled by a thread. The class contains two methods: `get()` which dequeues the queue and returns the item, and `put(item)` which enqueues an item (in this lab, a frame) into the queue
### Functions List
#### extract_frames
This function extracts the frames from the video 'clip.mp4' and saves them into a queue as jpeg images
#### convert_grayscale
This function converts a series of frames into grayscale and saves them as jpeg images into a queue
#### display_frames
Loads a series of frames and displays them with a 42ms delay
## Features

* [x] Extract frames from a video file, convert them to grayscale, and display
them in sequence
* [x] You must have three functions
  * [x] One function to extract the frames
  * [x] One function to convert the frames to grayscale
  * [x] One function to display the frames at the original framerate (24fps)
* [x] The functions must each execute within their own python thread
  * [x] The threads will execute concurrently
  * [x] The order threads execute in may not be the same from run to run
* [x] Threads will need to signal that they have completed their task
* [x] Threads must process all frames of the video exactly once
## How to run
In a console, move into the current directory (`/lab`) and run the command `./DisplayGrayscale.py`
