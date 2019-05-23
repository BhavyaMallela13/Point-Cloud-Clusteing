import laspy
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans

inFile = laspy.file.File("Buildings_sampled.las",mode = 'r')

print('\n')

for i in range(0,len(inFile.points)):
	list(inFile.points[i])
       
l = []

for i in range(0,len(inFile.points)):
	new = list(inFile.points[i][0])
	l.append(new)


df = pd.DataFrame(l,columns = ['X','Y','Z','intensity','return_number','number_of_returns','point_classification_values','R','G','B','GPS_time','scan_angle','scan_direction'])
#print(df)


kmeans = KMeans(n_clusters = 140)
kmeans.fit(df)
labels = kmeans.predict(df)
centroids = kmeans.cluster_centers_


plt.scatter(df['X'],df['Y'],c = labels,s = 0.01)
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

# threedee = plt.figure().gca(projection='3d')
# threedee.scatter(df.X, df.Y, df.Z,c = labels)
# threedee.set_xlabel('X')
# threedee.set_ylabel('Y')
# threedee.set_zlabel('Z')
# plt.show()

















