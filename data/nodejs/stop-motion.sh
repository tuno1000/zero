#!bin/bash

kill `pidof /usr/bin/motion | awk '{print $1}'`

exit 0
