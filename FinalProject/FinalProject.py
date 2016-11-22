import pandas
import numpy 
import matplotlib 

#reading the csv file using the pandas library
Data = pandas.read_csv("TrainingSet.csv")

Data.describe()
