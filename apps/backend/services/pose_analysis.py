"""
Analyses the uploaded video and extracts key frames at critical moments
in the shooting motion — base, set point, release, and follow-through.
These frames are passed to mechanics checks for form analysis.
"""
import numpy as np
import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose


# -------------functions ------------
def calculate_angle(a, b, c):
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)

    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - \
              np.arctan2(a[1] - b[1], a[0] - b[0])

    angle = np.abs(radians * 180.0 / np.pi)

    if angle > 180:
        angle = 360 - angle

    return angle


# ----------------------------



def get_pose(filename):

    min_angle = float('inf')
    set_point_frame = None

    cap = cv2.VideoCapture(filename)

    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            results = pose.process(image)
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            # get set point frame
            try:
                landmarks = results.pose_landmarks.landmark
                point = mp_pose.PoseLandmark

                wrist_r = [landmarks[point.RIGHT_WRIST.value].x,
                           landmarks[point.RIGHT_WRIST.value].y
                           ]
                elbow_r = [landmarks[point.RIGHT_ELBOW.value].x,
                           landmarks[point.RIGHT_ELBOW.value].y]

                shoulder_r = [landmarks[point.RIGHT_SHOULDER.value].x,
                              landmarks[point.RIGHT_SHOULDER.value].y]

                # knee_r = [landmarks[point.RIGHT_KNEE.value].x,
                #           landmarks[point.RIGHT_KNEE.value].y]
                # hip , knee, ankle ( for base )

                # Get set point: maximum elbow bend before extension.
                angle = calculate_angle(shoulder_r, elbow_r, wrist_r)
                if angle < 160 and angle < min_angle:
                    min_angle = angle
                    set_point_frame = frame.copy()
                    set_point_landmark = (wrist_r, elbow_r)

                # get base
            except AttributeError:
                print("No pose detected in frame")
            except Exception as e:
                print(f"Error processing landmarks: {e}")




    cap.release()

    if set_point_frame is not None:
        print(f"Set point elbow angle: {min_angle:.2f} degrees")
        cv2.imwrite("debug_setpoint.jpg", set_point_frame)
        return set_point_frame, set_point_landmark
    else:
        print("No set point detected")


