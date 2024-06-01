import pandas as pd
import numpy as np
import seaborn as sns
from pandas.api.types import is_datetime64_any_dtype
import matplotlib.pyplot as plt
file_path = r"C:\Users\Archana\Downloads\archive\Sample - Superstore.csv"
dataset = pd.read_csv(file_path, encoding='ISO-8859-1')
#print(dataset.head(2))
#print(dataset.isnull().sum()) #for checking any column has any null value or not
#print(dataset['Ship Mode'].value_counts())#find the total number of occurance in each ship mode.
#x=dataset['Ship Mode'].value_counts().index #for making pichart x axis data
#y=dataset['Ship Mode'].value_counts().values #for making piechart y axis data
#plt.figure(figsize=(5,4)) #for making piechart size
#plt.pie(y,labels=x,startangle=60,autopct="%0.2f%%")#for showing labels and percentage
#plt.legend(loc=2)
#plt.show()
#sns.countplot(x="Ship Mode",data=dataset,hue="Category")# to find kis prodcut category ne kesi shiping mode use ki hai.
#plt.show()
#plt.figure(figsize=(5,4))
#sns.countplot(x="Segment",data=dataset)#for checking kis segment se kitne log belong krte h
#plt.show()
#sns.countplot(x="Category",data=dataset)#kis product categpry ki selling sbse jayda ho rhi hai
#plt.show()
#sns.countplot(x="Category",data=dataset[dataset["Category"]=="Office Supplies"],hue="Sub-Category")#category m kis sub category sell kitna h
#plt.show()
#plt.figure(figsize=(6,10))
#sns.countplot(x="Category",data=dataset[dataset["Category"]=="Furniture"],hue="Sub-Category")
#plt.show()
#sns.countplot(x="Category",data=dataset[dataset["Category"]=="Technology"],hue="Sub-Category")
#plt.show()
#if is_datetime64_any_dtype(dataset['Order Date']):#for checking order date is in format of datetime or not
#print("'Order Date' is already in datetime format.")
#dataset['Order Date'] = pd.to_datetime(dataset['Order Date'], errors='coerce')#for converting order date column into time date format
#dataset["Order year"] = dataset['Order Date'].dt.year
#print(dataset['Order year'].value_counts())
#sns.countplot(x="Order year",data=dataset)
#plt.show()
#sns.barplot(x='Category', y="Profit", data=dataset, estimator='sum')#kis category m kitna profit hua h uska sum
#plt.show()
print(dataset['State'].value_counts()[:5])#count of top five state jisme sbse jayda sell hua h








