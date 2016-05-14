

class InputOutputOperation(object):

    def __init__(self,filename):
        self.inputfilename=filename

    def input(self):
        '''inputfile = raw_input(
            "Enter the fileName to learn from:\n1. i.txt(1-D attribute)\n2. in.txt(2-d Attributes)\n3. irisData.txt(3-d attributes)"
            "\n\tOr Enter Full Path of the file with attributes of any dimesion\nNote: Max iteration is set as n^(kd) where n=num of examples, k= clusters, d= dimensions.\n=>")
        '''
        with open(self.inputfilename) as f:
            Num_Examples = int(f.readline())
            Num_Attributes = int(f.readline())
            Num_Clusters = int(f.readline())
            maxiteration = Num_Clusters * Num_Attributes
            maxiteration = Num_Attributes ** maxiteration
            if (Num_Examples <= Num_Clusters):
                f.close()
                print ("\nPlease reduce the number of clusters")
                raise SystemExit
            data = f.readlines()
            #Data = []
            data_Set = {}
            for line in data:
                x = line.lower().rstrip("\n").replace(' ', '').split(',')
                #p = int(Num_Attributes - 1)
                attributes = map(float, x[1:])
                data_Set[x.pop(0)] = attributes
        f.close()
        return data_Set, Num_Examples,Num_Clusters, maxiteration

    def output(self,clusters,totaliteration):
        x = 1
        with open("out.txt", "w+") as f:
            f.write("File Name:  {0}\n".format(self.inputfilename))
            f.write(("Total Iteration: {0}\n\n".format(totaliteration)))
            f.write("================================================================================================================\n")
            for cluster in clusters:
                f.write("CLUSTER NUMBER:{0}\n".format(x))
                f.write("TOTAL MEMBERS:{0}\n".format(len(cluster.attributeNames)))
                f.write("Attribute NAMES: {0}\n".format(cluster.attributeNames))
                f.write("ATTRIBUTE CORDINATES:{0}\n ".format(cluster.attributes))
                f.write("CENTROID COORDINATES: {0}\n".format(cluster.centroid))
                f.write("================================================================================================================\n")
                print ("================================================================================================================")
                print("Filename: {0}\n Max iteration:{1}\n".format(self.inputfilename, totaliteration))
                print ("CLUSTER NUMBER:\t\t\t", x)
                print ("TOTAL MEMBERS= \t\t\t", len(cluster.attributeNames))
                print ("ATTRIBUTE NAMES:\t  ", cluster.attributeNames)
                print ("CORDINATES_ATTRIBUTE: ", cluster.attributes)
                print ("COORDINATES_CENTROID: ", cluster.centroid)
                x += 1
        print ("================================================================================================================")