#Written by Nathan A-M =^)
#Python files used to create plots in presentation 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
sns.set()
from matplotlib.font_manager import FontProperties

folder = r".\graphs\\"

#normalized function 
def normalize(raw):
  return [float(i)/max(raw) for i in raw]

#Date from test results
ALT2 = [91422.15236,	73653.31205, 1724666.044	,399887.0205,	65696.33485,	81618.78102]
ALT1 = [1426836.817,	1353931.506, 497416.386	,1542252.582,	2168429.192,	1974183.246]
PQ = [4669.348621,	51.67396791, 4669.348621	,4669.348621,	1.27E-24,	4669.348621]
HD_PQ = [4669.348621,	51.67396791, 4669.348621	,4669.348621,	1.27E-24,	4669.348621]
HD = [4301656.913,	4772712.943, 497416.386	,2136611.714,	4438943.836,	4438943.836]
labels = ['$BB$',	'$Bitmovin$', '$Bitmovin_{\ PQ}$',	'$Dash$',	'$HYB$',	'$HYB_{\ PQ}$']
leg = ['High Def', 'High Def Param but Poor Bandwidth','Poor quality','Soft Alternating','Hard Alternating']
labels2 = ['HD','HD/PQ','PQ','ALT (Soft)','ALT (Hard)']
leg2 = labels

#normalize test results as score scale has a large range
nALT2 =normalize(ALT2)
nALT1 =normalize(ALT1)
nPQ =normalize(PQ)
nHD_PQ =normalize(HD_PQ)
nHD =normalize(HD)

#get each algorithm performance 
matrix=np.array([nHD, nHD_PQ, nPQ, nALT1, nALT2 ]).T
BB = matrix[0].tolist()
Bitmovin = matrix[1].tolist()
BitmovinPQ=matrix[2].tolist()
DASH = matrix[3].tolist()
HYB_L = matrix[4].tolist()
HYB_S = matrix[5].tolist()

x = np.arange(len(labels2))  #get placement for labels 
w = .13 #width, decides graph weight and how far apart they are 
fig, ax = plt.subplots() #create create plot frame

#bar positions 
ax.bar(x-5*w/2,BB,width=w, label=leg2[0])
ax.bar(x-3*w/2,Bitmovin,width=w, label=leg2[1])
ax.bar(x-1*w/2, BitmovinPQ, width=w, label=leg2[2])
ax.bar(x+1*w/2,DASH,width=w, label=leg2[3])
ax.bar(x+3*w/2,HYB_L,width=w, label=leg2[4])
ax.bar(x+5*w/2,HYB_S,width=w, label=leg2[5])

#formating and details
ax.set_ylabel('Normalized QoE Scores')
ax.set_xlabel('ABR Tests')
ax.set_title('Normalized Test Performance of Various ABR Algorithms')
ax.set_xticks(x)
ax.set_xticklabels(labels2)
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), title = 'ABR Algorithms')
fig.set_size_inches(14.5, 5.5)
fig.tight_layout()
fig.patch.set_facecolor('w') #white background

plt.savefig(folder+'Scores_per_test_norm')


#take sum of normed scored
sBB = sum(matrix[0].tolist())
sBitmovin = sum(matrix[1].tolist())
sBitmovinPQ = sum(matrix[2].tolist())
sDASH = sum(matrix[3].tolist())
sHYB_L = sum(matrix[4].tolist())
sHYB_S = sum(matrix[5].tolist())

y =[sBB, sBitmovin, sBitmovinPQ, sDASH, sHYB_L, sHYB_S]
x = np.arange(len(labels)) #get placement for labels 
w = .4 #width, decides graph weight and how far apart they are 

fig, ax = plt.subplots() #create create plot frame

#set each plot color to match previous plot
color=['#4C72B0', '#DD8452', '#55A868', '#C44E52', '#8172B3', '#937860']
ax.bar(x,y,width=w, color = color) #plot

#formating and details
ax.set_ylabel('Total Normalized QoE Scores')
ax.set_xlabel('ABR Algorithms')
ax.set_title('Total Normalized Test Performance of Various ABR Algorithms')
ax.set_xticks(x) 
ax.set_xticklabels(labels,rotation=45, horizontalalignment='right')#set labels
ax.axes.get_xaxis().set_visible(True) 
fig.tight_layout()
fig.patch.set_facecolor('w') #white background


plt.savefig(folder+'Total_Scores_per_test_norm')