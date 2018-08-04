import os
import errno

def build_dict(file_path):
	""" This function removes the improper data and also build the dictionary at the same time. 
		It clean out the data by reassuring 'id' have to be an integer and 
	'drug_cost' can be able to converted to a float. If any row contains entries with incorrect data formats,
	this function will skip it and go to the next row in the data file.
	"""
	data_dict={}
	skip_rows=0
	with open(file_path,'r') as f:
		next(f)
		for line in f:
			line_to_list=line.split(',')
			per_id=line_to_list[0]
			drug_name=line_to_list[-2]
			drug_cost=line_to_list[-1]
			try:
				int(per_id)
				float(drug_cost)
			
				data_dict.setdefault(drug_name,[]).append({per_id:drug_cost})
			except ValueError:
				skip_rows +=1
				continue
		f.close()
		
	return data_dict,skip_rows

def process_data(data):
	""" This function count the number of prescribers for each drug_name and 
	at the same time, it also sums all the drug cost for each drug_name."""
	results=[]
	drug_name=[]
	for k,v in data.items():
		drug_name.append(k)
		id_list=[]
		cost_list=[]
		total=0
		for i in v:
			for k2,v2 in i.items():
				id_list.append(k2)
				total +=float(v2)
		results.append([k,len(set(id_list)),total])
		results=sorted(results,key=lambda l:(l[2],l[0]), reverse=True)
	return results
		

def write_csv(filepath,data):
	""" Write the data back to a csv file with these values:'drug_name','num_prescriber','total_cost'.
	"""
	data.insert(0,['drug_name','num_prescriber','total_cost'])
	with open(filepath,'w+') as f:
		for sublist in data:
			one_string=','.join(map(str, sublist))+'\n'
			f.write(one_string)
 





def make_outputfolder(output_path):
	#Create an folder for output file if it doesn't exist. 
	if not os.path.exists(os.path.dirname(output_path)):
		try:
			os.makedirs(os.path.dirname(output_path))
		except OSError as exc: # Guard against race condition
			if exc.errno != errno.EEXIST:
				raise
