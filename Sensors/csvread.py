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

#Choosing only rows with the ID683D
telem1 = pd.DataFrame({'A': df.iloc[:,42]})
telem_ID = df.loc[telem1['A'].str[8] == "8"]

t   = telem_ID.iloc[:, 0].values.reshape(-1, 1) # Time, first collumn
telem = telem_ID.iloc[:, 42].values.reshape(-1, 1)

#convertation to human readable time
timeUtc = np.array(t/1000)
time = np.asarray(timeUtc, dtype='datetime64[s]')

dataframe=pd.DataFrame(time)

dataframe.to_csv("sensors_output.csv", index=False)



telem = pd.DataFrame(telem)
telem.to_csv("/home/pvl/ROS/decor_result/ROS-arbeit/Sensors/ignore_1.csv", index=False)
telem = pd.read_csv("/home/pvl/ROS/decor_result/ROS-arbeit/Sensors/ignore_1.csv", delimiter=' ', skiprows=1)

################################################accelerometer

#x axis
accx1 = telem.iloc[:,5].astype(str)
accx2 = telem.iloc[:,6].astype(str)
accx = accx2 + accx1

#y axis
accy1 = telem.iloc[:,7].astype(str)
accy2 = telem.iloc[:,8].astype(str)
accy = accy2 + accy1
#z axis
accz1 = telem.iloc[:,9].astype(str)
accz2 = telem.iloc[:,10].astype(str)
accz = accz2 + accz1


accx = accx.apply(lambda accx: int(accx, 16))
accy = accy.apply(lambda accy: int(accy, 16))
accz = accz.apply(lambda accz: int(accz, 16))

accx = accx * 4 / 32768
accy = accy * 4 / 32768
accz = accz * 4 / 32768


acx = pd.read_csv("/home/pvl/ROS/decor_result/ROS-arbeit/Sensors/sensors_output.csv")
acx["Accelerometer X axis"] = ""
acx.to_csv("/home/pvl/ROS/decor_result/ROS-arbeit/Sensors/sensors_output.csv", index=False)
acx = pd.read_csv("/home/pvl/ROS/decor_result/ROS-arbeit/Sensors/sensors_output.csv")
acx["Accelerometer X axis"] = accx
acx.to_csv("/home/pvl/ROS/decor_result/ROS-arbeit/Sensors/sensors_output.csv", index=False)

acy = pd.read_csv("/home/pvl/ROS/decor_result/ROS-arbeit/Sensors/sensors_output.csv")
acy["Accelerometer Y axis"] = ""
acy.to_csv("/home/pvl/ROS/decor_result/ROS-arbeit/Sensors/sensors_output.csv", index=False)
acy = pd.read_csv("/home/pvl/ROS/decor_result/ROS-arbeit/Sensors/sensors_output.csv")
acy["Accelerometer Y axis"] = accy
acy.to_csv("/home/pvl/ROS/decor_result/ROS-arbeit/Sensors/sensors_output.csv", index=False)

acz = pd.read_csv("/home/pvl/ROS/decor_result/ROS-arbeit/Sensors/sensors_output.csv")
acz["Accelerometer Z axis"] = ""
acz.to_csv("/home/pvl/ROS/decor_result/ROS-arbeit/Sensors/sensors_output.csv", index=False)
acz = pd.read_csv("/home/pvl/ROS/decor_result/ROS-arbeit/Sensors/sensors_output.csv")
acz["Accelerometer Z axis"] = accz
acz.to_csv("/home/pvl/ROS/decor_result/ROS-arbeit/Sensors/sensors_output.csv", index=False)

##############################################gyro

#x axis
gyrx1 = telem.iloc[:,11].astype(str)
gyrx2 = telem.iloc[:,12].astype(str)
gyrx = gyrx2 + gyrx1
#y axis
gyry1 = telem.iloc[:,13].astype(str)
gyry2 = telem.iloc[:,14].astype(str)
gyry = gyry2 + gyry1
#z axis
gyrz1 = telem.iloc[:,15].astype(str)
gyrz2 = telem.iloc[:,16].astype(str)
gyrz = gyrz2 + gyrz1

gyrx = gyrx.apply(lambda gyrx: int(gyrx, 16))
gyry = gyry.apply(lambda gyry: int(gyry, 16))
gyrz = gyrz.apply(lambda gyrz: int(gyrz, 16))

gyrx = gyrx * 2000 / 32768
gyry = gyry * 2000 / 32768
gyrz = gyrz * 2000 / 32768

