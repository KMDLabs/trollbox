#!/usr/bin/env python3
import sys
import getconf

CHAIN = sys.argv[1]
ROOMNAME = sys.argv[2]
DESCRIPTION = 'CHAT ' + sys.argv[3]
RPCURL = getconf.def_credentials(CHAIN)

try:
    create_result = getconf.oraclescreate_rpc(CHAIN, ROOMNAME, DESCRIPTION, 'S')
    sendraw_result = getconf.sendrawtx_rpc(CHAIN, create_result['hex'])
    print(sendraw_result)
except:
    create_result = getconf.oraclescreate_rpc(CHAIN, ROOMNAME, DESCRIPTION, 'S')
    print(create_result['error'])
