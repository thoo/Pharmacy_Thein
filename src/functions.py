import pandas as pd 
import os

def process_fun(data):
	"""This function will return drug name, total drug cost 
	and total number of prescribers from input data files."""
	return (data.groupby('drug_name')
		.agg({'id':'count', 'drug_cost': 'sum'})
		.reset_index())

def read_csv_chunk(filename,chunksize):
	""" Read csv file in chunks and select the related columns. Count 'drug_name' column for the identical name 
	and sum the amount of cost from drug_cost column. Return as a data frames."""
	data_frames=[process_fun(chunk) for chunk in pd.read_csv(filename, chunksize=chunksize,\
		usecols=['id','drug_name','drug_cost'])]
	return pd.concat(data_frames)

def make_outputfolder(output_path):
	#Create an folder for output file if it doesn't exist. 
	os.makedirs(os.path.dirname(output_path), exist_ok=True)
