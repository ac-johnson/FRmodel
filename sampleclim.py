# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
from numpy import random

#Plan: there are 14 boxes. So x in [0,1]. Then I determine box by floor(x*14)
#I then take x-b/14 (box num). This gives a box bounds,
#and then I just take two samples
#basically I can just sample [0,13]
#middle box is a coin flip

def samplepico():
    

    crng = [[.55,.65],[.65,.75],[.75,.85],[.85,.95],[.95,1.5],[1.5,2.5],[2.5,3.5],
            [3.5,4.5],[4.5,5.5],[5.5,6.5],[6.5,7.5],
            [.75,.85],[.85,.95],[.95,1.5]]
    
    grng = [[1.5,2.5],[1.5,2.5],[1.5,2.5],[1.5,2.5],[1.5,2.5],[1.5,2.5],[1.5,2.5],
            [1.5,2.5],[1.5,2.5],[1.5,2.5],[1.5,2.5],
            [2.5,3.5],[2.5,3.5],[2.5,3.5]]
    
    crngsb1 = [[.95,1.0],[1.0,1.5]]
    crngsb2 = [[.95,1.0],[1.0,1.5]]
    
    grngsb1 = [[1.5,2.5],[1.5,2.5]]
    grngsb2 = [[2.5,3.5],[2.5,3.5]]

    boxnum = random.randint(0,14)
    if boxnum == 4:
        coin = random.randint(0,2)
        if coin==0:
            g=random.uniform(grngsb1[0][0],grngsb1[0][1])
            c=random.uniform(crngsb1[0][0],crngsb1[0][1])
        else:
            g=random.uniform(grngsb1[1][0],grngsb1[1][1])
            c=random.uniform(crngsb1[1][0],crngsb1[1][1])
    
    elif boxnum == 13:
        coin = random.randint(0,2)
        if coin==0:
            g=random.uniform(grngsb2[0][0],grngsb2[0][1])
            c=random.uniform(crngsb2[0][0],crngsb2[0][1])
        else:
            g=random.uniform(grngsb2[1][0],grngsb2[1][1])
            c=random.uniform(crngsb2[1][0],crngsb2[1][1])

    else:
        g=random.uniform(grng[boxnum][0],grng[boxnum][1])
        c=random.uniform(crng[boxnum][0],crng[boxnum][1])
        
    return g*1e-5,c

def samplesurf():
    # surfmodels = ['NORESM','CCSM4','MIROC_ESM_CHEM']
    # return surfmodels[random.randint(0,3)]
    return(random.randint(0,3))


# print(random.uniform())

if __name__=='__main__':
    #test the method for getting 
    numtwo = []
    for i in range(int(1e5)):
        vals = random.randint(0,3,150)
        numtwo.append(np.sum(vals==2))
    print(f'Mean number of twos: {np.mean(numtwo)}')
    print(f'std number of twos: {np.std(numtwo)}')