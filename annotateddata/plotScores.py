import matplotlib.pyplot as plt
import sys

plt.figure(figsize=(1, 2))
File = sys.argv[1]
f = open(File,'r')
X_rumor = list()
Y_rumor = list()
X_fact = list()
Y_fact = list()
count = 0
for line in f:
	if count == 0:
		count+=1
		continue;
	data = line.strip().split(',')
	if data[9]=='1':
		#rumor
		X_rumor.append(float(data[2])) #fact score for rumor
		Y_rumor.append(float(data[1]))# rumor score
	else:
		#Fact
		X_fact.append(float(data[2]))
		Y_fact.append(float(data[1]))
#plt.subplot(321)
plt.scatter(X_fact,Y_fact,marker='o')
#plt.subplot(786)
plt.scatter(X_rumor,Y_rumor,marker='x')
plt.show()
