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

class ThreadQueue:
    def __init__(self):
        self.queue = []
        self.lock = threading.Lock()
        self.full = threading.Semaphore(0)
        self.empty = threading.Semaphore(24)

    def put(self, item):
        empty.acquire()
        lock.acquire()
        queue.append(item)
        lock.release()
        full.release()

    def get(self):
        full.acquire()
        lock.acquire()
        item = queue.pop(0)
        lock.release()
        empty.release()


def extract_frames(frame_queue):
    '''
    Extracts a series of frames given a video
    '''
    # Initialize frame count
    count = 0

    # Open video file
    vid_cap = cv2.VideoCapture(FILE_NAME)

    # Read first image
    success, image = vid_cap.read()

    print(f'Reading frame {count} {success}')
    while success:
        # TODO: Add the frame to the buffer
        # frame_queue put image

        success, image = vid_cap.read()
        print(f'Reading frame {count} {success}')
        count += 1

    print('Frame extraction complete')


def convert_grayscale(color_frames, gray_frames):
    '''
    Converts frames to grayscale
    '''
    # Initialize frame count
    count = 0

    # Iterate through frames
    while not color_frames.empty():
        # dequeue the color_frames
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

    # Go through each frame in the buffer until the buffer is empty
    while not all_frames.empty():
        # TODO: Get the next frame
        # frame = dequeue all_frames

        print(f'Displaying frame {count}')

        # Display the image in a window called "video" and wait 42ms
        # before displaying the next frame
        cv2.imshow('Video', frame)
        if cv2.waitKey(42) and 0xFF == ord("q"):
            break

        count += 1

    print('Finished displaying all frames')
    # cleanup the windows
    cv2.destroyAllWindows()


def start():
    '''
    Start of code
    '''
    pass


if __name__ == "__main__":
    start()
