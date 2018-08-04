import pandas as pd 
import os
import numpy as np 

def read_csv(filename):
	""" Read selected columns ['id','drug_name', and 'drug_cost'] from a csv file to memory. 
	Make sure 'drug_cost' is in float data type. 

	"""

	data=pd.read_csv(filename,usecols=['id','drug_name','drug_cost'])
	return data

def clean_data(data):
	""" Clean data by removing typos and misplaced strings.
	"""
	data[['drug_cost','id']]=data[['drug_cost','id']].apply(pd.to_numeric, downcast='unsigned',errors='coerce')
	missing_rows=np.count_nonzero(data.isnull())
	data.dropna(how='any',inplace=True)
	data['id']=data['id'].astype(int)
	return data,missing_rows



def process_fun(data):
	data.dropna(how='any',inplace=True)
	"""This function will return drug name, total drug cost 
	and total number of prescribers from input data files 
	in descending order by total_cost followed by 'drug_name'."""
	return (data.groupby('drug_name')
		.agg({'id':'nunique', 'drug_cost': 'sum'})
		.reset_index()
		.rename(columns={'id':'num_prescriber','drug_cost':'total_cost'})
		.sort_values(by=['total_cost','drug_name'],ascending=False)
		)



def make_outputfolder(output_path):
	#Create an folder for output file if it doesn't exist. 
	os.makedirs(os.path.dirname(output_path), exist_ok=True)
