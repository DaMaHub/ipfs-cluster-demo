#!/usr/bin/env python

import sys
import argparse
import json
import os
from os.path import expanduser
from shutil import copyfile
from collections import OrderedDict

json_data = open('genesis.json.in').read()
data = json.loads(json_data, object_pairs_hook=OrderedDict)

accounts = {}
for i in sys.argv[1:]:
    accounts[str(i)] = {"balance": "1000"}

data['alloc'] = accounts

# save the json data
with open('genesis.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)
