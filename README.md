# Table of Contents

1. [Challenge](README.md#anomaly-detection)

2. [Implementation](README.md#implementation)

   1. [Package Requirements](README.md#package-requirements)
   2. [Installation](README.md#installation)
   3. [Usage](README.md#usage)
   4. [Details of Implementation](README.md#details-of-implementation)
   5. [Unit Testing](README.md#unit-testing)

3. [Performance](#performance)

4. [Conclusion](#conclusion)

# Challenge

I will work on the challenge mentioned [here](https://github.com/InsightDataScience/pharmacy_counting). Here is the summary of the challenge. 

> Imagine you are a data engineer working for an online pharmacy. You are asked to generate a list of all drugs, the total number of UNIQUE individuals who prescribed the medication, and the total drug cost, which must be listed in descending order based on the total drug cost and if there is a tie, drug name.

In general, I was provided with a real-world data file in `csv` format and I have to manipulate and extract information data from it and write an output file in `csv` format.  Here is the example shown as a part of the instruction.

> For example
> 
> If your input data, **`itcont.txt`**, is
> 
> ```
> id,prescriber_last_name,prescriber_first_name,drug_name,drug_cost
> 1000000001,Smith,James,AMBIEN,100
> 1000000002,Garcia,Maria,AMBIEN,200
> 1000000003,Johnson,James,CHLORPROMAZINE,1000
> 1000000004,Rodriguez,Maria,CHLORPROMAZINE,2000
> 1000000005,Smith,David,BENZTROPINE MESYLATE,1500
> ```
> 
> then your output file, **`top_cost_drug.txt`**, would contain the following lines
> 
> ```
> drug_name,num_prescriber,total_cost
> CHLORPROMAZINE,2,3000
> BENZTROPINE MESYLATE,1,1500
> AMBIEN,2,300
> ```

This is a fun and exciting project. For this challenge I will use `Python 3.6.4` with a few libraries mentioned in [**Package Requirements**](README.md#package-requirements) section. 

# Implementation

This section will walk you through the pre-requirements and the implementation of this challenge.  

## Package Requirements

I used `Python 3.6.4`. The following list is the pre-requirement for this challenge which is listed in `requirements.txt` file located at `src/requirements.txt`. 

```
atomicwrites==1.1.5
attrs==18.1.0
more-itertools==4.3.0
pluggy==0.7.1
py==1.5.4
pytest==3.7.1
six==1.11.0
```

## Installation

**First**, clone the repository.

```
git clone https://github.com/thoo/Pharmacy_Thein
cd Pharmacy_Thein
```

**Second (if you want to use `virtualenv` otherwise skip this step.)**,

* With `virtualenv`, ``` virtualenv -p python3 venv
  virtualenv -p python3 venv
  source venv/bin/activate
  ```

**Finally**, we can install all the required packages.

```pip
pip install -r src/requirements.txt
```

## Usage

First, you can check everything is woking by running `./run.sh` .  The script for this project is located in `src` directory. So you can also run your data file using:

```
python ./src/pharmacy_counting.py \
                  -i your_input_file_path \
                  -o your_output_file_path
```

The `pharmacy_counting.py` also prints out the number of rows with any missing data which are excluded in the process.

## Details of Implementation

First, the columns `id,drug_name,drug_cost` of  the input data file  is loaded into the memory as a `pandas` dataframe. To save the memory usage, I only selected the necessary columns for data processing.  

This is a real-world data and therefore, I have a function to rigorously clean the data. After that I do count uniquely `id`  for each `drug_name` and also sum all the `drug_cost` for each `drug_name`.  

All the functions mentioned aboved are located in `src/functions.py` . Here is the summary of each function:

* **build_dict** : *This function removes the improper data and also build the dictionary at the same time. It clean out the data by reassuring 'id' have to be an integer and  'drug_cost' can be able to converted to a float. If any row contains entries with incorrect data formats, this function will skip it and go to the next row in the data file.*

* **process_data** : *This function count the number of prescribers for each drug_name and at the same time, it also sums all the drug cost for each drug_name.*

* **write_csv** : *Write the data back to a csv file with these values:'drug_name', 'num_prescriber', 'total_cost'.*.

* **make_outputfolder** : *Make sure that the output foler exists and if it doesn't, create an folder named 'output'*.

## Unit Testing

I use `pytest` for unit testing. All the files related to `unit testing` are located in `src/py_test` .  Pytest can be run by using this command:

```
python -m pytest ./src/py_test
```

# Performance

On my macbook pro 2014 model with 16 GB of memory, [the whole data file](https://drive.google.com/file/d/1fxtTLR_Z5fTO-Y91BnKOQd6J0VC9gPO3/view?usp=sharing) , which contains over 24 million records, was processed in **less than 160 seconds**.  I output of the `cProfile` is located at `./profile_output.txt`. 

## Conclusion

Overall, it is an interesting project and it is also fun to write the whole process in python without using any extra package such as pandas. 


