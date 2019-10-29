#!/bin/bash

bash ../prep/raw_to_long.sh $1 > tmpfile1.txt

cat tmpfile1.txt | cut "-d " -f1 > colfile1.txt
cat tmpfile1.txt | cut "-d " -f2 > colfile2.txt
cat tmpfile1.txt | cut "-d " -f3 > colfile3.txt
cat tmpfile1.txt | cut "-d " -f4 > colfile4.txt
cat tmpfile1.txt | cut "-d " -f5 > colfile5.txt
cat tmpfile1.txt | cut "-d " -f6 > colfile6.txt

