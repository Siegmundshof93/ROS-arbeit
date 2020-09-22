
import csv
import numpy as np
import pandas as pd


colnames=['Time']

df = pd.read_csv("/home/pvl/ROS/decor_result/ROS-arbeit/time_decor.csv", names=colnames, header=None)

#df["Time"] = df

df['Time'] = df['Time'].astype(str).str[24:]
df['Time'] = df['Time'].astype(str).str[:-75]


df.to_csv("/home/pvl/ROS/decor_result/ROS-arbeit/data_output.csv", index=False)
