#!/bin/bash
#Program:
#  Create Virtualevn for python
#History:
#

read -p "Please input env name: " envname
read -p "Please select version: " ver

if [ $ver -eq "2" ]; then
  pypath=$(which python)
else
  pypath=$(which python3)
fi

# create virtual env
virtualenv -p $pypath $envname

