"""
Demo of the new boxplot functionality
"""

import numpy as np
import matplotlib.pyplot as plt
import sys

fav_rumour = []
like_rumour = []
dislike_rumour = []
comment_rumour = []
views_rumour = []

fav_fact = []
like_fact = []
dislike_fact = []
comment_fact = []
views_fact = []

for line in sys.stdin:    
    data = line.strip().split('');
    if(len(data)==15):
        view = int(data[8].split('=')[1])
        if(not (view == 0)):
            if(int(data[14])==0):
                #Fact
                like_fact.append(float(data[9].split('=')[1])/view)
                dislike_fact.append(float(data[10].split('=')[1])/view)
                fav_fact.append(float(data[11].split('=')[1])/view)
                comment_fact.append(float(data[12].split('=')[1])/view)
                views_fact.append(view)
            elif(int(data[14])==1):
                #rumour
                like_rumour.append(float(data[9].split('=')[1])/view)
                dislike_rumour.append(float(data[10].split('=')[1])/view)
                fav_rumour.append(float(data[11].split('=')[1])/view)
                comment_rumour.append(float(data[12].split('=')[1])/view)
                views_rumour.append(view)

#print str(like_fact)
#print str(like_rumour)
# fake data
#np.random.seed(786)
#data = np.array([[123,34,125,64,234,532,13,43],[23,56,889,45,67,98,477,123]])
data_comment = (np.array(comment_fact),np.array(comment_rumour))
data_like = (np.array(like_fact),np.array(like_rumour))
data_dislike = (np.array(dislike_fact),np.array(dislike_rumour))
data_fav = (np.array(fav_fact),np.array(fav_rumour))
data_fav = (np.array(fav_fact),np.array(fav_rumour))
data_view = (np.array(views_fact),np.array(views_rumour))
#data = data.transpose();
#print str(data1.shape)
labels = ['fact','Rumour']
fs = 12 # fontsize

# demonstrate how to toggle the display of different elements:
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(6,6))
axes[0, 0].boxplot(data_like, labels=labels, showfliers=False)
axes[0, 0].set_title('Likes', fontsize=fs)

axes[0, 1].boxplot(data_dislike, labels=labels, showfliers=False)
axes[0, 1].set_title('Dislikes', fontsize=fs)

axes[1, 1].boxplot(data_view, labels=labels, showfliers=False)
axes[1, 1].set_title('Views', fontsize=fs)

axes[1, 0].boxplot(data_comment, labels=labels, showfliers=False)
axes[1, 0].set_title('Comments', fontsize=fs)
'''
for ax in axes.flatten():
    ax.set_yscale('log')
    ax.set_yticklabels([])
'''
fig.subplots_adjust(hspace=0.4)
plt.show()
