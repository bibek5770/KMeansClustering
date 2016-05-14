#############################
# Bibek Gautam              #
# K-Means Clustering        #
# CMPS:470                  #
############################

# Upper bound of max iteration taken from http://cseweb.ucsd.edu/~avattani/papers/kmeans.pdf
# http://www.saedsayad.com/clustering_kmeans.htm

from KMeansCluster import Cluster as ClusterClass
from itertools import islice
from inputoutput import InputOutputOperation

inputfile = raw_input(
    "Enter the fileName to learn from:\n1. i.txt(1-D attribute)\n2. in.txt(2-d Attributes)\n3. irisData.txt(3-d attributes)"
    "\n\tOr Enter Full Path of the file with attributes of any dimesion\nNote: Max iteration is set as n^(kd) where n=num of examples,"
    " k= clusters, d= dimensions.\n=>")
#read the input file
readerWriter=InputOutputOperation(inputfile)
data_Set, Num_Examples, Num_Clusters, maxiteration=readerWriter.input()
ClusterClass.data_set = data_Set

# Kmeans algorithm
initialPoint = list(islice(data_Set.keys(),Num_Clusters))
clusters = [ClusterClass([p]) for p in initialPoint]# initialize the clusters
check=True
maxiterationcheck = 0
while check == True:
    for cluster in clusters:
            cluster.reset()
    for attributeName in data_Set:
        min = clusters[0].getdistancefromcentroid((attributeName))
        belongsToCluster = clusters[0]
        for cluster in clusters[1:]:
            dist_Centroid = cluster.getdistancefromcentroid((attributeName))# get distance from current centroid
            if(dist_Centroid < min):# assign the data to nearest cluster
                belongsToCluster = cluster
                min = dist_Centroid
        belongsToCluster.addname((attributeName))
    unchangedClusters = 0
    for cluster in clusters:#check centroid position with old one
       shift = cluster.update()
       if shift <= .0001:
           unchangedClusters += 1
    if(unchangedClusters==Num_Clusters):#check centroid position with old one
        check=False
    maxiterationcheck+=1
    if( maxiterationcheck >= maxiteration):# check max iteration
        check=False

#print the result and write it to out.txt
readerWriter.output(clusters, maxiterationcheck)