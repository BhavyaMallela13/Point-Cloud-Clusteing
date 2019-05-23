import laspy
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import MeanShift,estimate_bandwidth

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

bandwidth = estimate_bandwidth(df, quantile=0.1, n_samples=50)

ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
ms.fit(df)
labels = ms.labels_
cluster_centers = ms.cluster_centers_

labels_unique = np.unique(labels)
n_clusters_ = len(labels_unique)

print("number of estimated clusters : %d" % n_clusters_)
plt.scatter(df['X'],df['Y'],c = labels)
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(df[X], df[Y], df[Z],c = labels)
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
# ax.scatter(cluster_centers[:,0], cluster_centers[:,1], cluster_centers[:,2], marker='x', color='red', s=300, linewidth=5, zorder=10)
# plt.show()


