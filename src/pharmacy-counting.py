import pandas as pd 
import os
from argparse import ArgumentParser
from functions import *

# This is all the variable which can be passed. I use `argparse` library. 
parser = ArgumentParser()


#parser.add_argument("-f", "--file", dest="myFilenameVariable",help="write report to FILE", metavar="FILE")
parser.add_argument('-i','--input',dest="input_path", help='Filename and location of the input file.', required=True)
parser.add_argument('-o','--output' ,dest="output_path",help='Filename and location of the output file.',default="Not_MenTion")
parser.add_argument('-z','--chunk_size' ,dest="size",help='This is chunk size for the input file. The size of the number of rows to keep on the memory.', default=10**6)
args = parser.parse_args()






#Loop through the whole data    

def test_run():
	#For the big data file, we will set chunksize 
	# that we won't load all data to the memory.
	chunksize=args.size
	input_path=args.input_path

	#Set output file path if not defined.
	output_path=args.output_path
	
	if output_path == "Not_MenTion":
		output_path=os.sep.join(input_path.split(os.sep)[0:-2])+os.sep+'output'+os.sep+'top_cost_drug.txt'

	
	comb_data=read_csv_chunk(input_path,chunksize)
	
	#Recount for the same id from different chunks. Rename the columns. Sort the result.
	comb_data_mod=process_fun(comb_data)\
		.rename(columns={'id':'num_prescriber','drug_cost':'total_cost'})\
		.sort_values(by=['total_cost','drug_name'],ascending=False)

	make_outputfolder(output_path)
	
	#Write a csv file.
	comb_data_mod.to_csv(output_path,index=False)

if __name__ == '__main__':
	test_run()
