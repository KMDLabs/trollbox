#!/usr/bin/env python3
"""
argument 1 is chain
arg 2 is oracle txid, find these via oracleslist command
arg 3 is length of pubkey to show.
Usernames can be impersonated, pubkeys cannot
"""
import sys
import time
import codecs
import pprint
import ast
from datetime import datetime
import getconf
import bitcoin
from conf import CoinParams
from bitcoin.wallet import P2PKHBitcoinAddress
from bitcoin.core import x

VERLEN = '10' or sys.argv[3]
ORCLID = sys.argv[2]
CHAIN = sys.argv[1]
RPCURL = getconf.def_credentials(CHAIN)
bitcoin.params = CoinParams

# main loop
latest_printed = {}
latest_messgs = {}

while True:
    # for testing
    # dummy = input("Type message: ")

    # iterate over latest_batontxids
    latest_batontxids = getconf.get_latest_batontxids(CHAIN, ORCLID)
    # print(latest_batontxids)
    for publisher_id in latest_batontxids:

        # get samples
        batontxid = latest_batontxids[publisher_id]
        # oraclessamples_result = get_oracle_samples(batontxid)
        oraclessamples_result = getconf.oraclessamples_rpc(
            CHAIN,
            ORCLID,
            batontxid,
            str(1))
        oraclessamples_result = getconf.oraclessamples_rpc(
            CHAIN,
            ORCLID,
            batontxid,
            str(1))

        # print('oraclessamples_result', oraclessamples_result['samples'][0])
        # ignore empty messages
        if not oraclessamples_result['samples']:
            continue
        else:
            latest_messgs[publisher_id] = oraclessamples_result['samples'][0][0]

        # print messages if they have updated
        try:
            if latest_printed[publisher_id] != latest_messgs[publisher_id]:
                message_list = ast.literal_eval(latest_messgs[publisher_id])
                # print(message_dict)
                kvsearch_result = getconf.kvsearch_rpc(CHAIN, publisher_id)
                # print('kvsearch_result', kvsearch_result)

                # if username is set via KV show it
                if 'value' in kvsearch_result:
                    addr = str(P2PKHBitcoinAddress.from_pubkey(x(publisher_id)))
                    # check if username is signed properly
                    signature = kvsearch_result['value'][:88]
                    value = kvsearch_result['value'][88:]
                    verifymessage_result = getconf.verifymessage_rpc(CHAIN, addr, signature, value)
                    if verifymessage_result:
                        print(datetime.utcfromtimestamp(message_list[0]).strftime('%D %H:%M') + '[' + kvsearch_result['value'][88:] + '-' + publisher_id[0:int(VERLEN)] + ']:' + message_list[1])
                    else:
                        print('IMPROPER SIGNATURE', datetime.utcfromtimestamp(message_list[0]).strftime('%D %H:%M') + '[' + kvsearch_result['value'][88:] + '-' + publisher_id[0:int(VERLEN)] + ']:' + message_list[1])
                else:
                    # print('w', latest_messgs[publisher_id])
                    print(datetime.utcfromtimestamp(message_list[0]).strftime('%D %H:%M') + '[' + publisher_id[0:int(VERLEN)] + ']:' + message_list[1])

                latest_printed[publisher_id] = latest_messgs[publisher_id]
        except:
            latest_printed[publisher_id] = latest_messgs[publisher_id]

