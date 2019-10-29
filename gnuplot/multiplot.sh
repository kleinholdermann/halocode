#!/usr/bin/gnuplot

set term x11 persist
set multiplot layout 6, 1 
set tmargin 2

unset key
plot 'colfile1.txt'
plot 'colfile2.txt'
plot 'colfile3.txt'
plot 'colfile4.txt'
plot 'colfile5.txt'
plot 'colfile6.txt'

unset multiplot
#
#
#
