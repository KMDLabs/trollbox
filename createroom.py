#!/usr/bin/env python3
#oraclescreate name description format
import sys
import getconf

CHAIN = sys.argv[1]
ROOMNAME = sys.argv[2]
DESCRIPTION = sys.argv[3]
RPCURL = getconf.def_credentials(CHAIN)

def oraclescreate_rpc(name, description):
    # create dynamic oraclessamples payload
    description = "CHAT " + description
    oraclescreate_payload = {
        "jsonrpc": "1.0",
        "id": "python",
        "method": "oraclescreate",
        "params": [
            name,
            description,
            'S']}
    # make oraclessamples rpc call
    oraclescreate_result = getconf.post_rpc(RPCURL, oraclescreate_payload)
    return(oraclescreate_result['result'])

# define sendrawtransaction rpc
def sendrawtx_rpc(RPCURL, rawtx):
    sendrawpayload = {
        "jsonrpc": "1.0",
        "id": "python",
        "method": "sendrawtransaction",
        "params": [rawtx]}
    return(getconf.post_rpc(RPCURL, sendrawpayload))

create_result = oraclescreate_rpc(ROOMNAME, DESCRIPTION)
sendraw_result = sendrawtx_rpc(RPCURL, create_result['hex'])
print(sendraw_result)
