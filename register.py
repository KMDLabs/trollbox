#!/usr/bin/env python3
#oraclesregister oracletxid datafee
#-ac_name=STAKEDED gettransaction 58200ac8742537be73b7dc4f9b0f07548b478c78972e5b3da7a9163b4aeaf0ac
#oraclessubscribe oracletxid publisher amount
import sys
import getconf

CHAIN = sys.argv[1]
ORCLID = sys.argv[2]
UTXOS = '10' or sys.argv[3]
AMOUNT = '1' or sys.argv[4]
DATAFEE = '10000' or sys.argv[5]
PUBKEY = getconf.getpubkey_rpc(CHAIN)

oraclesregister_result = getconf.oraclesregister_rpc(CHAIN, ORCLID, DATAFEE)
rawtx = oraclesregister_result['hex']
sendraw_result = getconf.sendrawtx_rpc(CHAIN, rawtx)
print('oraclesregister:', sendraw_result['result'])

oraclesregister_txid = sendraw_result['result']

for i in range(int(UTXOS)):

    try:
        subscribe_result = getconf.oraclessubscribe_rpc(CHAIN, ORCLID, PUBKEY, AMOUNT)
        #print(subscribe_result)
        rawtx = subscribe_result['hex']
        sendraw_result = getconf.sendrawtx_rpc(CHAIN, rawtx)
        print('oraclessubscribe:', sendraw_result['result'])

    except:
        subscribe_result = getconf.oraclessubscribe_rpc(CHAIN, ORCLID, PUBKEY, AMOUNT)
        print(subscribe_result['error'])

print('wait for oraclessubscribe transactions to confirm before attempting to send message')
