"""
Evaluates shooting mechanics on key frames extracted from the video.
Checks specific body positions and angles against ideal basketball form standards.
"""
import cv2
# import mediapipe as mp
#
# mp_drawing = mp.solutions.drawing_utils
# mp_pose = mp.solutions.pose

# get set point and check  if elbow-wrist  is vertically aligned

# get vertical position : basically means the hand can only move up or down in the y direction
#  and the x value will be constant ...: soo the wrist x and the elbow x  will be the same constant value .

# In reality they will never be exactly the same. So your check becomes:
# How different are the X values of the elbow and wrist?
# If the difference is small — forearm is close to vertical, good form.
# If the difference is large — forearm is leaning, bad form.


def vertical_position(landmark1, landmark2):
    delta_x = landmark1 - landmark2


def elbow_alignment(landmarks):
    wrist, elbow = landmarks
    delta_x = wrist[0] - elbow[0]
    return abs(delta_x)






