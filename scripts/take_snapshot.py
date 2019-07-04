""" Take snapshot and save as numpy array. """

from datetime import datetime

import numpy as np
import pyrealsense2 as rs

OUT_DIR = "data/snapshots/"

pipeline = rs.pipeline()
pipeline.start()
depth_frame = pipeline.wait_for_frames().get_depth_frame()
data = depth_frame.get_data()

arr = np.asanyarray(data)

# frame to distance
dist = np.zeros(arr.shape)
for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
        dist[i, j] = depth_frame.get_distance(j, i)

pipeline.stop()

# write to file
np.save(file=OUT_DIR + str(datetime.now()) + ".npy", arr=dist)
