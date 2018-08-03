import pandas as pd 
import os
import numpy as np 
from src.functions import *
import pytest
np.seterr(divide='ignore', invalid='ignore')

@pytest.fixture
def setup_test_data():
	input_file = os.path.dirname(os.path.abspath(__file__))+os.sep+'data_pytest.txt'
	return read_csv(input_file)



@pytest.fixture
def setup_clean_test_data(test_data):
	return clean_data(test_data)

test_data=setup_test_data()
cleaned_test_data,rows=setup_clean_test_data(test_data)
	

@pytest.mark.dependency()
def test_read_csv():
	data=test_data.iloc[0,:].values
	assert int(data[0])==1000000001
	assert data[1]=='AMBIEN'
	assert int(data[2])== 100

@pytest.mark.dependency(depends=['test_read_csv'])
def test_clean_data():
	assert isinstance(cleaned_test_data,pd.DataFrame)
	assert rows == 2

@pytest.mark.dependency(depends=['test_clean_data'])
def test_process_fun():
	results=process_fun(cleaned_test_data)
	assert isinstance(results,pd.DataFrame)
	assert results.num_prescriber.values[0] == 2
	assert results.total_cost.values[0]	 == 300.0



 



