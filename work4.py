# Code by Raja Shah
import matplotlib.pyplot as plt
import math

# Epsilon and min point value
e=2.5
min_pnt=4
# Global variables
visited=[]
clust=[]
clusterpnts=[]

#####################################################################
# Extract data pnts from the file and place in 2D list P
P=[[]]
del(P[0])
with open ('jain.txt') as myfile:
    for line in myfile:
        a=list(map(float, line.split()))
        P.append(a)
a=[]
for row in P:
    a.append(row[0:2])

#####################################################################
# function to find Eucladian distance
def distance(p1,p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 )
    # return abs(p1[0]-p2[0])+abs(p1[0]-p2[0])

#####################################################################
# function that expands the clusters finding the neighbours
def neighbour(x,a):
    count=0
    b=[]
    isCore=False
    radius_pnts=[]
    global visited
    visited.append(x)
    for row in a:
        d = distance(row , x)
        if(d <= e ):
            b.append(row)
            count=count+1
        if(count==min_pnt):
            #x is a core
            isCore=True

    a.append(x)
    if(isCore==True):
        for t in b:
            radius_pnts.append(t)
        isCore=False
    else:
        return False   # x is not a core
    return radius_pnts      # radius_pnts are pnts. that lie in the radius

###################################################################
# function to find all the cluster
def main():
    c=[]
    global a
    global visted
    global clust
    global clusterpnts
    
    for row in a:  
        if(row in visited):
            continue
        a.remove(row)
        c=neighbour(row,a)
        if(c!=False):
            for pnt in c:
                c1=neighbour(pnt, a)
                if(c1!=False):
                    for item in c1:
                        if item not in c:
                            c.append(item)
                            clusterpnts.append(item)
            clust.append(c)
            
###################################################
main()   ## initial call ti main()
print "No. of clusters: %d" %len(clust)

####################################################        
# plot all the clusters
for cluster in clust:
    x1=[]
    x2=[]
    for pnt in cluster:
        x1.append(pnt[0])
        x2.append(pnt[1])
    plt.scatter(x1,x2, s=25)
plt.show()   
###################################################



