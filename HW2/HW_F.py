from sklearn.ensemble import RandomForestClassifier
from sklearn.cluster import KMeans, Birch, AgglomerativeClustering, DBSCAN
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import time



# Loads data from wine.data
def loadData():
	inputData = open("wine.data", "r")
	X = list()
	Y = list()
	for line in inputData:
		addedRow = [float(x) for x in line.split(',')]
		X.append(addedRow[1:])
		Y.append(addedRow[0])
	inputData.close()
	return X,Y

# Performs a RandomForestRegression on the wine data set
def getFeaturesFromTree(names):
	data, target = loadData()
	#rf = RandomForestClassifier(n_estimators=120)
	rf = RandomForestClassifier(n_estimators = 100, random_state = 1)
	rf.fit(data,target)

	results = sorted(zip(map(lambda x: round(x, 4), rf.feature_importances_), names), 
	             reverse=True)
	return data, results
def reduceToThreeAttributes(X, results, names):
	x = results[0][1]
	y = results[1][1]
	z = results[2][1]
	pos = 0
	for name in names:
		if x == name:
			x = pos
		elif y == name:
			y = pos
		elif z == name:
			z = pos
		pos = pos + 1
	data = list()
	for row in X:
		# Color intensity [-4], Proline [-1], OD280/OD315 of diluted wines [-2] 
		data.append([row[x], row[y], row[z]])
	return np.array(data), [names[x],names[y],names[z]]

def completeKMeansEstimation(data, axisLabels):
	estimators = {'KMeans_one_cluster' : KMeans(n_clusters = 1, init='random'),
					'KMeans_three_cluster' : KMeans(n_clusters=3, init='random'),
					'KMeans_five_cluster' : KMeans(n_clusters=5, init='random'),
					'KMeans_eleven_cluster' : KMeans(n_clusters=11, init='random')}
	plotData(data, estimators, axisLabels,1)
def completeBirchEstimation(data, axisLabels):
	estimators = {'Birch_one_cluster' : Birch(n_clusters = 1),
					'Birch_three_cluster' : Birch(n_clusters=3),
					'Birch_five_cluster' : Birch(n_clusters=5),
					'Birch_eleven_cluster' : Birch(n_clusters=11)}
	plotData(data, estimators, axisLabels,5)

def completeAggloEstimation(data, axisLabels):
	estimators = {'Agglo_one_cluster' : AgglomerativeClustering(n_clusters = 1),
					'Agglo_three_cluster' : AgglomerativeClustering(n_clusters=3),
					'Agglo_five_cluster' : AgglomerativeClustering(n_clusters=5),
					'Agglo_eleven_cluster' : AgglomerativeClustering(n_clusters=11)}
	plotData(data, estimators, axisLabels, 9)

def completeDBSCAN(data, axisLabels):
	estimators = {'DBSCAN' : DBSCAN(eps = 35, min_samples = 5)}
	plotData(data, estimators, axisLabels, 13)

def plotData(data, estimators, axisLabels, figNum):
	
	for name, est in estimators.items():
		fig = plt.figure(figNum, figsize=(4,3))
		plt.clf()
		ax = Axes3D(fig, rect = [0,0,0.95,1], elev = 48, azim = 134)
		start_time = time.time()
		est.fit(data)
		print("Time taken for "+name+": "+str(1000*(time.time() - start_time))+"ms")
		labels = est.labels_
		ax.scatter(data[:,0], data[:,1], data[:,2], c=labels.astype(np.float))
		ax.w_xaxis.set_ticklabels([])
		ax.w_yaxis.set_ticklabels([])
		ax.w_zaxis.set_ticklabels([])
		ax.set_xlabel(axisLabels[0])
		ax.set_ylabel(axisLabels[1])
		ax.set_zlabel(axisLabels[2])
		figNum = figNum + 1


names = ['Alcohol','Malic acid','Ash','Alcalinity of ash','Magnesium','Total phenols','Flavanoids','Nonflavanoid phenols','Proanthocyanins','Color intensity','Hue','OD280/OD315 of diluted wines','Proline']
data, results = getFeaturesFromTree(names)
data, axisLabels = reduceToThreeAttributes(data, results, names)
print("Features sorted by their score:"+str(axisLabels))
completeKMeansEstimation(data, axisLabels)
completeBirchEstimation(data, axisLabels)
completeAggloEstimation(data, axisLabels)
completeDBSCAN(data, axisLabels)
plt.show()
