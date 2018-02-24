#!/usr/bin/env python

import json
from os.path import expanduser
from shutil import copyfile
from collections import OrderedDict

# get the home folder
home = expanduser("~")

# the file to edit
json_filename = home + '/.ipfs-cluster/service.json' 

# make a backup file
copyfile(json_filename, json_filename + '.bak')

# load the data
json_data = open(json_filename).read()
data = json.loads(json_data, object_pairs_hook=OrderedDict)

# edit the data
data['cluster']['secret'] = 'af204ff961615e83fbf9f8b19d669e2b39e9fc9d469f0394481dcb92b35a096a'

dimitris = "/ip4/10.189.102.241/tcp/9096/ipfs/Qmdo7ML44MUmqHCqBsAZsv1WKMCQh3kjcktGA3ewHjWjC6"
sonke = "/ip4/10.189.102.255/tcp/9096/ipfs/QmUPavTLbQqw89HsUPWRMuFs6SS54FGcSKLAmFF9hs6EZC"
deniz = "/ip4/10.189.103.0/tcp/9096/ipfs/QmR2qzY2jknHDPG4pngt3fdYrCfWay2w9iXAr6GmZNUBfq"
ayham = "/ip4/10.189.103.10/tcp/9096/ipfs/Qmbc9RPXaBvCdWvvbqRb8CRFekSKYp6auxsAh3e6N5S5ow"
simone = "/ip4/10.189.102.254/tcp/9096/ipfs/QmeAsyicNP9EXfD5kW12bGfdUGPnTjpmhgoWv1zGyMvink"
denis = "/ip4/10.189.102.224/tcp/9096/ipfs/Qmck9UaVJXpmQ9gbvcAL8T8DPVnUNoq57BXTeAHtpQkrCL"

data['cluster']['peers'] = []
data['cluster']['peers'].append(dimitris)
data['cluster']['peers'].append(sonke)
data['cluster']['peers'].append(deniz)
data['cluster']['peers'].append(ayham)
data['cluster']['peers'].append(simone)
data['cluster']['peers'].append(denis)

# save the data
with open(json_filename, 'w') as outfile:  
    json.dump(data, outfile, indent=4)
