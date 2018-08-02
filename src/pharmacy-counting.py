import pandas as pd 
import os
from argparse import ArgumentParser


# This is all the variable which can be passed. I use `argparse` library. 
parser = ArgumentParser()


#parser.add_argument("-f", "--file", dest="myFilenameVariable",help="write report to FILE", metavar="FILE")
parser.add_argument('-i','--input',dest="input", help='Filename and location of the input file.', required=True)
parser.add_argument('-o','--output' ,dest="output",help='Filename and location of flagged_purchases.json file', default='flagged_purchases.json')
parser.add_argument('-z','--chunk_size' ,dest="size",help='This is chunk size for the input file. The size of the number of rows to keep on the memory.', default=10**6)
args = parser.parse_args()



def process_data(data):
	"""This function will return drug name, total drug cost 
	and total number of prescribers from input data files."""
    return (data.groupby('drug_name')
       .agg({'id':'count', 'drug_cost': 'sum'})
       .reset_index()
       #.rename(columns={'id':'num_prescriber','drug_cost':'total_cost'})
    )


#For the big data file, we will set chunksize 
# that we won't load all data to the memory.
chunksize=10**4

#Loop through the whole data    