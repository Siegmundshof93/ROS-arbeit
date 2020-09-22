#!/bin/bash
#############################################creating a time file#############################
FILES=/home/pvl/ROS/decor_result/in/*
for f in $FILES
do

ls --full-time $f




done > time_decor.csv

#############################################creating a decor file#########################


for f in $FILES
do

   xxd -u $f




done > data.csv

###########################################python execution################################

python3 py_time.py

python3 decor.py
