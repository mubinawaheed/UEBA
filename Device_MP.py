import pandas as pd
import numpy as np
import stumpy as sp
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


## Group by Date


data=pd.read_csv('user1.csv',index_col=0)
data['date'] = pd.to_datetime(data['date_'])
data=data.set_index(data['date'],drop=True)
# data.head()
data=data.drop(['date_','date'],axis=1)
data['freq']=data['id']
data=data.drop('id',axis=1)
#data.head()

figsize=(20,7)

data['freq']=data['freq'].astype(np.float64)
smp=sp.stump(data['freq'].values,30)
# smp
mp=np.argsort(smp[:,0])#return sorted indices 
# smp[:,0]
# mp
motifs=[]
for i in range(5):
    motif=np.argsort(smp[:,0])[i]#smp[first_row:last_row,column_no]
    motifs.append(motif)
# motifs
neighbors=[]
for motif in motifs:
    neighbors.append(smp[motif,1])
# neighbors
fig, axes=plt.subplots(2,figsize=figsize,sharex=True)
fig.suptitle('Motif Discovery in Device Data(Monthly)')
axes[0].plot(data['freq'].values)
axes[0].set_ylabel('Device Data')
axes[1].set_ylabel('Matrix Profile')
axes[1].set_xlabel('Time')



for i in range(5):
    rect = Rectangle((motifs[i], 0), 30, 10, facecolor='lightgrey')
    axes[0].add_patch(rect)
    rect = Rectangle((neighbors[i], 0), 30, 10, facecolor='lightgrey')
    axes[0].add_patch(rect)
    axes[1].axvline(x=motifs[i], linestyle="dashed",color='red')
    axes[1].axvline(x=neighbors[i], linestyle="dashed",color='red')
    
axes[1].plot(smp[:, 0])
plt.savefig('motifs_date.png')

# axes[1].plot(smp[:,0])
discords=[]
for i in range(1,6):
    discord=np.argsort(smp[:,0])[-i]#smp[first_row:last_row,column_no]
    discords.append(discord)
# i=0 
# np.argsort(smp[:,0])[-i]
# discords
# d_neighbors=[]
# for discord in discord:
#     d_neighbors.append(smp[discord,1])
# smp[discords,1]
fig2, axes=plt.subplots(2,figsize=figsize,sharex=True)
fig2.suptitle('Anomalies Discovery in Device Data(Monthly)')
axes[0].plot(data['freq'].values)
axes[0].set_ylabel('Device Data')
axes[1].set_ylabel('Matrix Profile')
axes[1].set_xlabel('Time')



for i in range(5):
    rect = Rectangle((discords[i], 0), 30, 10, facecolor='lightgrey')
    axes[0].add_patch(rect)
    
    axes[1].axvline(x=discords[i],linestyle="dotted",color='red',marker='o') 
axes[1].plot(smp[:, 0])
plt.savefig('discord_date.png')


##                      Group by Time
data_hour=pd.read_csv('user1_device_hour.csv',index_col=0)
# hour['hour']=hour['date']
# hour.drop('date',axis=1)
# hour['date']=hour['level_0']
# hour.drop('level_0',axis=1,inplace=True)
# hour.to_csv('user1_device_hour.csv')
# data_hour

data_hour=data_hour.set_index(['date_','hour']).sort_index()
# data_hour.reset_index()

# data_hour




data_hour['freq']=data_hour['freq'].astype(np.float64)
m=8*7
smp=sp.stump(data_hour['freq'].values,m)
# smp
mp=np.argsort(smp[:,0])#return sorted indices 
smp[:,0]
# mp
motifs=[]
for i in range(5):
    motif=np.argsort(smp[:,0])[i]#smp[first_row:last_row,column_no]
    motifs.append(motif)
# motifs
neighbors=[]
for motif in motifs:
    neighbors.append(smp[motif,1])
neighbors
fig, axes=plt.subplots(2,figsize=figsize,sharex=True)
fig.suptitle('Motif Discovery in Device Data(Weekly)', fontsize=30)
axes[0].plot(data_hour['freq'].values)
axes[0].set_ylabel('Device Data')
axes[1].set_ylabel('Matrix Profile')
axes[1].set_xlabel('Time')



for i in range(5):
    rect = Rectangle((motifs[i], 0), m, 10, facecolor='lightgrey')
    axes[0].add_patch(rect)
    rect = Rectangle((neighbors[i], 0), m, 10, facecolor='lightgrey')
    axes[0].add_patch(rect)
    axes[1].axvline(x=motifs[i], linestyle="dashed",color='red')
    axes[1].axvline(x=neighbors[i], linestyle="dashed",color='red')
    
axes[1].plot(smp[:, 0])
plt.savefig('motifs_hour')

# axes[1].plot(smp[:,0])
discords=[]
for i in range(1,6):
    discord=np.argsort(smp[:,0])[-i]#smp[first_row:last_row,column_no]
    discords.append(discord)
# i=0 
# np.argsort(smp[:,0])[-i]
# discords
# d_neighbors=[]
# for discord in discord:
#     d_neighbors.append(smp[discord,0])
# smp[discords,1]
fig2, axes=plt.subplots(2,figsize=figsize,sharex=True)
fig2.suptitle('Anomalies Discovery in Device Data(Weekly)', fontsize=30)
axes[0].plot(data_hour['freq'].values)
axes[0].set_ylabel('Device Data',fontsize=20)
axes[1].set_ylabel('Matrix Profile',fontsize=20)
axes[1].set_xlabel('Time',fontsize=20)



for i in range(5):
    # print(discords[i])
    rect = Rectangle((discords[i], 0), m, 10, facecolor='lightgrey')
    axes[0].add_patch(rect)
    
    axes[1].axvline(x=discords[i],linestyle="dotted",color='red',marker='o') 
    
axes[1].plot(smp[:, 0])
plt.savefig('discord_hour.png')


# import matrixprofile as mp
# mph=mp.compute(data_hour['freq'].values,8*7)
# mp.visualize(mph)
# mp.visualize(mp.discover.motifs(mph))
# mp.visualize(mp.discover.discords(mph))
# mp.analyze(data_hour['freq'].values)
