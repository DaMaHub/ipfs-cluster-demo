# ipfs-cluster-demo
IPFS cluster demo 24 Feb 2018

Workflow:

One time configuration:
```
git clone https://github.com/DaMaHub/ipfs-cluster-demo
```

To sync:
```
cd https://github.com/DaMaHub/ipfs-cluster-demo
git pull
./edit-service-json.py
rm -rf $HOME/.ipfs-cluster/ipfs-cluster-data && ipfs-cluster-service
```
