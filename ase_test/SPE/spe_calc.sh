#!/bin/bash
export PBS_NP=2
#PBS -l walltime=02:30:00
#PBS -l nodes=1:ppn=2 
cd $PBS_O_WORKDIR
echo Running on host `hostname`
echo Time is `date`
echo Directory is `pwd`
echo PBS job ID is $PBS_JOBID
echo This jobs runs on the following machines:
echo `cat $PBS_NODEFILE | uniq`
echo $ASE_NWCHEM_COMMAND
input=spe_calc.py
python $input > $input.out
