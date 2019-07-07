""" Convert arrays with depth information to images. """
# %%
import os
from pathlib import Path
from typing import Dict, Tuple

import cv2 as cv
import numpy as np
import png

DIR_IN = "data/snapshots/npy/"
DIR_OUT = "data/snapshots/png/"

MAX_DIST = 0.5

npy_files = [DIR_IN + i for i in os.listdir(DIR_IN) if i.endswith(".npy")]


# %%
def save_16bit_png(array: Dict[Tuple[int, int], float], file_path: str):
    # normalize to [0, 1]
    arr_norm = (array - np.min(array)) / np.ptp(array)
    # 'strech' to [0, 2**16]
    arr_16bit = (arr_norm * 2**16).astype(np.uint16)
    # write as 16 bit PNG
    with open(file_path, "wb") as f:
        writer = png.Writer(
            width=arr_16bit.shape[1],
            height=arr_16bit.shape[0],
            bitdepth=16,
            greyscale=True,
        )
        writer.write(f, arr_16bit)


# %%
# npy_file = npy_files[1]
for npy_file in npy_files:
    arr = np.load(npy_file)
    # clip high and low valuess
    depth_center = arr[int(arr.shape[0] / 2), int(arr.shape[1] / 2)]
    depth_min = max(depth_center - 0.05, 0.01)  # closer than center, but greater 0
    depth_max = depth_center + 0.1
    arr[arr > depth_max] = depth_max
    arr[arr < depth_min] = depth_min
    # write to file
    png_file = DIR_OUT + Path(npy_file).stem + ".png"
    save_16bit_png(array=arr, file_path=png_file)

# %%
