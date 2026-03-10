import numpy as np
import tempfile
import os




def process(video_bytes):
    # Create a temporary file and write the bytes to it
    with tempfile.NamedTemporaryFile(suffix=".mp4", delete=False) as temp_file:
        temp_filename = temp_file.name
        temp_file.write(video_bytes)
    # os.remove(temp_filename)
    return temp_filename
