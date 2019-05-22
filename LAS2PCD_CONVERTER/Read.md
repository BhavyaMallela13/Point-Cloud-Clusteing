You need to just run above .cpp file to convert .las file into .pcd.

First create a LAS2PCD_CONVERTER folder and place this .cpp file and also create another file which is CMakeLists.txt or directly you can clone it.

For this you need to have PCL installed on your pc.Just follow the steps below..

Open Terminal and just copy paste one by one..

...$ sudo apt install -y git cmake

...$ sudo apt install -y libpcl-dev liblas-dev liblas-c-dev

...$ git clone https://github.com/BhavyaMallela13/Point-Cloud-Clustering.git

...$ cd Point-Cloud-Clustering/LAS2PCD_CONVERTER/

...$ cmake .

...$ make

Place the .las file you want to convert in the same LAS2PCD_CONVERTER folder and then paste below statement in the terminal and you're done.

...$ ./LAS2PCD Buildings.las Buildings.pcd




