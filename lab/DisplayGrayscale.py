#!/usr/bin/env python3

'''
@author: Stephanie Galvan
@course: Theory of Operating Systems
@assignment: 3 - Threaded Video Player
@python-version: 3.6.5
'''

import cv2

FILE_NAME = '../clip.mp4'

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


def convert_grayscale():
    '''
    Converts frames to grayscale
    '''
    pass


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
