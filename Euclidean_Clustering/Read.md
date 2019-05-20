This euclidean clustering is done to seperate out the buildings.

To run this just follow the below steps..

...$ git clone https://github.com/BhavyaMallela13/Point-Cloud-Clustering.git

...$ cd Point-Cloud-CLustering//Euclidean_Clustering/

...$ cmake .

...$ make

...$ ./cluster_extraction

Then it will create all the clusters in the .pcd file format in the same folder.You can view them by using

...$ pcl_viewer cloud_cluster_0.pcd
