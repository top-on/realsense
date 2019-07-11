""" Comparing prediction from images to measured ground truth. """

from typing import List

import numpy as np
from scipy import stats

GROUND_TRUTH: str = "data/comparison/ground_truth_15626997.txt"
IMAGE_PREDICTIONS: str = "data/comparison/image_predictions_15626997.txt"


def read_to_list(path: str) -> List[float]:
    with open(path) as f:
        lines = f.readlines()
        truth = [float(x.strip()) for x in lines]
    return truth


# read files
truth: List[float] = read_to_list(GROUND_TRUTH)  # ground truth
prediction: List[float] = read_to_list(IMAGE_PREDICTIONS)  # predictions

# report comparison
print(f"GROUND TRUTH (in mm):")
print(f"Data: {truth}")
print(stats.describe(truth))
print(f"Standard deviation: {np.std(truth):.3f}\n")

print("PREDICTIONS FROM CAMERA (in mm):")
print(f"Data: {prediction}")
print(stats.describe(prediction))
print(f"Standard deviation: {np.std(prediction):.3f}")
