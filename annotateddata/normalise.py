import sys
import csv
from collections import defaultdict
import operator
from nltk.corpus import stopwords
from nltk.stem.lancaster import LancasterStemmer
st = LancasterStemmer()
k = 500
labels = ['fact','rumour']
corpus = defaultdict(int)
stop = stopwords.words('english')

for line in sys.stdin:
    data = line.strip().split(',')
    if len(data) < 2:
        continue
    stri = ""
    stri = ' '.join(e for e in data[1].split(" ") if e.isalnum())
    for i in stri.split(" "):
        if st.stem(i) not in stop:
            corpus[st.stem(i)]+=1

sortDict = sorted(corpus.items(),key=operator.itemgetter(1),reverse=True)
keys = [i[0] for i in sortDict[:k]]
keys = set(keys)
for k in keys:
    print k+"_w,",
print ""
with open('desc1.csv', 'rb') as csvfile:
    r = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in r:
        a = row[1].split(" ")
        s = set([st.stem(i) for i in a])
        for k in keys:
            if k in s:
                print "1,",
            else: 
                print "0,",
        print labels[int(row[0])]
