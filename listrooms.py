#!/usr/bin/env python3
import sys
import getconf

# construct daemon url

CHAIN = sys.argv[1]
RPCURL = getconf.def_credentials(CHAIN)

def get_oracleinfo(orclid):
    # create orclinfo payload
    orclinfopayload = {
        "jsonrpc": "1.0",
        "id": "python",
        "method": "oraclesinfo",
        "params": [orclid]}
    # make oraclesdata rpc call
    oracleinfo_result = getconf.post_rpc(RPCURL, orclinfopayload)
    return(oracleinfo_result['result'])


oracleslistpayload = {
        "jsonrpc": "1.0",
        "id": "python",
        "method": "oracleslist",
        "params": []}
oraclelist_result = getconf.post_rpc(RPCURL, oracleslistpayload)
#print(oraclelist_result['result'])
#print(type(oraclelist_result['result']))
sample = oraclelist_result['result']

for oracle_txid in sample:
    hello = get_oracleinfo(oracle_txid)
    description = hello['description']
    name = hello['name']
    #print(description[0:4])
    if description[0:4] == 'CHAT':
       print('[' + name + ': ' + description[5:] + ']: ' + oracle_txid)
