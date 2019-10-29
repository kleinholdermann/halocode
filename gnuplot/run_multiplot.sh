#!/bin/bash

# first runs preparation file which splits data into six files, one
# for each column
# then runs multiplot in order to display data

bash multiplot_prep.sh $1
/usr/bin/gnuplot multiplot.sh
