__author__ = 'quynhdo'

import numpy as np

colums = ["computer", "data", "pinch", "result", "suger"]
rows= ["apricot", "pineapple", "digital", "information"]

counts=  [[0,0,1,0,1], [0,0,1,0,1], [2,1,0,1,0], [ 1,6,0,4,0]]

colums = ["large","computer", "data", "pinch", "result", "suger"]
rows= ["apricot", "pineapple", "digital", "information"]

counts=  [[2,0,0,1,0,1], [1,0,0,1,0,1], [0,2,1,0,1,0], [1, 1,6,0,4,0]]




### calculate P(c)
counts_arr = np.asarray(counts)

sum_c = np.sum(counts_arr)

p_c = np.asarray([ np.sum(counts_arr[:,i])/ sum_c for i in range(len(colums))])

#p_c = np.around(p_c, decimals=2)
print (p_c)


p_w = np.asarray([ np.sum(counts_arr[i,:])/ sum_c for i in range(len(rows))])

#p_w = np.around(p_w, decimals=2)
print (p_w)


p_w_c = np.asarray(counts_arr/sum_c)
#p_w_c = np.around(p_w_c, decimals=2)
print (p_w_c)


#### PMI score
final_pmi=[]
s = ""
for i in range(len(rows)):
    rs = []
    for j in range(len(colums)):
        rs.append(np.around(np.log2(p_w_c[i,j]/(p_c[j]*p_w[i])), decimals=2))
        s+= str(np.around(np.log2(p_w_c[i,j]/(p_c[j]*p_w[i])), decimals=2)) + " & "
    s+="\n"




    final_pmi.append(rs)
print (s)
print (np.asarray(final_pmi))
print (np.log2(0.05/(0.16*0.58)))


import math
def cosine(u,v):
    x=0
    for i in range(len(u)):
        x+= u[i]*v[i]
    y=0
    for i in range(len(u)):
        y+= u[i]*u[i]

    z=0
    for i in range(len(v)):
        z+= v[i]*v[i]
    print ( "----")
    print (x)
    print (y)
    print (z)
    print ((math.sqrt(y)* math.sqrt(z)))
    print (x/(math.sqrt(y)* math.sqrt(z)))


print (cosine([0,1,2],[1,6,1]))

