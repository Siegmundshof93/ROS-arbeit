#!/bin/bash
#input=" in/0x0087_0x0000001600097095827"
FILES=/home/pvl/ROS/decor_result/in/*
for f in $FILES
do
#echo "processed $f"
   xxd -u $f



   #$f > data.txt
done > data.csv
#xxd in/0x0087_0x000000160009709582
python3 decor.py
