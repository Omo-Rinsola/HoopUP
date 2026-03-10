"""
Orchestrates the full analysis pipeline — from raw video bytes to final coaching feedback.
This is the single entry point the router calls.
"""


from .process_video import process
from .pose_analysis import  get_pose

def analyse_video(contents):
    # process video
    filepath = process(contents)
    # return filepath

    # get frame for specific pose e.g set  point
    set_point_frame = get_pose(filepath)
    return set_point_frame


# analyse mechanics


#  get coach feedback and return result

