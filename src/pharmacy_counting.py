import os
from argparse import ArgumentParser
from functions import *

# This is all the variable which can be passed. I use `argparse` library. 
parser = ArgumentParser()


#parser.add_argument("-f", "--file", dest="myFilenameVariable",help="write report to FILE", metavar="FILE")
parser.add_argument('-i','--input',dest="input_path", help='Filename and location of the input file.', required=True)
parser.add_argument('-o','--output' ,dest="output_path",help='Filename and location of the output file.',default="Not_MenTion")

args = parser.parse_args()







def test_run():
	
	input_path=args.input_path

	#Set output file path if not defined.
	output_path=args.output_path
	
	if output_path == "Not_MenTion":
		output_path=os.sep.join(input_path.split(os.sep)[0:-2])+os.sep+'output'+os.sep+'top_cost_drug.txt'

	
	data_dict,skip_rows=build_dict(input_path)
	
	results=process_data(data_dict)
	

	make_outputfolder(output_path)
	
	#Write a csv file.
	write_csv(output_path,results)

	print("\033[95m \033[1m {} rows have missing values and they are excluded in the process.".format(skip_rows))

if __name__ == '__main__':
	test_run()
