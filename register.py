#!/usr/bin/env python3
#oraclesregister oracletxid datafee
#-ac_name=STAKEDED gettransaction 58200ac8742537be73b7dc4f9b0f07548b478c78972e5b3da7a9163b4aeaf0ac
#oraclessubscribe oracletxid publisher amount
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

def oraclesregister_rpc(ORCLID):
    # create dynamic oraclessamples payload
    oraclesregister_payload = {
        "jsonrpc": "1.0",
        "id": "python",
        "method": "oraclesregister",
        "params": [
            ORCLID,
            str(10000)]}
    # make oraclessamples rpc call
    oraclesregister_result = getconf.post_rpc(RPCURL, oraclesregister_payload)
    return(oraclesregister_result['result'])

# create getinfo payload
getinfo_payload = {
    "jsonrpc": "1.0",
    "id": "python",
    "method": "getinfo",
    "params": []}

#getinfo_result = getconf.post_rpc(RPCURL, getinfo_payload)
#print(getinfo_result)
#TODO error if pubkey isn't set
#pubkey = getinfo_result['result']['pubkey']


oraclesregister_result = oraclesregister_rpc(ORCLID)
#print(oraclesregister_result)
rawtx = oraclesregister_result['hex']
#print(rawtx)
sendraw_result = getconf.sendrawtx_rpc(RPCURL, rawtx)
print('oraclesregister:', sendraw_result)

oraclesregister_txid = sendraw_result['result']


try:
    subscribe_result = oraclessubscribe_rpc(ORCLID)
    #print(subscribe_result)
    rawtx = subscribe_result['hex']
    sendraw_result = getconf.sendrawtx_rpc(RPCURL, rawtx)
    print('oraclessubscribe:', sendraw_result)

except:
    subscribe_result = oraclessubscribe_rpc(ORCLID)
    print(subscribe_result['error'])

