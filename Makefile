DIFF := meld
FILE := $(HOME)/.ipfs-cluster/service.json

start: clean-state
	ipfs-cluster-service

clean-state:
	ipfs-cluster-service state cleanup -y

edit:
	./edit-service-json.py

show-peers-to-be show-peers-current:
	./edit-service-json.py --$@

diff-bak:
	$(DIFF) $(FILE) $(FILE).bak

diff-orig:
	$(DIFF) $(FILE) $(FILE).orig

.PHONY: start clean-state edit \
        show-peers-to-be show-peers-current \
        diff-bak diff-orig
