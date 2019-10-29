#!/bin/bash

# 1. cut leading and trailing meta info (stuff in front and behind of [] brackets
#    usind sed -> raw, comma separated data remains
# 2. transpose data and remove whitespace using rs
# 3. remove commas using sed

cat $1 | sed 's/.*\[//' |sed 's/].*//' |rs -c' ' -C' ' -T |sed 's/,//g'


