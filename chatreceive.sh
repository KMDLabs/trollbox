#!/bin/bash
#arg1 is chain
#arg2 is oracleid
#arg3 is length of pubkey to show, people can impersonate names, but not pubkeys. Default is 6, make it higher if you want to be sure you're talking to the right person
chain=${1:-STAKEDB1}
orclid=${2:-742d2317a734fce4f6f99862dd878ed58538434dc855cd76879ad68be3f1bff4}
verlen=${3:-6}
dateformat=${4:-+%T-%Z}
latest=""
n=0
while true; do
	pubs=$(komodo-cli -ac_name=$chain oraclesinfo $orclid | jq -r '.registered | unique' | jq -r '.[] | .publisher')
	pubsarray=(${pubs///n/ })
	batons=$(komodo-cli -ac_name=$chain oraclesinfo $orclid | jq -r '.registered | unique' | jq -r '.[] | .batontxid')
	batonarray=(${batons///n/ })
	len=$(komodo-cli -ac_name=$chain oraclesinfo $orclid | jq -r '.registered | unique' | jq -r '.[] | .publisher'|wc -l)
	for i in $(seq 0 $(( $len - 1 ))); do
		message[$i]=$(komodo-cli -ac_name=$chain oraclessamples $orclid ${batonarray[$i]} 1 | jq -r '.samples[0][0]')
			if [ "${message[$i]}" != "${latest[$i]}" ]; then
        			latest[$i]=${message[$i]}
        				if [[ $n != 0 ]]; then
						kv=$(komodo-cli -ac_name=$chain kvsearch ${pubsarray[$i]} | jq -r .value)
						if [[ $kv = "null" ]]; then
							echo "$(date -d @$(echo ${latest[$i]} | head -c 10) $dateformat)[${pubsarray[$i]}]:$(echo "${latest[$i]}" | cut -c 11-)"
						else
							ver=$(echo ${pubsarray[$i]} | head -c $verlen)
          						echo "$(date -d @$(echo ${latest[$i]} | head -c 10) $dateformat)[$kv-$ver]:$(echo "${latest[$i]}" | cut -c 11-)"
						fi
        				fi
			fi
	done
	sleep 0.1
	n=$(( $n +1 ))
done
