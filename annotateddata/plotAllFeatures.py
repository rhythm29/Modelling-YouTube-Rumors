import sys
from  matplotlib import pyplot as plt
import matplotlib.gridspec as gridspec

#id,rumor score, fact score, liscence, defination, like density, dislike density, fav density, comment density

def plotXY(a,b,ax):
  x_fact,y_fact = [],[] 
  x_rumor,y_rumor = [],[] 
  i = 0
  for v in feature_data[a]:
	 print feature_data[9][i]
	 if feature_data[9][i] == '1':
	   x_rumor.append(v)
	   y_rumor.append(feature_data[b][i])
	 else:
	   x_fact.append(v)
	   y_fact.append(feature_data[b][i])
	 i+=1
  ax.set_ylabel(feature_map[b]);
  ax.set_xlabel(feature_map[a]);
  ax.set_yscale('log')
  ax.set_xscale('log')
  plt.plot(x_fact, y_fact, '.',color='b'
	,label='Correlation of '+feature_map[1], lw=2)
  plt.plot(x_rumor, y_rumor, '.',color='r'
	,label='Correlation of '+feature_map[1]+" with Classes", lw=2)

if __name__=='__main__':
  feature_map = {1:'rumor score',2:'fact scrore',3:'liscense',4:'definition',5:'like ratio',6:'dislike ratio',7:'fav ratio',8:'comment ratio',9:'class label'}
  feature_data = {0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}
  feature_file = sys.argv[1]
  for line in open(feature_file,'r'):
     data = line.strip().split(',')
     i = 0;
     for field in data:
	     feature_data[i].append(field)
	     i+=1
  fig = plt.figure();
  gs = gridspec.GridSpec(1, 1)
  ax = plt.subplot(gs[0, 0])
  plotXY(1,2,ax)
  fig.add_subplot(ax)
  ax = plt.subplot(gs[0, 0])
  plotXY(1,6,ax)
  fig.add_subplot(ax)
  plt.show()
