#print("start")
import csv
import numpy as np
import pandas as pd
import numpy as np
import re
import pickle


df = pd.read_csv("/home/pvl/ROS/decor_result/data.csv", delimiter=":", engine="python")

result = []
for i in range(len(df)):
        if i%2 == 0:
            t = str(df.iloc[i, 1])[:20]
            t = t.split(" ")
            dt = t[1:5]

            result.append(dt)

res = pickle.dumps(result)



res1 = pickle.loads(res)

#res1.rename(columns={"A": "a", "B": "c"})



#data= res1.str.split( n = 1, expand = True)

#   print(res1)



np.savetxt('data1.csv', (res1), fmt='%s')

colnames={' ', '  ', '   ', '    '}


df1 = pd.read_csv("/home/pvl/ROS/decor_result/data1.csv", dtype = str, names=colnames, delimiter=" ")

#df1 = df1.astype(object)

t   = df1.iloc[:, 2]


print(df1)
