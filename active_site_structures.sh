#!/bin/bash
# #PBS -l walltime=10:00:00
# ##PBS -q gpu
# #PBS -l nodes=1:ppn=1 #:gpus=1
# cd $PBS_O_WORKDIR
# echo Running on host `hostname`
# echo Time is `date`
# echo Directory is `pwd`
# echo PBS job ID is $PBS_JOBID
# echo This jobs runs on the following machines:
# echo `cat $PBS_NODEFILE | uniq`

charmm_dir=$CHARMMROOT/gnu
input=active_site_structures

$charmm_dir/charmm -i $input.inp > $input.out