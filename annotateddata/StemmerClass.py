from nltk.corpus import stopwords
from nltk.stem.lancaster import LancasterStemmer
class Stemmer:
	def __init__(self):
		self.st = LancasterStemmer()
		self.stop = stopwords.words('english')
	#Provides list of stem words given a line
	def getStemmedCorpus(self,line):
    		stemWords = list()
    		data = line.strip().split(',')
	    	if len(data) < 2:
        		return None
    		stri = ""
    		stri = ' '.join(e for e in data[1].split(" ") if e.isalnum())
    		for i in stri.split(" "):
        		if self.st.stem(i) not in self.stop:
            			stemWords.append(self.st.stem(i))
		return stemWords
