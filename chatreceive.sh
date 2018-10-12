#!/bin/bash
chain=$1
orclid=742d2317a734fce4f6f99862dd878ed58538434dc855cd76879ad68be3f1bff4
latest=""
n=0
while true; do
	pubs=$(komodo-cli -ac_name=$chain oraclesinfo $orclid | jq -r '.registered | .[] | .publisher')
	pubsarray=(${pubs///n/ })
	batons=$(komodo-cli -ac_name=$chain oraclesinfo $orclid | jq -r '.registered | .[] | .batontxid')
	batonarray=(${batons///n/ })
	len=$(komodo-cli -ac_name=$chain oraclesinfo $orclid | jq -r '[.registered | .[] | .publisher] | length')
	for i in $(seq 0 $(( $len - 1 ))); do
		message[$i]=$(komodo-cli -ac_name=$chain oraclessamples $orclid ${batonarray[$i]} 1 | jq -r '.samples[0][0]')
			if [ "${message[$i]}" != "${latest[$i]}" ]; then
        			latest[$i]=${message[$i]}
        				if [[ $n != 0 ]]; then
						kv=$(komodo-cli -ac_name=$chain kvsearch ${pubsarray[$i]} | jq -r .value)
						if [[ $kv = "null" ]]; then
							echo "[${pubsarray[$i]}]:${latest[$i]}"
						else
          						echo "[$kv]:${latest[$i]}"
						fi
        				fi
			fi
	done
	sleep 0.1
	n=$(( $n +1 ))
done
