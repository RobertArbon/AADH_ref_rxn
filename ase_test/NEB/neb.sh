#!/bin/bash
#PBS -l walltime=02:30:00
#PBS -l nodes=1:ppn=1 
cd $PBS_O_WORKDIR
echo Running on host `hostname`
echo Time is `date`
echo Directory is `pwd`
echo PBS job ID is $PBS_JOBID
echo This jobs runs on the following machines:
echo `cat $PBS_NODEFILE | uniq`
source activate py27
input=neb.py
python $input > $input.out
