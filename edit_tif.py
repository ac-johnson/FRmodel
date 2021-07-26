#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This creates a new velocity map (or two) which have masked areas masked out.

Created on Mon Jun 28 11:35:42 2021

@author: andrew
"""

import numpy as np
import netCDF4 as nc
from osgeo import gdal,osr
from matplotlib import pyplot as plt
import csv
from scipy import stats

refnc = '/media/andrew/Clathrate/APModel_util/filron/maps/pism_spinup3_filron_2km_bedmachine.nc'
vfloc = '/media/andrew/Clathrate/APModel_util/filron/sens/Vel_align_nofloat.tif' #NOTE: this is 2km file

refds = nc.Dataset(refnc,'r')

velmap = gdal.Open(vfloc).ReadAsArray()



#add bound lines around the edge of the map:
newvelmap = np.zeros(np.shape(velmap))-999
bandpix=15
newvelmap[bandpix:-bandpix,bandpix:-bandpix]=velmap[bandpix:-bandpix,bandpix:-bandpix]
velmap = newvelmap

nanmap = velmap < 0
velmap[nanmap]= np.nan

velmap = np.ma.masked_array(velmap,mask=nanmap)



drat = 917/1030

thkmap = np.flipud(np.array(refds.variables['thk'][0,:]))
topgmap = np.flipud(np.array(refds.variables['topg'][0,:]))

velmap[thkmap==0]=np.nan

np.save('/media/andrew/Clathrate/APModel_util/filron/sens/Vel_align.npy',velmap.data)

slmap = topgmap < 0
flcrit = thkmap < -1*topgmap/drat

velmap[flcrit]=np.nan
np.save('/media/andrew/Clathrate/APModel_util/filron/sens/Vel_align_nofloat.npy',velmap.data)

#tthmap = thkmap < 500
#tthmap[flcrit==False] = False
#
#velmap[tthmap]=np.nan
#np.save('/media/andrew/Clathrate/APModel_util/filron/sens/Vel_align_minthk.npy',velmap.data)


#velmap[]


#np.save('/media/andrew/Clathrate/APModel_util/filron/sens/Vel_align.npy',velmap)

refds.close()
#velmap.Close()