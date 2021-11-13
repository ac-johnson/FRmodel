# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 15:00:05 2018

@author: andrewjohnson
"""
import numpy as np

#Create defaults

d = {}

#d['inspin']='maps/pism_spinup_filron_1km_3006n_1000yr.nc'
#d['inspin']='maps/pism_spinup_filron_3km_bedmap.nc'
#d['inspin']='maps/pism_spinup_filron_2km_bedmachine.nc'
d['inspin']='maps/pism_spinup4_filron_2km_bedmachine.nc'
#d['surffile'] = 'maps/filchner_ronne_res1km_new2b_cesm2mean_nolapse.nc'
d['surffile'] = 'maps/surface_2km_nolapse.nc'
d['otype'] = 'pico'
d['ofile'] = 'maps/pico/ocean_pico_2km_0C.nc'
#d['TGPhi']="15.0,40.0,-500,500"
d['TGP2'] = -900.0
d['TGP3'] = 1500.0
d['frontretreatfile'] = 'maps/filchner_ronne_res1km_new2b_cesm2mean_nolapse.nc'
#d['yearend'] = 1555
d['yearend'] = 1590
d['SIAe'] = 1.0
d['SSAe'] = 1.0
d['PPQ'] = 0.75
d['TEFO']=0.04
d['sloc']='picoruns'
d['sfile']='run_rcp85.slurm'
#d['ens']
#d['rcp']

#d['SIAe']=1.0
#d['SSAe']=0.60
#d['PPQ']=0.75
#

#d['ecalvK']='1e15'
#d['tcalvt']=50
##d['lapr']=8         #lapse rate
#d['PPUt']=100       #pseudo_plastic sliding threshold
#d['nbsm']=''
#d['bdef']=''
#d['calvstr']="-calving eigen_calving,thickness_calving"
#d['Yst']=0
#d['Yet']=200
##d['sshfi']=0.5
#d['otype']='pico'
#d['ostr']='-ocean_pico_file $CAI/data_sets/ocean/schmidtko_initmip8km.nc'
#d['Outloc']='$CAI/runs/output/'
#d['Outex']='$CAI/runs/extra/'
#d['misc']=''
#d['Atmofile']='$CAI/data_sets/climate/Atmosphere_Forcing/noresm1-m_rcp2.6/Regridded_8km/NorESM1-M_8km_clim_rcp26_1995-2014.nc'

#d['']
#d['-shelf_base_melt_rate']
#Or look at ocean.sub_shelf_heat_flux_into_ice  (default is 0.5 W m-2)

#print d
#np.save('config/defaults_calibration.npy',d)
np.save('config/defaults_rcp85.npy',d)



#d = {}
#
#d['SIAe']=2.0
#d['SSAe']=0.65
#d['PPQ']=0.25
#d['TEFO']=0.02
#d['TGPhi']="15.0,40.0,-700,-100"
#d['ecalvK']='5e15'
#d['tcalvt']=50
#d['lapr']=8         #lapse rate
#d['PPUt']=100       #pseudo_plastic sliding threshold
#d['nbsm']=''
#d['bdef']=''
#d['calvstr']="-calving eigen_calving,thickness_calving"
#d['Yst']=0
#d['Yet']=1000
#d['sshfi']=0.5
#d['Outloc']='$CENTERAIS/runs/'
##d['misc']=''
#
##d['-shelf_base_melt_rate']
##Or look at ocean.sub_shelf_heat_flux_into_ice  (default is 0.5 W m-2)
#
##print d
#np.save('defaults_filron.npy',d)

#d['SIAe']=2.0
#d['SSAe']=0.65
#d['PPQ']=0.25
#d['TEFO']=0.02
#d['TGPhi']="15.0,40.0,-700,-100"
#d['ecalvK']='5e15'
#d['tcalvt']=50
#d['lapr']=8         #lapse rate
#d['PPUt']=100       #pseudo_plastic sliding threshold
#d['nbsm']=''
#d['bdef']=''
#d['calvstr']="-calving eigen_calving,thickness_calving"
#d['Yst']=0
#d['Yet']=1000
#d['sshfi']=0.5
#d['Outloc']='$CENTERAIS/runs/'
##d['misc']=''

##if [ -z ${NN+1} ];
##then echo "Set NN number of cores!"; fi
#
#if [ -z ${SIAe+1} ];
#then export SIAe=2.0; fi
#
#if [ -z ${SSAe+1} ];
#then export SSAe=0.65; fi
#
#if [ -z ${PPQ+1} ];
#then export PPQ=0.25; fi
#
#if [ -z ${TEFO+1} ];
#then export TEFO=0.02; fi
#
#if [ -z ${TGPhi+1} ];
#then export TGPhi=15.0,40.0,-700,-100; fi
#
##if [ -z ${TFGO+1} ];		#What is this??
##then TFGO=15.0,40,-700,-100; fi
#
#if [ -z ${ecalvK+1} ];
#then export ecalvK=5e15; fi
#
#if [ -z ${tcalvt+1} ];
#then export tcalvt=50; fi
#
#if [ -z ${lapr+1} ];
#then export lapr=8; fi
#
#if [ -z ${PPUt+1} ];
#then export PPUt=100; fi
#
##Options to enable:
#if [ -z ${nsbm+1} ];
#then export nsbm="";
#else export nsbm="-no_subgl_basal_melt"; fi
#
#if [ -z ${bdef+1} ];
#then export bdefstr="";
#else export bedfstr="-bed_def "$bdef; fi
#
#if [ -z ${set_fk+1} ];
#then export calvstr="-calving eigen_calving,thickness_calving";
#else export calvstr="-calving float_kill,eigen_calving,thickness_calving"; fi