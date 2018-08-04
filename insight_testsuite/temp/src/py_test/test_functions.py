import os
from src.functions import *
import pytest

@pytest.fixture
def setup_test_data():
	input_file = os.path.dirname(os.path.abspath(__file__))+os.sep+'data_pytest.txt'
	return build_dict(input_file)



@pytest.fixture
def get_process_data(test_data):
	return process_data(test_data)

test_data_dict,skip_rows=setup_test_data()
results=get_process_data(test_data_dict)
	

@pytest.mark.dependency()
def test_build_dict():
	assert isinstance(test_data_dict,dict)
	assert list(test_data_dict.keys())[0] == 'AMBIEN'
	assert skip_rows == 2


@pytest.mark.dependency(depends=['test_build_dict '])
def test_process_data():
	data=results
	assert data[0][0]=='AMBIEN'
	assert int(data[0][1])== 2
	assert float(data[0][2]) == 300.0




@pytest.mark.dependency(depends=['test_process_data'])
def test_write_csv(tmpdir):
	file = tmpdir.join('output.txt')
	write_csv(file.strpath,results)  
	assert file.readlines(1)[0] == 'drug_name,num_prescriber,total_cost\n'



 



