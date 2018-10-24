#!/usr/bin/env python3

import sys
import getconf

CHAIN = sys.argv[1]
ROOM_TXID = sys.argv[2]
RPCURL = getconf.def_credentials(CHAIN)

def oraclesregister_rpc(ROOM_TXID):
    # create dynamic oraclessamples payload
    oraclesregister_payload = {
        "jsonrpc": "1.0",
        "id": "python",
        "method": "oraclesregister",
        "params": [
            ROOM_TXID,
            str(10000)]}
    # make oraclessamples rpc call
    oraclesregister_result = getconf.post_rpc(RPCURL, oraclesregister_payload)
    return(oraclesregister_result['result'])

# define sendrawtransaction rpc
def sendrawtx_rpc(RPCURL, rawtx):
    sendrawpayload = {
        "jsonrpc": "1.0",
        "id": "python",
        "method": "sendrawtransaction",
        "params": [rawtx]}
    return(getconf.post_rpc(RPCURL, sendrawpayload))

try:
    oraclesregister_result = oraclesregister_rpc(ROOM_TXID)
    rawtx = oraclesregister_result['hex']
    sendraw_result = sendrawtx_rpc(RPCURL, rawtx)
    print(sendraw_result)

except:
    oraclesregister_result = oraclesregister_rpc(ROOM_TXID)
    print(oraclesregister_result['error'])

