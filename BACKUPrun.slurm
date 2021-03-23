#!/bin/bash

#SBATCH --partition=t2standard
#SBATCH --job-name=filron_9
#SBATCH --ntasks=192
#SBATCH --tasks-per-node=24
#SBATCH --account=ICESHEET
#SBATCH --mail-user=acjohnson16@alaska.edu
#SBATCH --output=logs/pismlog.%j

umask 007
ulimit -s unlimited
ulimit -l unlimited
ulimit

# Generate a list of allocated nodes; will serve as a machinefile for mpirun
srun -l /bin/hostname | sort -n | awk '{print $2}' > ./nodes.$SLURM_JOB_ID
# Launch the MPI application

mpiexec -n $SLURM_NTASKS pismr -i maps/pism_spinup_filron_1km_3006n_1000yr.nc -surface given -surface_given_file maps/filchner_ronne_res1km_new2b_cesm2mean_nolapse.nc -ocean given -ocean_given_file maps/fesom2pism_temp.nc -bed_def none -hydrology null -topg_to_phi 1.0,45.0,-900.0,1500.0 -config_override maps/pism_config_override.nc -config maps/pism_config_default.nc -front_retreat_file maps/filchner_ronne_res1km_new2b_cesm2mean_nolapse.nc -ye 1050 -skip -skip_max 100 -options_left -verbose 2 -o_format netcdf4_parallel -o_order yxz -allow_extrapolation -ssa_dirichlet_bc -stress_balance.sia.max_diffusivity 500 -backup_interval 3.0 -ssa_rtol 1.0e-4 -ssa_maxi 300 -ssafd_nuH_iter_failure_underrelaxation 0.8 -ssa_eps 1.0e13 -sia_e 1.0 -ssa_e 1.0 -ssa_method fd -stress_balance ssa+sia -sia_flow_law gpbld -ssa_flow_law gpbld -pik -pseudo_plastic -pseudo_plastic_q 0.75 -pseudo_plastic_uthreshold 100.0 -till_effective_fraction_overburden 0.04 -subgl -ts_file extra/timeseries_run9.nc -ts_times 0:yearly:2000 -extra_file extra/extra_run9.nc -extra_times -1:1:2000 -extra_vars velbar_mag,mask,dbdt,topg,thk,usurf,ice_surface_temp,climatic_mass_balance,bmelt,tillwat,velsurf_mag,diffusivity -save_file output/snap_run9 -save_times 0:1:2000 -save_split -save_size small -o output/result_run9.nc -o_size small

# Clean up the machinefile
rm ./nodes.$SLURM_JOB_ID


