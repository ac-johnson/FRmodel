#!/bin/bash

#SBATCH --partition=t2small
#SBATCH --job-name=FRr2_$id
#SBATCH --ntasks=$NN
#SBATCH --tasks-per-node=24
#SBATCH --account=ICESHEET
#SBATCH --mail-user=acjohnson16@alaska.edu
#SBATCH --mail-type=FAIL
#SBATCH --output=$sloc/logs/pismlog_$id.%j
#SBATCH --time=00-08:00:00

umask 007
ulimit -s unlimited
ulimit -l unlimited
ulimit

# Generate a list of allocated nodes; will serve as a machinefile for mpirun
srun -l /bin/hostname | sort -n | awk '{print $2}' > ./nodes.$SLURM_JOB_ID
# Launch the MPI application

mpiexec -n $NN -machinefile ./nodes.$SLURM_JOB_ID pismr -i $inspin -surface given,anomaly -surface_given_file maps/surface_2km_nolapse.nc -surface_anomaly_file $sa_file -ocean pico -ocean_pico_file maps/ocean_2km_rcp26_1995-2100.nc -gamma_T $pico_g -overturning_coeff $pico_c -bed_def none -hydrology null -topg_to_phi 1.0,45.0,$TGP2,$TGP3 -config_override maps/pism_config_override.nc -config maps/pism_config_default.nc -front_retreat_file $frontretreatfile -ys 2015 -ye 2100 -skip -skip_max 100 -options_left -verbose 2 -o_format netcdf4_parallel -o_order yxz -allow_extrapolation -ssa_dirichlet_bc -stress_balance.sia.max_diffusivity 6000 -regional -regional.zero_gradient -ssa_rtol 1.0e-4 -ssa_maxi 300 -ssafd_nuH_iter_failure_underrelaxation 0.8 -ssa_eps 1.0e13 -sia_e $SIAe -ssa_e $SSAe -ssa_method fd -stress_balance ssa+sia -sia_flow_law gpbld -ssa_flow_law gpbld -pik -calving eigen_calving,thickness_calving -eigen_calving_K 2e15 -thickness_calving_threshold 100 -pseudo_plastic -pseudo_plastic_q $PPQ -pseudo_plastic_uthreshold 100.0 -till_effective_fraction_overburden $TEFO -subgl -ts_file $sloc/extra/timeseries_$id.nc -ts_times 0:yearly:2200 -extra_file $sloc/extra/extra_large_$id.nc -extra_times -1:yearly:2200 -extra_vars mask,velsurf_mag,thk,flux_mag,shelfbmassflux -o $sloc/output/result_medium_$id.nc -o_size medium

#-extra_file $sloc/extra/extra_$id.nc -extra_times -1:5:2000 -extra_vars velbar_mag,mask,dbdt,topg,thk,usurf,ice_surface_temp,climatic_mass_balance,bmelt,tillwat,velsurf_mag,diffusivity 

##### EXTRACT AND COMPRESS NC FILES #####

#Convert result_medium to result_thin:
echo "Attempting to convert to thin"
if test -f $sloc/output/result_thin_$id.nc; then
    echo "removing old thin"
    rm $sloc/output/result_thin_$id.nc
fi
ncks -A -v x,y,lat,lon,velsurf_mag,thk,mask,shelfbmassflux $sloc/output/result_medium_$id.nc $sloc/output/result_thin_$id.nc
if test -f $sloc/output/result_thin_$id.nc; then
    echo "removing result_medium files"
    rm $sloc/output/result_medium_$id.nc
    rm $sloc/output/result_medium_$id_backup.nc
    rm $sloc/output/result_medium_$id_backup.nc~
fi

#Convert result_thin to result
echo "removing converting thin to result"
if test -f $sloc/output/result_$id.nc; then
    echo "removing old result"
    rm $sloc/output/result_$id.nc
fi
ncks -4 -L 2 $sloc/output/result_thin_$id.nc $sloc/output/result_$id.nc
if test -f $sloc/output/result_$id.nc; then
    echo "removing thin"
    rm $sloc/output/result_thin_$id.nc
fi

#Convert extra_large to extra
echo "Compressing extra_large"
if test -f $sloc/extra/extra_$id.nc; then
    echo "removing old extra"
    rm $sloc/extra/extra_$id.nc
fi
ncks -4 -L 2 $sloc/extra/extra_large_$id.nc $sloc/extra/extra_$id.nc
if test -f $sloc/extra/extra_$id.nc; then
    echo "removing extra_large"
    rm $sloc/extra/extra_large_$id.nc
fi

#ncks -A -v x,y,lat,lon,velsurf_mag,thk,mask,shelfbmassflux $sloc/output/result_medium_$id.nc $sloc/output/result_thin_$id.nc
#ncks -4 -L 2 $sloc/output/result_thin_$id.nc $sloc/output/result_$id.nc
#ncks -4 -L 2 $sloc/extra/extra_large_$id.nc $sloc/extra/extra_$id.nc

#rm $sloc/output/result_medium_$id.nc
#rm $sloc/output/result_thin_$id.nc
#rm $sloc/extra/extra_large_$id.nc
#rm $sloc/output/result_medium_$id_backup.nc
#rm $sloc/output/result_medium_$id_backup.nc~

# Clean up the machinefile
rm ./nodes.$SLURM_JOB_ID


