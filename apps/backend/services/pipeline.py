"""
Orchestrates the full analysis pipeline — from raw video bytes to final coaching feedback.
This is the single entry point the router calls.
"""


from .process_video import process
from .pose_analysis import get_pose
from .analyse_mechanics import elbow_alignment

def analyse_video(contents):
    # process video
    filepath = process(contents)
    # return filepath

    # get frame for specific pose e.g set  point
    set_point_frame, set_point_landmark = get_pose(filepath)
    # check vertical elbow alignment at set point
    result = elbow_alignment(set_point_landmark)
    return result







#  get coach feedback and return result

