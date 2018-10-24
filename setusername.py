#!/usr/bin/env python3
import sys
import getconf
import pprint

CHAIN = sys.argv[1]
#PUBKEY = sys.argv[2]
VALUE = sys.argv[2]
PASSWORD = sys.argv[3]
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


# create getinfo payload
getinfo_payload = {
    "jsonrpc": "1.0",
    "id": "python",
    "method": "getinfo",
    "params": []}

getinfo_result = getconf.post_rpc(RPCURL, getinfo_payload)
#print(getinfo_result)
#TODO error if pubkey isn't set
pubkey = getinfo_result['result']['pubkey']


#try:
kvupdate_result = kvupdate_rpc(pubkey, VALUE, 100, PASSWORD)
pprint.pprint(kvupdate_result['result'])

#except:
#    kvupdate_result = kvupdate_rpc(pubkey, VALUE, 100, PASSWORD)
#    print(kvupdate_result['error'])

