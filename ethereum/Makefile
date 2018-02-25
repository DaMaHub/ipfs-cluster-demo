init:
	rm -rf user1 user2
	./mk_all.sh

mine-user1:
	geth --mine --rpc --networkid 999 --datadir "user1"

mine-user2:
	geth --mine --rpc --networkid 999 --datadir "user2" --port 30304 --rpcport 8486
