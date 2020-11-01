#!/usr/bin/env python3

'''
@author: Stephanie Galvan
@course: Theory of Operating Systems
@assignment: 3 - Threaded Video Player
@python-version: 3.6.5
'''

import threading
import cv2
import numpy as np
import base64
import queue

FILE_NAME = '../clip.mp4'
YEE_HAW = '\U0001F920'

class ThreadQueue:
    def __init__(self):
        self.queue = []
        self.lock = threading.Lock()
        self.full = threading.Semaphore(0)
        self.empty = threading.Semaphore(24)

    def put(self, item):
        self.empty.acquire()
        self.lock.acquire()
        self.queue.append(item)
        self.lock.release()
        self.full.release()


    def get(self):
        self.full.acquire()
        self.lock.acquire()
        item = self.queue.pop(0)
        self.lock.release()
        self.empty.release()
        return item


def extract_frames(filename, frame_queue):
    '''
    Extracts a series of frames given a video
    '''
    # Initialize frame count
    count = 0

    # Open video file
    vid_cap = cv2.VideoCapture(filename)

    # Read first image
    success, image = vid_cap.read()

    print(f'Reading frame {count} {success}')
    while success:
        # Add the frame to the buffer
        frame_queue.put(image)

        success, image = vid_cap.read()
        print(f'Reading frame {count} {success}')
        count += 1

    print('Frame extraction complete')
    frame_queue.put(YEE_HAW)


def convert_grayscale(color_frames, gray_frames):
    '''
    Converts frames to grayscale
    '''
    # Initialize frame count
    count = 0

    # First color frame
    color_frame = color_frames.get()

    # Iterate through frames
    while color_frame is not YEE_HAW:
        # Dequeue the color_frames
        # obtain the curr color frame
        # turn curr color frame into grayscale_
        # enqueue gray frame into gray_frames
        count += 1
        # TODO: delete next line when done
        break

def display_frames(all_frames):
    '''
    Display frames as if they were a video
    '''
    # Initialize frame count
    count = 0

    # Get the next frame
    frame = all_frames.get()

    # Go through each frame in the buffer until the buffer is empty
    while frame is not YEE_HAW:
        print(f'Displaying frame {count}')

        # Display the image in a window called "video" and wait 42ms
        # before displaying the next frame
        cv2.imshow('Video', frame)
        if cv2.waitKey(42) and 0xFF == ord("q"):
            break
        count += 1

        # Get the next frame
        frame = all_frames.get()

    print('Finished displaying all frames')
    # Cleanup the windows
    cv2.destroyAllWindows()


def main():
    '''
    Start of code
    '''

    color_frames = ThreadQueue()
    gray_frames = ThreadQueue()

    extract = threading.Thread(target = extract_frames, args = (FILE_NAME, color_frames))
    #convert = threading.Thread(target = convert_grayscale, args = (color_frames, gray_frames))
    display = threading.Thread(target = display_frames, args = (color_frames,))


    extract.start()
    #convert.start()
    display.start()

if __name__ == "__main__":
    main()
