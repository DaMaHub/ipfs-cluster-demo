#!/bin/sh

if [ -z "$1" ]; then
    echo "datadir parameter expected"
    exit 1
fi

addr=$(geth account new --datadir $1 --password password.txt | sed 's/Address: {\(.*\)}/\1/')
echo $addr
