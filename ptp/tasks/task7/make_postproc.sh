#!/bin/bash

cd postproc_data || exit

./create_linear.gpi
./create_linear_error.gpi
./create_moustache.gpi

cd ..

