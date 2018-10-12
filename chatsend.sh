#!/bin/bash
orclid=$2
chain=$1
while true; do
read -rp "type message: " message
echo "$message" > msg
xxd -p msg | tr -d '\n' > rawhex
hexraw=$(cat rawhex)
declen=$(($(xxd -p msg | tr -d '\n' | wc -c) / 2 ))
if [ $declen -lt 16 ]; then
        hexlen=$(echo "000$(printf '%x\n' $declen)")
elif [ $declen -lt 256 ]; then
        hexlen=$(echo "00$(printf '%x\n' $declen)")
elif [ $declen -lt 4096 ]; then
        hexlen=$(echo "0$(printf '%x\n' $declen)")
else
        hexlen=$(printf '%x\n' $declen)
fi
len=$(echo ${hexlen:2:2}${hexlen:0:2})
rawtx=$(komodo-cli -ac_name=$chain oraclesdata $orclid $len$hexraw | jq -r .hex)
komodo-cli -ac_name=$chain sendrawtransaction $rawtx > /dev/null
done
