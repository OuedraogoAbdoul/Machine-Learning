import os
import json
import gzip
import pandas as pd
from urllib.request import urlopen
import wget
import patoolib
from pathlib import Path
import numpy as np
import arff
import wget

# Download the dataset
url = 'https://s3.amazonaws.com/amazon-reviews-pds/tsv/amazon_reviews_us_Wireless_v1_00.tsv.gz'
my_file = Path("amazon_reviews_us_Wireless_v1_00.tsv.gzwc8rkdtr.tmp")

if not my_file.is_file():
    wget.download(url)
# Read the dataset

# data = pd.read_csv('sample_us.tsv',delimiter='\t',encoding='utf-8')
# total length of list, this number equals total number of products
print(len(data))

# first row of the list
print(data)