gyx = pd.read_csv("/home/pvl/ROS/decor_result/ROS-arbeit/Sensors/sensors_output.csv")
gyx["Gyro X axis"] = ""
gyx.to_csv("/home/pvl/ROS/decor_result/ROS-arbeit/Sensors/sensors_output.csv", index=False)
gyx = pd.read_csv("/home/pvl/ROS/decor_result/ROS-arbeit/Sensors/sensors_output.csv")
gyx["Gyro X axis"] = gyrx
gyx.to_csv("/home/pvl/ROS/decor_result/ROS-arbeit/Sensors/sensors_output.csv", index=False)

gyy = pd.read_csv("/home/pvl/ROS/decor_result/ROS-arbeit/Sensors/sensors_output.csv")
gyy["Gyro Y axis"] = ""
gyy.to_csv("/home/pvl/ROS/decor_result/ROS-arbeit/Sensors/sensors_output.csv", index=False)
gyy = pd.read_csv("/home/pvl/ROS/decor_result/ROS-arbeit/Sensors/sensors_output.csv")
gyy["Gyro Y axis"] = gyry
gyy.to_csv("/home/pvl/ROS/decor_result/ROS-arbeit/Sensors/sensors_output.csv", index=False)

gyz = pd.read_csv("/home/pvl/ROS/decor_result/ROS-arbeit/Sensors/sensors_output.csv")
gyz["Gyro Z axis"] = ""
gyz.to_csv("/home/pvl/ROS/decor_result/ROS-arbeit/Sensors/sensors_output.csv", index=False)
gyz = pd.read_csv("/home/pvl/ROS/decor_result/ROS-arbeit/Sensors/sensors_output.csv")
gyz["Gyro Z axis"] = gyrz
gyz.to_csv("/home/pvl/ROS/decor_result/ROS-arbeit/Sensors/sensors_output.csv", index=False)

#####################################magnetometer

#x axis
magx1 = telem.iloc[:,17].astype(str)
magx2 = telem.iloc[:,18].astype(str)
magx = magx2 + magx1
#y axis
magy1 = telem.iloc[:,19].astype(str)
magy2 = telem.iloc[:,20].astype(str)
magy = magy2 + magy1
#z axis
magz1 = telem.iloc[:,21].astype(str)
magz2 = telem.iloc[:,22].astype(str)

magz = magz2 + magz1



magx = magx.apply(lambda magx: int(magx, 16))
magy = magy.apply(lambda magy: int(magy, 16))
magz = magz.apply(lambda magz: int(magz, 16))

magx = magx * 400 / 32768
magy = magy * 400 / 32768
magz = magz * 400 / 32768

max = pd.read_csv("/home/pvl/ROS/decor_result/ROS-arbeit/Sensors/sensors_output.csv")
max["Magnetometer X axis"] = ""
max.to_csv("/home/pvl/ROS/decor_result/ROS-arbeit/Sensors/sensors_output.csv", index=False)
max = pd.read_csv("/home/pvl/ROS/decor_result/ROS-arbeit/Sensors/sensors_output.csv")
max["Magnetometer X axis"] = magx
max.to_csv("/home/pvl/ROS/decor_result/ROS-arbeit/Sensors/sensors_output.csv", index=False)

may = pd.read_csv("/home/pvl/ROS/decor_result/ROS-arbeit/Sensors/sensors_output.csv")
may["Magnetometer Y axis"] = ""
may.to_csv("/home/pvl/ROS/decor_result/ROS-arbeit/Sensors/sensors_output.csv", index=False)
may = pd.read_csv("/home/pvl/ROS/decor_result/ROS-arbeit/Sensors/sensors_output.csv")
may["Magnetometer Y axis"] = magy
may.to_csv("/home/pvl/ROS/decor_result/ROS-arbeit/Sensors/sensors_output.csv", index=False)

maz = pd.read_csv("/home/pvl/ROS/decor_result/ROS-arbeit/Sensors/sensors_output.csv")
maz["Magnetometer Z axis"] = ""
maz.to_csv("/home/pvl/ROS/decor_result/ROS-arbeit/Sensors/sensors_output.csv", index=False)
maz = pd.read_csv("/home/pvl/ROS/decor_result/ROS-arbeit/Sensors/sensors_output.csv")
maz["Magnetometer Z axis"] = magz
maz.to_csv("/home/pvl/ROS/decor_result/ROS-arbeit/Sensors/sensors_output.csv", index=False)
