import numpy as np
import math

#I used this file to generate random chunk sizes for the manifest, WIP
low = np.random.normal(50000 / 8,5000/ 8,30)
med = np.random.normal(100000/ 8,10000/ 8,30)
high = np.random.normal(500000/ 8,50000/ 8,30)

cum = []
finalstr = ""
num = 0
for i in range(len(low)):

    cum.append((low,med,high))

    finalstr += '"' + str(num) + '"' + ' : [\n' + str(math.floor(low[i])) + ",\n" + str(math.floor(med[i])) + ",\n" + str(math.floor(high[i])) + "\n],\n\n"

    num += 1
print(finalstr)