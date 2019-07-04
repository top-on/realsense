import matplotlib.pyplot as plt
import numpy as np

FILE = "data/snapshots/2019-07-04 21:42:44.251837.npy"

arr = np.load(FILE)

plt.imshow(arr)
