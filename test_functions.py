import pandas as pd 
import os
import numpy as np 
from functions import *

data1=pd.DataFrame({"id":[1000000001,1000000002,1000000002,'\? '],\
                    "prescriber_last_name":["Smith","Garcia","Garcia","Rodriguez"],\
                    "prescriber_first_name":["James","Maria","Maria","Maria"],\
                    "drug_name":["AMBIEN","AMBIEN","AMBIEN","CHLORPROMAZINE"],\
                    "drug_cost":[100,200,' ',300]})
def test():
	print(data1)
print(data1)
if __name__ == '__main__':
	print("hello")