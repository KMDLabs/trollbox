#!/bin/bash
#arg1 is chain
#arg2 is oracleid
#arg3 is length of pubkey to show, people can impersonate names, but not pubkeys. Default is 6, make it higher if you want to be sure you're talking to the right person
chain=$1
orclid=$2
verlen=${3:-6}
${1:-foo}
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
							ver=$(echo ${pubsarray[$i]} | head -c $verlen)
          						echo "[$kv-$ver]:${latest[$i]}"
						fi
        				fi
			fi
	done
	sleep 0.1
	n=$(( $n +1 ))
done
