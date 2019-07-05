""" Evaluate labelled data """

import os
from pathlib import Path

from bs4 import BeautifulSoup

DIR_LABELS = "data/snapshots/labels/"
DIR_IMAGES = "data/snapshots/npy/"
DIR_ARRAYS = "data/snapshots/npy/"

label_files = [DIR_LABELS + i for i in os.listdir(DIR_LABELS)]
img_ids = [Path(i).stem for i in label_files]

img_files = [Path(DIR_IMAGES + i).with_suffix(".jpg").__str__() for i in img_ids]
arr_files = [Path(DIR_ARRAYS + i).with_suffix(".npy").__str__() for i in img_ids]

with open(label_files[0]) as fd:
    xml = fd.read()
    
soup = BeautifulSoup(xml, "xml")
names = [i.find('name').text for i in soup.find_all('object')]
soup.find_all('object')[0].find('bndbox').__dict__

# TODO parse XML
