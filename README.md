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
numpy==1.15.0
pandas==0.23.3
pluggy==0.7.1
py==1.5.4
pytest==3.7.1
python-dateutil==2.7.3
pytz==2018.5
six==1.11.0
```

## Installation

**First**, clone the repository.

```
git clone https://github.com/thoo/Pharmacy_Thein
cd Pharmacy_Thein
```

**Second (if you want to use `virtualenv` otherwise skip this step.)**,

* With `virtualenv`, 

  ``` virtualenv -p python3 venv
  virtualenv -p python3 venv
  source venv/bin/activate
  ```

**Finally**, we can install all the required packages.

``` pip 
pip install -r src/requirements.txt
```

## Usage

First, you can check everything is woking by running `./run.sh` .  The script for this project is located in `src` directory. So you can also run your data file using:

```
python ./src/pharmacy_counting.py \
  				-i your_input_file_path \
  				-o your_output_file_path
```

## Details of Implementation

First, the columns `id,drug_name,drug_cost` of  the input data file  is loaded into the memory as a `pandas` dataframe. To save the memory usage, I only selected the necessary columns for data processing.  

This is a real-world data and therefore, I have a function to rigorously clean the data. After that I do count uniquely `id`  for each `drug_name` and also sum all the `drug_cost` for each `drug_name`.  



All the functions mentioned aboved are located in `src/functions.py` . Here is the summary of each function:

* **read_csv** : *Read selected columns ( 'id','drug_name', and 'drug_cost' ) from a csv file to memory. Make sure 'drug_cost' is in float data type*.

* **clean_data** : *Clean data by removing typos and misplaced strings.*

* **process_fun** : *This function will return drug name, total drug cost and total number of prescribers from input data files in descending order by 'total_cost' followed by 'drug_name'*.

* **make_outputfolder** : *Make sure that the output foler exists and if it doesn't, create an folder named 'output'*.

## Unit Testing

I use `pytest` for unit testing. All the files related to `unit testing` are located in `src/py_test` .  Pytest can be run by using this command:

```
python -m pytest ./src/py_test
```

# Performance

All the performance related processes are done on the sample datasets and the program is run on macbook pro 2014 model with 16 GB of memory. Building a social network graph takes about 3 seconds and the analysis takes about 6 seconds. UltraJSON gives 30% speed boost compared to the standard json library from python. The output of the profile on Some of the `if-else` statements are switched to dictionary comprehension to gain some performances. During the whole process, only a part of `stream_log.json` is on the memory and its size can be controlled by setting `-z` parameter. The default is 50,000. So this program is very scalable. 

If I can load all json files to memory, there will definitely be an improvement on performance. However, it will have limitation on scalability. 

I also experimented with `pandas and hdf5`. The `batch_log.json` contains multiple objects instead of a single line. Therefore, the read-out with `pandas.DataFrame.read_json` is slower than `ujson`.  If we do more than just finding the mean and standard deviation, it would be a better option to use `pandas dataframe with hdf5`. In this case, the query file format for `batch_log.json` and `stream_log.json` might be changed to be suitable for `pandas` dataframe. Right now depending on `event`, the keys of the transition is different. For example, `event=purchase` will not have `id1` and `id2` key and so on. 

Currently, most of the time on my program is spent on reading and writing files. Instead of waiting the script to finish, I design to update any anomaly transition as soon as possible. 

## Conclusion

Overall, it is an interesting and fundamental project which is very applicable to our daily life. I have written a scalable program with real time update to `flagged_purchases.json`. I wish I have more control over how the data is collected.  Moreover, if I can load all the data to the system memory, the script will be a lot simplier and readable than it is now.
