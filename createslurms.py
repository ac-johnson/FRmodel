# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 11:49:07 2018

@author: andrewjohnson
"""

# How to set up PISM runs:
#
# Use the "CreateDefaults" script to create a numpy array of default values.
# Create an input CSV. The first line should be keys which align with the
#   keys from the defaults file, and then values entered for each run.

import csv
import numpy as np
import os

defaultfile = '/home/acjohnson16/FRmodel/config/defaults_sens.npy'
inputfile = 'config/sens_inputs.csv'
outns = ''              #out name start
rundir = '/import/c1/ICESHEET/ICESHEET/uaf-antarctica/filron/filron_runs/'
runcmddir = 'sens/runcmds/'


#TESTCOMMENT
#Values that must be in defaults list:
#    
#    runname,sfile,NN,PART,mx,my,Inspin,Inboot

#setrunlist = range(,21)
#setrunlist = [21]
#dorunlist = range(12,21)
#dorunlist = []
doruns = 1
dorunlist = range(30)


partition = 't2small'
nodes = '48'

#runnums = np.array(setrunlist)

#setrunlist = ['run'+str(i) for i in setrunlist]
#dorunlist = ['run'+str(i) for i in dorunlist]


defaults = np.load(defaultfile,allow_pickle=True).item()

csvfile = open(inputfile)
#readCSV = csv.reader(csvfile, delimiter=',')
readCSVd = csv.DictReader(csvfile)

def adddefaults(run,defaultfile):
    #Adds default values if value doesn't exist
    runkeys = run.keys()
    defaults = np.load(defaultfile,allow_pickle=True).item()
    for key in defaults.keys():
        if key not in runkeys:
            run[key]=defaults[key]
        if not run[key]:
            run[key]=defaults[key]
            
os.chdir(rundir)
print(os.system('pwd'))
            
for run in readCSVd:
    #run = row
    #print run
#    if run['id'] in setrunlist:
    run['Outfm']=outns+run['id']+'.nc'
    run['runnum']=(run['id'])
    run['PART'] = partition
    run['NN'] = nodes

#        currentdir = dirname + run['runname']
    
#        print(currentdir)        
    #Create run directory if it does not exist:
#        if not os.path.exists(currentdir):
#            print('creating dir for: '+run['runname'])
#            os.makedirs(currentdir)

    #Add in default values
    adddefaults(run,defaultfile)

    sfile=run['sfile']
    os.system('cp '+sfile+' runtemp.slurm')
#        os.system('rm ' + currentdir +'/run.slurm')

    #Set up the sbatch tasks and partitions:
    #   (This cannot be done with variables other than just writing
    #   a new file)        
    f = open('runtemp.slurm','r+')
    s = f.read()
    #print "%s, ecalvK: %s" % (run['runname'],run['ecalvK'])
    #print run['Outloc']
    for key in run.keys():
        s = s.replace('$'+str(key),str(run[str(key)]))
        f.seek(0)

    f.seek(0)
    f.write(s)
    f.close()
    
    os.system('cp runtemp.slurm sens/runcmds/sens_run%s.slurm'%run['id'])
    os.system('rm runtemp.slurm')

    #if run['runname'] in dorunlist:
    if doruns==1:
        runcheck=1
        if dorunlist:
            if int(run['id']) not in dorunlist:
                runcheck=0
        if runcheck==1:
            os.system('sbatch sens/runcmds/sens_run%s.slurm'%run['id'])
    #        os.system('cd '+ currentdir + '; sbatch run.slurm')
    

#mpiexec -n $NN -machinefile ./nodes.$SLURM_JOB_ID pismr -i $Inspin \
#  -Mx $mx -My $my \
#  -skip -skip_max 20 \
#  -bed_smoother_range 5e3 \
#  -grid.correct_cell_areas false -grid.registration corner \
#  -ys -$Yst -ye $Yet \
#  -surface given -surface_given_file $Inboot \
#  -atmosphere given,lapse_rate -atmosphere_given_file $Inboot \
#  -atmostphere_lapse_rate_file $Inboot -temp_lapse_rate $lapr \
#  -sia_e $SIAe -ssa_e $SSAe -stress_balance ssa+sia \
#  -topg_to_phi $TGPhi -pseudo_plastic -pseudo_plastic_q $PPQ \
#  -pseudo_plastic_uthreshold $PPUt \
#  -till_effective_fraction_overburden $TEFO \
#  -calving $calvstr \
#  -eigen_calving_K $ecalvK -thickness_calving_threshold $tcalvt \
#  -subgl true $nsbm $bdefstr \
#  -tauc_slippery_grounding_lines -ts_file "${Outloc}ts_${Outfm}" -ts_times -$Yst:yearly:$Yet \
#  -extra_file "${Outloc}ex_${Outfm}" -extra_times -$Yst:100:$Yet \
#  -extra_vars diffusivity,temppabase,tempicethk_basal,bmelt,tillwat,velsurf_mag,mask,thk,topg,usurf,hardav,velbase_mag,tauc,tendency_of_ice_amount_due_to_discharge,dHdt \
#  -o "$Outloc$Outfm"


