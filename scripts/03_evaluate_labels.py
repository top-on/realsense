""" Evaluate labelled data """
# %%
import os
from collections import namedtuple
from pathlib import Path
from typing import Tuple

from bs4 import BeautifulSoup

DIR_LABELS = "data/snapshots/labels/"
DIR_IMAGES = "data/snapshots/npy/"
DIR_ARRAYS = "data/snapshots/npy/"

label_files = [DIR_LABELS + i for i in os.listdir(DIR_LABELS)]
img_ids = [Path(i).stem for i in label_files]

img_files = [Path(DIR_IMAGES + i).with_suffix(".jpg").__str__() for i in img_ids]
arr_files = [Path(DIR_ARRAYS + i).with_suffix(".npy").__str__() for i in img_ids]


def parse_object_to_box(tag) -> Tuple[int, int, int, int]:
    Box = namedtuple("Box", "xmin xmax ymin ymax")
    xmin = int(tag.find("xmin").text)
    xmax = int(tag.find("xmax").text)
    ymin = int(tag.find("ymin").text)
    ymax = int(tag.find("ymax").text)
    _box = Box(xmin, xmax, ymin, ymax)
    return _box


def parse_xml_to_boxes(
    xml: str
) -> Tuple[Tuple[int, int, int, int], Tuple[int, int, int, int]]:
    soup = BeautifulSoup(xml, "xml")
    obj_low = soup.find("name", string="low").parent
    obj_high = soup.find("name", string="high").parent
    box_low = parse_object_to_box(obj_low)
    box_high = parse_object_to_box(obj_high)
    return box_low, box_high


# %%
with open(label_files[0]) as fd:
    text = fd.read()

boxes = parse_xml_to_boxes(xml=text)
# %%
