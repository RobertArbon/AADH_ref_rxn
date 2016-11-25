#!/bin/bash

charmm_dir=$CHARMMROOT/vanilla
input=add_hatoms

$charmm_dir/charmm -i $input.inp > $input.out
