#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Plot Sensitivity

Created on Mon May 10 12:32:51 2021

@author: andrew
"""

import numpy as np
import netCDF4 as nc
from osgeo import gdal,osr
from matplotlib import pyplot as plt
import csv
from scipy import stats

pfloc = '/media/andrew/Clathrate/APModel_util/filron/sens/output' #pism output file loc
vfloc = '/media/andrew/Clathrate/APModel_util/filron/sens/Vel_align.tif' #NOTE: this is 2km file
cfile = 'config/sens_inputs.csv'   #config file
nlen = 48
norm_ord = 2

docomparison=1

velmap = gdal.Open(vfloc).ReadAsArray()
nanmap = velmap < 0
velmap[nanmap]=0

velmap = np.ma.masked_array(velmap,mask=nanmap)

#plt.figure()
#plt.imshow(velmap)
#plt.colorbar()

diffnorms = np.zeros(nlen)
diffnormsg= np.zeros(nlen)

### OPEN PARAMETER SETS ###

csvfile = open(cfile)
#readCSV = csv.reader(csvfile, delimiter=',')
readCSVd = csv.DictReader(csvfile)

for run in readCSVd:
    nn = int(run['id'])
    if nn==0:
       param_keys = run.keys()
       klen = len(param_keys)   #number of parameters
       params = np.zeros((nlen,klen))
      
    kk=0
    for key in param_keys:
        params[nn,kk] = run[key]
        kk+=1
    
#    test = run
    print(run)

### COMPARE PISM DATA ###
if docomparison==1:
    print('starting velocity comparisons')
    for nn in range(nlen):
    
        #nn=18
        pfstr = '%s/result_%s.nc'%(pfloc,nn)
        data = nc.Dataset(pfstr)
        pvmap = data.variables['velsurf_mag'][0]
        pvmap = np.flipud(pvmap)
        #pvmap[nanmap]=0
        
        #plt.figure()
        #plt.imshow(pvmap)
        #plt.colorbar()
    
        diffmap = velmap-pvmap
        diffnorms[nn]=np.linalg.norm(diffmap,ord=norm_ord)
        
        #get mask:
        if nn==0:
            imask = data.variables['mask'][0]
            imask = imask==3
            imask = np.flipud(imask)
        
        pvmapg = np.ma.masked_array(pvmap,mask=pvmap.mask | imask)
        
        diffmapg = velmap-pvmapg
        diffnormsg[nn]=np.linalg.norm(diffmapg,ord=norm_ord)
        
        data.close()
        
    print('finished velocity comparisons')


### PLOT RESULTS ###

def plotcomparison(diffnorms,param_name,param_vec,svstr='sens_',alpha=0.05):
    dn = diffnorms
    pn = param_name
    pv = param_vec
    
    slope,intercept,r,p,stdev = stats.linregress(pv,dn)
    
    plt.figure(figsize=(8,8))
    plt.plot(pv,dn,'.')
    if p<alpha:
        xmin=np.min(pv)
        xmax=np.max(pv)
        plt.plot([xmin,xmax],[xmin*slope+intercept,xmax*slope+intercept],'-',linewidth=1,color='gray')
    
    plt.ylabel('Diffnorm')
    plt.xlabel(pn)
    plt.title('Parameter: %s'%pn)
    plt.savefig('figures/%s%s.png'%(svstr,pn))
    
#    slope,

kk=0
for key in param_keys:
    plotcomparison(diffnorms,key,params[:,kk])
    plotcomparison(diffnormsg,key,params[:,kk],svstr='NOSHELF_sens_')
    kk+=1


plt.figure()
plt.imshow(diffmapg)
plt.colorbar()

#print('Matrix Norm: %d'%np.linalg.norm(diffmap,ord=2))