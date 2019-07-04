# First import the library
import matplotlib.pyplot as plt
import numpy as np
import pyrealsense2 as rs


# Create a context object. This object owns the handles to all connected realsense devices
pipeline = rs.pipeline()
pipeline.start()
depth_frame = pipeline.wait_for_frames().get_depth_frame()
data = depth_frame.get_data()

arr = np.asanyarray(data)
plt.imshow(arr)

# frame to distance
dist = np.zeros(arr.shape)
for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
        dist[i, j] = depth_frame.get_distance(j, i)

# removing too low and too high values
dist[dist > 1] = np.nan
dist[dist == 0] = np.nan

plt.imshow(dist)
np.max(dist)


plt.hist(dist[dist < 0.9], bins=100)

pipeline.stop()
