#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 11:33:29 2021

@author: andrew
"""

import numpy as np
import os
import sys
#import glob

#runtemp = sys.argv[1]

runlist_start = int(sys.argv[1])
runlist_stop = int(sys.argv[2])
#runtemp = sys.argv[3]

#
runlist = range(runlist_start,runlist_stop)
#
##templist=['0C','2C','4C','6C']
##templist = ['0C','2C','4C']
templist = []
#
for t in sys.argv[3:]:
    templist.append(t)

rundir = '/import/c1/ICESHEET/ICESHEET/uaf-antarctica/filron/filron_runs/'
#rundir = rundir+'picoruns/ocean_'+runtemp+'/output/'

os.chdir(rundir)
#print(os.system('pwd'))



#flist = glob.glob(rundir+'picoruns/ocean_'+runtemp+'/output/*.nc')



for i in runlist:
    for T in templist:
        opdir = rundir+'picoruns/ocean_'+T+'/output/'
#        os.system('sbatch picoruns/ocean_%s/runcmds/pico_run%s.slurm'%(T,i))
        os.system('ncks -A -v x,y,mask,thk,velsurf_mag,flux_mag %sresult_%i.nc %sresult_thin_%i.nc'%(opdir,i,opdir,i))