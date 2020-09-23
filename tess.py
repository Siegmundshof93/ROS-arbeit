import csv
import numpy as np
import pandas as pd
import pickle

df = pd.DataFrame({'Date':['2', '4', '5', '6']})


dd = pd.DataFrame({'event':['1', '2', '3', '4', '5','6']})

#data = df.iloc[:,0]
#print(df["Date"][0])
#print(data[2])

#print(data)
result = []
for k in range(len(df)):
    if dd['event'][k] == df["Date"][k]:

        dt[k] = dd[k]
        k += 1

        result.append(dt)

res = pickle.dumps(result)



res1 = pickle.loads(res)

print(res1)
