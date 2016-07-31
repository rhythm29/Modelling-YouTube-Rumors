import nltk
from nltk.tokenize import word_tokenize
from nltk.stem.lancaster import LancasterStemmer
from nltk.corpus import stopwords
import operator
import csv
import random

labels = ['fact','rumour']
stop = stopwords.words('english')
stop.extend([',','0','1'])
st = LancasterStemmer()
#from nltk import bigrams
f = open('desc1.csv')
raw = f.read()
tokens = word_tokenize(raw)
stopTokens = [st.stem(i) for i in tokens if (st.stem(i) not in stop)]

#Create your bigrams
bgs = nltk.bigrams(stopTokens)

#compute frequency distribution for all the bigrams in the text
fdist = nltk.FreqDist(bgs)
corpus = dict()
for k,v in fdist.items():
        corpus[k] = v

sortDict = sorted(corpus.items(),key=operator.itemgetter(1),reverse=True)
#print sortDict

K =500
keys = [i[0] for i in sortDict[:K]]
keys = set(keys)
for k in keys:
    print str(random.randint(0,2000000))+"_w,",
print "class"
with open('desc1.csv', 'rb') as csvfile:
    r = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in r:
        a = row[1].split(" ")
        s = [st.stem(i) for i in a]
        bg = set(nltk.bigrams(s))
        for k in keys:
            if k in bg:
                print "1,",
            else:
                print "0,",
        print labels[int(row[0])]

