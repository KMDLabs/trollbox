#!/usr/bin/env python3
import sys
import getconf

CHAIN = sys.argv[1]
ORCLID = sys.argv[2]
PUBKEY = sys.argv[3]
RPCURL = getconf.def_credentials(CHAIN)

def oraclessubscribe_rpc(ROOM_TXID):
    # create oraclessubscribe payload
    oraclessubscribe_payload = {
        "jsonrpc": "1.0",
        "id": "python",
        "method": "oraclessubscribe",
        "params": [
            ROOM_TXID,
            PUBKEY,
            str(1)]}
    # make oraclessubscribe rpc call
    oraclessubscribe_result = getconf.post_rpc(RPCURL, oraclessubscribe_payload)
    return(oraclessubscribe_result['result'])

# define sendrawtransaction rpc
def sendrawtx_rpc(RPCURL, rawtx):
    sendrawpayload = {
        "jsonrpc": "1.0",
        "id": "python",
        "method": "sendrawtransaction",
        "params": [rawtx]}
    return(getconf.post_rpc(RPCURL, sendrawpayload))

subscribe_result = oraclessubscribe_rpc(ORCLID)
rawtx = subscribe_result['hex']
sendraw_result = sendrawtx_rpc(RPCURL, rawtx)
print(sendraw_result)

