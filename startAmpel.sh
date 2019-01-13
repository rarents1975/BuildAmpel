#!/bin/bash

i=0

while [ $i == 0 ]
do
 sleep 10
 prozesstest="/bin/ps -ef"
 test="$($prozesstest | grep ampelAPI.py | wc -l)"
 echo test $test
 if [ $test == 1 ]
 then
 /usr/bin/python /home/pi/ampel/ampelAPI.py
 fi
done
