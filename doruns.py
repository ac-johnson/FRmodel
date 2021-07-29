# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 11:49:07 2018

@author: andrewjohnson

PLEASE HAVE ARGUMENTS
"""

import os
import sys

runlist_start = int(sys.argv[1])
runlist_stop = int(sys.argv[2])

runlist = range(runlist_start,runlist_stop)

#templist=['0C','2C','4C','6C']
templist = ['0C','2C','4C']

rundir = '/import/c1/ICESHEET/ICESHEET/uaf-antarctica/filron/filron_runs/'

os.chdir(rundir)
print(os.system('pwd'))

for i in runlist:
    for T in templist:
        os.system('sbatch picoruns/ocean_%s/runcmds/pico_run%s.slurm'%(T,i))
