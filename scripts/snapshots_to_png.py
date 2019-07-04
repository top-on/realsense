import os
from pathlib import Path

import numpy as np
import png

DIR_IN = "data/snapshots/npy/"
DIR_OUT = "data/snapshots/png/"

MAX_DIST = 0.5

npy_files = [i for i in os.listdir(DIR_IN) if i.endswith(".npy")]

for file in npy_files:
    arr = np.load(DIR_IN + file)

    depth_center = arr[int(arr.shape[0] / 2), int(arr.shape[1] / 2)]
    depth_min = depth_center - 0.05
    depth_max = depth_center + 0.05
    # clip high and low valuess
    arr[arr > depth_max] = depth_max
    arr[arr < depth_min] = depth_min
    # normalize to [0, 255]
    arr_trans = ((arr - depth_min) / (depth_max - depth_min) * 65535).astype(np.uint16)
    # write to file
    file_out = Path(DIR_OUT + file).with_suffix(".png")
    # write as 16 bit PNG
    with open(file_out, "wb") as f:
        writer = png.Writer(
            width=arr_trans.shape[1],
            height=arr_trans.shape[0],
            bitdepth=16,
            greyscale=True,
        )
        zgray2list = arr_trans
        writer.write(f, zgray2list)
