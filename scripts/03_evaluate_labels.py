""" Evaluate labelled data """
# %%
import os
from collections import namedtuple
from pathlib import Path

import numpy as np
from bs4 import BeautifulSoup

DIR_LABELS = "data/snapshots/labels/"
DIR_IMAGES = "data/snapshots/jpg/"
DIR_ARRAYS = "data/snapshots/npy/"

label_files = [DIR_LABELS + i for i in os.listdir(DIR_LABELS)]
img_ids = [Path(i).stem for i in label_files]

img_files = [Path(DIR_IMAGES + i).with_suffix(".jpg").__str__() for i in img_ids]
arr_files = [Path(DIR_ARRAYS + i).with_suffix(".npy").__str__() for i in img_ids]

# %%
Box = namedtuple("Box", "xmin xmax ymin ymax")


def parse_object_to_box(tag) -> Box:
    xmin = int(tag.find("xmin").text)
    xmax = int(tag.find("xmax").text)
    ymin = int(tag.find("ymin").text)
    ymax = int(tag.find("ymax").text)
    _box = Box(xmin, xmax, ymin, ymax)
    return _box


def parse_xml_to_boxes(xml: str, name: str) -> Box:
    soup = BeautifulSoup(xml, "xml")
    obj = soup.find("name", string=name).parent
    box = parse_object_to_box(obj)
    return box


# %%
# label_file = label_files[0]
# arr_file = arr_files[0]
for label_file, arr_file in zip(label_files, arr_files):
    # read label file
    with open(label_file) as fd:
        text = fd.read()
    # parsing boxes
    box_low: Box = parse_xml_to_boxes(xml=text, name="low")
    box_high: Box = parse_xml_to_boxes(xml=text, name="high")
    # depth information from bounding boxes
    arr_low = np.load(arr_file)[
        box_low.ymin : box_low.ymax, box_low.xmin : box_low.xmax
    ]
    arr_high = np.load(arr_file)[
        box_high.ymin : box_high.ymax, box_high.xmin : box_high.xmax
    ]
    # calculate tread depth
    depth_mm = (np.median(arr_low) - np.median(arr_high)) * 1000
    print(f"Median profile depth of {label_file}: {depth_mm:.2f}")

# %%
