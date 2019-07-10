""" Comparing prediction from images to measured ground truth. """

from typing import List

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
print(f"GROUND TRUTH (in mm)\nData: {truth}\nDistribution:{stats.describe(truth)}\n")
print(
    "PREDICTIONS FROM CAMERA (in mm)\n"
    f"Data: {prediction}\n"
    f"Distribution:{stats.describe(prediction)}"
)
