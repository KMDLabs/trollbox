#!/usr/bin/env python3
import sys
import getconf

CHAIN = input('Chain:')
ROOMNAME = input('Roomname:')
DESCRIPTION = 'DCHAT ' + getconf.getpubkey_rpc(CHAIN)



try:
    create_result = getconf.oraclescreate_rpc(CHAIN, ROOMNAME, DESCRIPTION, 'S')
    sendraw_result = getconf.sendrawtx_rpc(CHAIN, create_result['hex'])
    print(sendraw_result)
except:
    create_result = getconf.oraclescreate_rpc(CHAIN, ROOMNAME, DESCRIPTION, 'S')
    print(create_result['error'])
