#!/usr/bin/env python3
#pip3 install python-bitcoinlib
import sys
import getconf
import pprint
import bitcoin
import ast
from conf import CoinParams
from bitcoin.wallet import P2PKHBitcoinAddress
from bitcoin.core import x

CHAIN = sys.argv[1]
#PUBKEY = sys.argv[2]
USERNAME = sys.argv[2]
PASSWORD = sys.argv[3]
pubkey = getconf.getpubkey_rpc(CHAIN)
bitcoin.params = CoinParams

addr = str(P2PKHBitcoinAddress.from_pubkey(x(pubkey)))
print(addr)

signmessage_result = getconf.signmessage_rpc(CHAIN, addr, USERNAME)
print('whataa', signmessage_result)

value = signmessage_result + USERNAME
print(value)
#try:
kvupdate_result = getconf.kvupdate_rpc(CHAIN, pubkey, value, 100, PASSWORD)
pprint.pprint(kvupdate_result['result'])

#except:
#    kvupdate_result = kvupdate_rpc(pubkey, VALUE, 100, PASSWORD)
#    print(kvupdate_result['error'])

