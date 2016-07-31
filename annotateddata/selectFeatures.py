import numpy as np
import sys
from sklearn.cross_validation import cross_val_score
from sklearn.datasets import make_blobs
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_selection import SelectFromModel
from sklearn.metrics import roc_curve, auc
from sklearn.cross_validation import StratifiedKFold
from scipy import interp
from  matplotlib import pyplot as plt

def getAUC(clf):
	mean_tpr = 0.0
	mean_fpr = np.linspace(0, 1, 100)
	all_tpr = []
	cv = StratifiedKFold(y, n_folds=6)

	for i, (train, test) in enumerate(cv):
	    X_NEW = list()
	    Y_NEW = list()
	    X_TEST = list()
	    Y_TEST = list()
	    for i in train:
		X_NEW.append(X[i])
		Y_NEW.append(y[i])
	    for i in test:
		    X_TEST.append(X[i])
		    Y_TEST.append(y[i])
	    probas_ = clf.fit(X_NEW, Y_NEW).predict_proba(X_TEST)
	    # Compute ROC curve and area the curve
	    fpr, tpr, thresholds = roc_curve(Y_TEST, probas_[:, 1])
	    mean_tpr += interp(mean_fpr, fpr, tpr)
	    mean_tpr[0] = 0.0

	mean_tpr /= len(cv)
	mean_tpr[-1] = 1.0
	mean_auc = auc(mean_fpr, mean_tpr)
	return mean_tpr, mean_fpr,mean_auc

if __name__ == "__main__":
	X=list()
	y=list()

	#id,rumor score, fact score, liscence, defination, like density, dislike density, fav density, comment density
	feature_index = [1,2,5,6,8]
	dataset = sys.argv[1]
	dataset = open(dataset,'r')
	for line in dataset:
		data = line.strip().split(',')
		feature = list()
		for index in feature_index:
			feature.append(data[index])
		X.append(feature)
		y.append(int(data[9]))

	clf = DecisionTreeClassifier(max_depth=None, min_samples_split=1,random_state=0)
	scores = cross_val_score(clf, X, y,cv=10)
	print "DECISION TREE"
	print scores.mean()
	clf = clf.fit(X, y)
	print str(clf.feature_importances_)
	mean_tpr, mean_fpr,mean_auc = getAUC(clf)
	plt.plot(mean_fpr, mean_tpr, 'k--',color=(0.6, 0, 0)
		 ,label='Decision Tree Mean ROC (area = %0.2f)' % mean_auc, lw=2)
	print "========================"

	clf = RandomForestClassifier(n_estimators=10, max_depth=None, min_samples_split=1, random_state=0)
	scores = cross_val_score(clf, X, y,cv=10)
	print "RANDOM FOREST"
	print scores.mean()
	clf = clf.fit(X, y)
	print str(clf.feature_importances_)
	mean_tpr, mean_fpr,mean_auc = getAUC(clf)
	plt.plot(mean_fpr, mean_tpr, 'k--',color=(0.0, 0.0, 0.6)
		 ,label='Random Forest Mean ROC (area = %0.2f)' % mean_auc, lw=2)
	print "========================"

	clf = ExtraTreesClassifier(n_estimators=10, max_depth=None, min_samples_split=1, random_state=0)
	scores = cross_val_score(clf, X, y,cv=10)
	print "EXTREME RANDOM FOREST"
	print scores.mean()
	clf = clf.fit(X, y)
	print str(clf.feature_importances_)
	mean_tpr, mean_fpr,mean_auc = getAUC(clf)
	plt.plot(mean_fpr, mean_tpr, 'k--',color=(0.0, 0.6, 0.0)
		 ,label='Extreme Random Forest Mean ROC (area = %0.2f)' % mean_auc, lw=2)
	print "========================"
	
	plt.plot([0, 1], [0, 1], '--', color=(0.6, 0.6, 0.6), label='Random')
	plt.xlim([-0.05, 1.05])
	plt.ylim([-0.05, 1.05])
	plt.xlabel('False Positive Rate')
	plt.ylabel('True Positive Rate')
	plt.title('Receiver operating characteristic example')
	plt.legend(loc="lower right")
	plt.show()
