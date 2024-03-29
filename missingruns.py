# -*- coding: utf-8 -*-
"""

Run pism commands. To run this script put in:
    
python doruns.py runstart runstop scenario1 scenario2 ...

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

for T in templist:
	print(f'\n{T}')
	for i in runlist:
		resultfile = f'picoruns/ocean_{T}/output/result_{i}.nc'
		extrafile = f'picoruns/ocean_{T}/extra/extra_{i}.nc'
		timeseriesfile = f'picoruns/ocean_{T}/extra/timeseries_{i}.nc'
		if not exists(resultfile):
			#print(f'No result: run {i}')
			#failstate = 'unknown'
			if exists(f'picoruns/ocean_{T}/output/result_medium_{i}_stressbalance_failed.nc'):
				#failstate='stress'
				print(f'Run {i} failed: stressbalance')
			elif exists(f'picoruns/ocean_{T}/output/result_medium_{i}_max_thickness.nc'):
				print(f'Run {i} failed: max thickness')
			else:
				print(f'Run {i} failed: reason unknown')
		if not exists(extrafile):
			if exists(resultfile):
				print(f'Run {i} succeeded but has no extra file. Weird!')			
				
