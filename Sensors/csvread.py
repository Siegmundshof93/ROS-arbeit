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


"""
file_path = filedialog.askopenfile(initialdir='/home/pvl/ROS/',
title='Select telemetry'
).name #dialog window, for manual telemetry search
"""


df = pd.read_csv("/home/pvl/ROS/decor_result/ROS-arbeit/Sensors/2020.09.17_13.50.18_log.csv", delimiter=';', index_col=False, skiprows=1) # Read csv file



t   = df.iloc[:, 0].values.reshape(-1, 1) # Time, first collumn
telem = df.iloc[:, 42].values.reshape(-1, 1)

#Choosing only rows with the ID683D
telem = pd.DataFrame(telem)
telem.to_csv("/home/pvl/ROS/decor_result/ROS-arbeit/Sensors/ignore_1.csv", index=False)
telem = pd.read_csv("/home/pvl/ROS/decor_result/ROS-arbeit/Sensors/ignore_1.csv", delimiter=' ', skiprows=1)
telem1 = pd.DataFrame({'A': telem.iloc[:,3]})
telem_ID = telem.loc[telem1['A'] == "68"]

#accelerometer

#x axis
accx1 = telem_ID.iloc[:,5].astype(str)
accx2 = telem_ID.iloc[:,6].astype(str)
accx = accx2 + accx1

#y axis
accy1 = telem_ID.iloc[:,7].astype(str)
accy2 = telem_ID.iloc[:,8].astype(str)
accy = accy2 + accy1
#z axis
accz1 = telem_ID.iloc[:,9].astype(str)
accz2 = telem_ID.iloc[:,10].astype(str)
accz = accz2 + accz1



accx = accx.apply(lambda accx: int(accx, 16))
accy = accy.apply(lambda accy: int(accy, 16))
accz = accz.apply(lambda accz: int(accz, 16))

accx = accx * 4 / 32768
accy = accy * 4 / 32768
accz = accz * 4 / 32768



#convertation to human readable time
timeUtc = np.array(t/1000)
time = np.asarray(timeUtc, dtype='datetime64[s]')

dataframe=pd.DataFrame(time)


dataframe.to_csv("sensors_output.csv", index=False)
