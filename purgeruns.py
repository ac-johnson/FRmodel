#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Purge old PISM data. To run this script put in:
    
python purgeruns.py runstart runstop scenario1 scenario2 ...

ex: python missingruns.py 50 75 0C 1C 2C 4C 6C

Created on Pi Day, 2022

@author: andrewjohnson

PLEASE HAVE ARGUMENTS
"""



import os
from os.path import exists
import sys

runlist_start = int(sys.argv[1])
runlist_stop = int(sys.argv[2])

runlist = range(runlist_start,runlist_stop)

#templist=['0C','2C','4C','6C']
#templist = ['0C','2C','4C']
templist = []

for t in sys.argv[3:]:
    templist.append(t)

rundir = '/import/c1/ICESHEET/ICESHEET/uaf-antarctica/filron/filron_runs/'

os.chdir(rundir)
print(os.system('pwd'))

runlist = range(0,100)

def purge(file):
    if exists(file):
        print(f'Purging {file}')
        os.system(f'rm {file}')

dopurge=False
if input('Warning. This will delete files. Are you sure (yes/no): ')=='yes':
    if input('Ok, but are you absolutely certain (yes/no): ')=='yes':
        dopurge=True
        print('ITS A PURGE PLANET MORTY\n')
    else:
        print('Oh good')
else:
    print('Yeah, best not to')

for T in templist:
    print(f'\n{T}')
    for i in runlist:
        if dopurge:
            resultfile = f'picoruns/ocean_{T}/output/result_{i}.nc'
            medfile = f'picoruns/ocean_{T}/output/result_medium_{i}.nc'
            medbackfile = f'picoruns/ocean_{T}/output/result_medium_{i}_backup.nc'
            medback2file = f'picoruns/ocean_{T}/output/result_medium_{i}_backup.nc~'
            extrafile = f'picoruns/ocean_{T}/extra/extra_{i}.nc'
            extralargefile = f'picoruns/ocean_{T}/extra/extra_large_{i}.nc'
            extralarge2file = f'picoruns/ocean_{T}/extra/extra_large_{i}.nc~'
            timeseriesfile = f'picoruns/ocean_{T}/extra/timeseries_{i}.nc'
            
            purge(resultfile)
            # purge(medfile)
            # purge(medbackfile)
            # purge(medback2file)
            purge(extrafile)
            # purge(extralargefile)
            # purge(extralarge2file)
            purge(timeseriesfile)

# 		if not exists(resultfile):
# 			#print(f'No result: run {i}')
# 			#failstate = 'unknown'
# 			if exists(f'picoruns/ocean_{T}/output/result_medium_{i}_stressbalance_failed.nc'):
# 				#failstate='stress'
# 				print(f'Run {i} failed: stressbalance')
# 			elif exists(f'picoruns/ocean_{T}/output/result_medium_{i}_max_thickness.nc'):
# 				print(f'Run {i} failed: max thickness')
# 			else:
# 				print(f'Run {i} failed: reason unknown')
# 		if not exists(extrafile):
# 			if exists(resultfile):
# 				print(f'Run {i} succeeded but has no extra file. Weird!')			