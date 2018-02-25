#!/bin/sh

user1=`./new_account.sh "user1"`
user2=`./new_account.sh "user2"`
./mk_genesis_block.py $user1 $user2
geth -datadir user1 init genesis.json
geth -datadir user2 init genesis.json
