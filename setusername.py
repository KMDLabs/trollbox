#!/usr/bin/env python3
import sys
import getconf
import pprint

CHAIN = sys.argv[1]
#PUBKEY = sys.argv[2]
VALUE = sys.argv[2]
PASSWORD = sys.argv[3]
pubkey = getconf.getpubkey_rpc(CHAIN)

#try:
kvupdate_result = getconf.kvupdate_rpc(CHAIN, pubkey, VALUE, 100, PASSWORD)
pprint.pprint(kvupdate_result['result'])

#except:
#    kvupdate_result = kvupdate_rpc(pubkey, VALUE, 100, PASSWORD)
#    print(kvupdate_result['error'])

