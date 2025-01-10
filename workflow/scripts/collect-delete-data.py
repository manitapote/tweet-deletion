import pandas as pd
from pathlib import Path
import glob

raw_data_path = './../data/Raw'
derived_path = './../data/Derived'

def read_file(path):
	print(glob('{}/*.json.gz'.format(path)))
        for file_name in glob.glob('{}/*.json.gz'.format(path)):
                print(file_name)
                break

read_file(raw_data_path)

