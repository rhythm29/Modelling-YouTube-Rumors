import sys
from collections import defaultdict
import StemmerClass
import Cleaner
import TFIDF

#id,title,description,tags,date,duration=PT1M4S,isLiscensed,defination,views,like,dislikes,favourite,comments
def preprocessing(StemmedDict,fileName): 
	v = set()
	f = open(fileName,'r')
	for line in f:
		line = line.strip()
		#print line
		lineCleaned = Cleaner.getProcessedData(line,1)
		#print lineCleaned
        	Id = lineCleaned.split('\x01')[0]
		lineStem = StemmerClass.Stemmer()
		if not Id in v:
       			v.add(Id)
			StemmedDict[Id] = lineStem.getStemmedCorpus(lineCleaned)
		

class tfidf:
	def __init__(self,stemmedCorpus):
		self.stemmedCorpus = stemmedCorpus
        def getTF(self):
		return TFIDF.getTF(self.stemmedCorpus)

class DocumentScore:
	def __init__(slef,stemmedCorpus):
		self.stemmedCorpus = stemmedCorpus

def getTotalTFIDF(tf,idf):
	sum = 0.0;
	for word,freq in tf.iteritems():
		if word is not None:
			sum += (freq * idf[word])
	return sum

		
#Create feature now
def createFeature(fileName, docRumourScore,docFactScore,classLabel):
        f = open(fileName,'r')
	rmax = max(docRumourScore.itervalues())
	rmin = min(docRumourScore.itervalues())
	lmax = max(docFactScore.itervalues())
	lmin = min(docFactScore.itervalues())
        for line in f:
                line = line.strip()
                #print line
                lineCleaned = Cleaner.getProcessedData(line,1)
                data = lineCleaned.split('\x01')
		id = data[0]
                rumorScore = docRumourScore[id]
                factScore = docFactScore[id]
		liscence = 0 if data[3] == 'false' else 1
                defination = 0 if data[4] == 'sd' else 1
		views = float(data[5])
                print id+','+str((rumorScore-rmin)/rmax)+','+str((factScore-lmin)/lmax)+','+str(liscence)+','+str(defination)+','+str(float(data[6])/views)+','+str(float(data[7])/views)+','+str(float(data[8])/views)+','+str(float(data[9])/views)+","+str(classLabel)
if __name__ == "__main__":
	factFile = sys.argv[1]
	rumorFile = sys.argv[2]

	rumorStemmedCorpus = defaultdict(list)
	preprocessing(rumorStemmedCorpus,rumorFile)
	#print str(rumorStemmedCorpus)

	factStemmedCorpus = defaultdict(list)
	preprocessing(factStemmedCorpus,factFile)
	#print str(factStemmedCorpus)
	rumour = tfidf(rumorStemmedCorpus);
	tfr  = rumour.getTF()
	fact = tfidf(factStemmedCorpus);
	tff = fact.getTF()

	idf = TFIDF.getIDF(tfr,tff);
	
	totalRumor = getTotalTFIDF(tfr,idf)
	totalFact = getTotalTFIDF(tff,idf)

	#print totalRumor
	#print totalFact
	docRumourScore = defaultdict(float)
	docFactScore = defaultdict(float)
        
        rumorBigger = 0
	factBigger = 0
	allStemmedCorpus = rumorStemmedCorpus.copy()
	allStemmedCorpus.update(factStemmedCorpus)
	for doc,words in allStemmedCorpus.iteritems():
	    if words is not None:	
		sumR = 0.0
		sumF = 0.0
		for word in words:
			if word is not None:
				freqR = tfr[word]
				freqF = tff[word]
				if freqR is None:
					freqR = 0.0
				if freqF is None:
					freqF = 0.0
				sumR += (freqR * idf[word])
				sumF += (freqF * idf[word])
		docRumourScore[doc] = sumR
		docFactScore[doc] = sumF
		#print str(docRumourScore[doc]) +"  ::  "+str(docFactScore[doc])	
		if docRumourScore[doc] > docFactScore[doc]:
			rumorBigger+=1
		else:
			factBigger+=1
	createFeature(rumorFile,docRumourScore,docFactScore,1)
	createFeature(factFile,docRumourScore,docFactScore,0)	
