#!/bin/bash

# runs an infinite loop which waits for the IMU data (6 rows) from the halocode device and
# saves the data to timestamped text files

while true
do
mosquitto_sub -h test.mosquitto.org -t /KLEINHOLDERMANN/HALOCODE -C 6 > ../data/log_$(date -Is).txt
done
