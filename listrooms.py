#!/usr/bin/env python3
import sys
import getconf

# construct daemon url

CHAIN = sys.argv[1]
RPCURL = getconf.def_credentials(CHAIN)

oraclelist_result = getconf.oracleslist_rpc(CHAIN)

for oracle_txid in oraclelist_result:
    oraclesinfo_result = getconf.oraclesinfo_rpc(CHAIN, oracle_txid)
    description = oraclesinfo_result['description']
    name = oraclesinfo_result['name']
    if description[0:4] == 'CHAT':
       print('[' + name + ': ' + description[5:] + ']: ' + oracle_txid)
