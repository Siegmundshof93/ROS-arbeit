import tkinter as tk
import csv
import numpy as np
import pandas as pd
import numpy as np
import time
import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from sklearn.linear_model import LinearRegression
from tkinter import filedialog
from tkinter import simpledialog
from scipy.signal import lfilter
import sys
import pickle



file_path = filedialog.askopenfile(initialdir='/home/pvl/ROS/',
title='Select telemetry'
).name #dialog window, for manual telemetry search



df = pd.read_csv("/home/pvl/ROS/decor_result/ROS-arbeit/Sensors/2020.09.17_13.50.18_log.csv", delimiter=';', index_col=False, skiprows=1) # Read csv file



t   = df.iloc[:, 0].values.reshape(-1, 1) # Time, first collumn
telem = df.iloc[:, 42].values.reshape(-1, 1)

telem = pd.DataFrame(telem)


telem.to_csv("/home/pvl/ROS/decor_result/ROS-arbeit/Sensors/ignore_1.csv", index=False)



telem = pd.read_csv("/home/pvl/ROS/decor_result/ROS-arbeit/Sensors/ignore_1.csv", delimiter=' ', skiprows=1)

telem1 = pd.DataFrame({'A': telem.iloc[:,3]})
telem_ID =telem.loc[telem1['A'] == "68"]


#telem_ID.to_csv("/home/pvl/ROS/decor_result/ROS-arbeit/Sensors/ignore_2.csv", index=False)
#print(telem)


#convertation to human readable time
timeUtc = np.array(t/1000)
time = np.asarray(timeUtc, dtype='datetime64[s]')

dataframe=pd.DataFrame(time)


dataframe.to_csv("sensors_output.csv", index=False)
