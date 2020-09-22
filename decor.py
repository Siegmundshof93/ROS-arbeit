#import libraries
import csv
import numpy as np
import pandas as pd
import re
import pickle

#read the csv file
df = pd.read_csv("/home/pvl/ROS/decor_result/ROS-arbeit/data.csv", delimiter=":", engine="python")

# extracting the decor measurements for four cameras "#### #### #### #### "

result = [] #creatting a buffer
for i in range(len(df)): # making a for loop to ask only for odd line
        if i%2 == 0: #odd line
            t = str(df.iloc[i, 1])[:20] #convert int to string and delete last 20 caracters
            t = t.split(" ") # split into " " into columnns
            dt = t[1:5] #delete the first (empty) column

    #using the pickle library to take measurements from for loop and save it into the variable
            result.append(dt)

res = pickle.dumps(result)



res1 = pickle.loads(res) #take a value

#save into the data1.csv

np.savetxt('data1.csv', (res1), fmt='%s')

#give the "names" for columns
colnames={' ', '  ', '   ', '    '}

#read the csv file as string
df1 = pd.read_csv("/home/pvl/ROS/decor_result/ROS-arbeit/data1.csv", dtype = str, names=colnames, delimiter=" ")

#values of the columns
x1 = df1.iloc[:, 0]
x2 = df1.iloc[:, 1]
x3 = df1.iloc[:, 2]
x4 = df1.iloc[:, 3]


#first column
x11 = x1.str[:2] #MSB
x12 = x1.str[2:4] #LSB

#second column
x21 = x2.str[:2] #MSB
x22 = x2.str[2:4] #LSB

#third column
x31 = x3.str[:2] #MSB
x32 = x3.str[2:4] #LSB

#fourth column
x41 = x4.str[:2] #MSB
x42 = x4.str[2:4] #LSB

#merge LSB and MSB
First_value = x12 + x11
Second_value = x22 + x21
Third_value = x32 + x31
Fourth_value = x42 + x41

#convert hex 2 int
First_value = First_value.apply(lambda First_value: int(First_value, 16))
Second_value = Second_value.apply(lambda Second_value: int(Second_value, 16))
Third_value = Third_value.apply(lambda Third_value: int(Third_value, 16))
Fourth_value = Fourth_value.apply(lambda Fourth_value: int(Fourth_value, 16))


df_first = pd.read_csv("/home/pvl/ROS/decor_result/ROS-arbeit/data_output.csv")
df_first["Value of the first camera"] = ""
df_first.to_csv("/home/pvl/ROS/decor_result/ROS-arbeit/data_output.csv", index=False)
df_first = pd.read_csv("/home/pvl/ROS/decor_result/ROS-arbeit/data_output.csv")
df_first["Value of the first camera"] = First_value
df_first.to_csv("/home/pvl/ROS/decor_result/ROS-arbeit/data_output.csv", index=False)


df_second = pd.read_csv("/home/pvl/ROS/decor_result/ROS-arbeit/data_output.csv")
df_second["Value of the second camera"] = ""
df_second.to_csv("/home/pvl/ROS/decor_result/ROS-arbeit/data_output.csv", index=False)
df_second = pd.read_csv("/home/pvl/ROS/decor_result/ROS-arbeit/data_output.csv")
df_second["Value of the second camera"] = Second_value
df_second.to_csv("/home/pvl/ROS/decor_result/ROS-arbeit/data_output.csv", index=False)

df_third = pd.read_csv("/home/pvl/ROS/decor_result/ROS-arbeit/data_output.csv")
df_third["Value of the third camera"] = ""
df_third.to_csv("/home/pvl/ROS/decor_result/ROS-arbeit/data_output.csv", index=False)
df_third = pd.read_csv("/home/pvl/ROS/decor_result/ROS-arbeit/data_output.csv")
df_third["Value of the third camera"] = Third_value
df_third.to_csv("/home/pvl/ROS/decor_result/ROS-arbeit/data_output.csv", index=False)

df_fourth = pd.read_csv("/home/pvl/ROS/decor_result/ROS-arbeit/data_output.csv")
df_fourth["Value of the fourth camera"] = ""
df_fourth.to_csv("/home/pvl/ROS/decor_result/ROS-arbeit/data_output.csv", index=False)
df_fourth = pd.read_csv("/home/pvl/ROS/decor_result/ROS-arbeit/data_output.csv")
df_fourth["Value of the fourth camera"] = Fourth_value
df_fourth.to_csv("/home/pvl/ROS/decor_result/ROS-arbeit/data_output.csv", index=False)
