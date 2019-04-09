import random
import math
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
class K_means_numerical:


    def __init__(self,path='',center=3,itr=0):
        self.path=path
        self.center=center
        self.itr=itr

    # K-Means Algorithm
    def kmeans(self, datapoints):

        # d - Dimensionality of Datapoints
        d = len(datapoints[0])

        # Limit our iterations
        Max_Iterations = 1000
        i = 0

        cluster = [0] * len(datapoints)
        prev_cluster = [-1] * len(datapoints)

        # Randomly Choose Centers for the Clusters
        cluster_centers = []
        for i in range(0, self.center):
            new_cluster = []
            # for i in range(0,d):
            #    new_cluster += [random.randint(0,10)]
            cluster_centers += [random.choice(datapoints)]

            # Sometimes The Random points are chosen poorly and so there ends up being empty clusters
            # In this particular implementation we want to force K exact clusters.
            # To take this feature off, simply take away "force_recalculation" from the while conditional.
            force_recalculation = False

        while (cluster != prev_cluster) or (i > Max_Iterations) or (force_recalculation):

            prev_cluster = list(cluster)
            force_recalculation = False
            i += 1

            # Update Point's Cluster Alligiance
            for p in range(0, len(datapoints)):
                min_dist = float("inf")

                # Check min_distance against all centers
                for c in range(0, len(cluster_centers)):

                    dist = eucldist(datapoints[p], cluster_centers[c])

                    if (dist < min_dist):
                        min_dist = dist
                        cluster[p] = c  # Reassign Point to new Cluster

            # Update Cluster's Position
            for self.center in range(0, len(cluster_centers)):
                new_center = [0] * d
                members = 0
                for p in range(0, len(datapoints)):
                    if (cluster[p] == self.center):  # If this point belongs to the cluster
                        for j in range(0, d):
                            new_center[j] += datapoints[p][j]
                        members += 1

                for j in range(0, d):
                    if members != 0:
                        new_center[j] = new_center[j] / float(members)

                        # This means that our initial random assignment was poorly chosen
                    # Change it to a new datapoint to actually force k clusters
                    else:
                        new_center = random.choice(datapoints)
                        force_recalculation = True
                        print("Forced Recalculation...")

                cluster_centers[self.center] = new_center

        print("======== Results ========")
        print("Clusters", cluster_centers)
        print("Iterations", i)
        print("Assignments", cluster)



# Euclidian Distance between two d-dimensional points
def eucldist(p0, p1):
    dist = 0.0
    for i in range(0, len(p0)):
        dist += (p0[i] - p1[i]) ** 2
    return math.sqrt(dist)


t=K_means_numerical()

datapoints = [(1, 2),
		(1.5, 1.8),
		(5, 8),
		(8, 8),
		(1, 0.6),
		(5, 9) ,
		(8, 6) ,
		(7, 7) ,
		(3, 3) ,
		(2, 4) ,
		(2, 0) ,
		(8, 1) ,
		(9.2, 0.5) ,
		(10, 2) ]
t.kmeans(datapoints)



