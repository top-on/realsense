
import os
from pathlib import Path

import imageio
import numpy as np


DIR_IN = "data/snapshots/npy/"
DIR_OUT = "data/snapshots/png/"

MAX_DIST = 0.5

npy_files = [i for i in os.listdir(DIR_IN) if i.endswith(".npy")]

for file in npy_files:
    arr = np.load(DIR_IN + file)
    arr[arr > MAX_DIST] = MAX_DIST  # clipping distances greater MAX_DIST in meter
    file_out = Path(DIR_OUT + file).with_suffix('.png')
    imageio.imwrite(uri=file_out, im=arr)
