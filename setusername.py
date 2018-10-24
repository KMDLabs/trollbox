#!/usr/bin/env python3
import sys
import getconf

CHAIN = sys.argv[1]
PUBKEY = sys.argv[2]
VALUE = sys.argv[3]
PASSWORD = sys.argv[4]
RPCURL = getconf.def_credentials(CHAIN)

def kvupdate_rpc(key, value, days, password):
    # create dynamic oraclessamples payload
    kvupdate_payload = {
        "jsonrpc": "1.0",
        "id": "python",
        "method": "kvupdate",
        "params": [
            key,
            value,
            str(days),
            password]}
    # make kvupdate rpc call
    kvupdate_result = getconf.post_rpc(RPCURL, kvupdate_payload)
    return(kvupdate_result)

try:
    kvupdate_result = kvupdate_rpc(PUBKEY, VALUE, 100, PASSWORD)
    rawtx = kvupdate_result['hex']
    sendraw_result = sendrawtx_rpc(RPCURL, rawtx)
except:
    kvupdate_result = kvupdate_rpc(PUBKEY, VALUE, 100, PASSWORD)
    print(kvupdate_result['error'])

