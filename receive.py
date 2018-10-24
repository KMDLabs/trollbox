#!/usr/bin/env python3
"""
argument 1 is chain  
arg 2 is oracle txid, find these via oracleslist command
arg 3 is length of pubkey to show. Usernames can be impersonated, pubkeys cannot
""" 
import sys
import time
import codecs
import pprint
import ast
from datetime import datetime
from getconf import *

VERLEN = sys.argv[3]
ORCLID = sys.argv[2]
CHAIN = sys.argv[1]
RPCURL = def_credentials(CHAIN)


def get_latest_batontxids():
    # create orclinfo payload
    orclinfopayload = {
        "jsonrpc": "1.0",
        "id": "python",
        "method": "oraclesinfo",
        "params": [ORCLID]}
    # make oraclesdata rpc call
    orclinfo_result = post_rpc(RPCURL, orclinfopayload)
    latest_batontxids = {}
    # fill "latest_batontxids" dictionary with publisher:batontxid data
    for i in orclinfo_result['result']['registered']:
        latest_batontxids[i['publisher']] = i['batontxid']
    return(latest_batontxids)


def get_oracle_samples(batontxid):
    # create dynamic oraclessamples payload
    orclsamples_payload = {
        "jsonrpc": "1.0",
        "id": "python",
        "method": "oraclessamples",
        "params": [
            ORCLID,
            batontxid,
            str(1)
        ]
    }
    # make oraclessamples rpc call
    orclsamples_result = post_rpc(RPCURL, orclsamples_payload)
    samples = orclsamples_result['result']['samples']
    return(samples)

def kvsearch_rpc(key):
    kvsearch_payload = {
        "jsonrpc": "1.0",
        "id": "python",
        "method": "kvsearch",
        "params": [
            key
        ]
    }
    
    kvsearch_result = post_rpc(RPCURL, kvsearch_payload)
    return(kvsearch_result['result'])

# main loop
latest_printed = {}
latest_messgs = {}
new_value = ''
while True:
    # for testing
    #message = input("Type message: ")

    # iterate over latest_batontxids
    latest_batontxids = get_latest_batontxids()
    #print(latest_batontxids)
    for publisher_id in latest_batontxids:

        # get samples
        batontxid = latest_batontxids[publisher_id]
        samples = get_oracle_samples(batontxid)
        
        # ignore empty messages
        if not samples:
             continue
        else:
             latest_messgs[publisher_id] = samples[0][0]
        
        # print messages if they have updated
        try:
            if latest_printed[publisher_id] != latest_messgs[publisher_id]:
                message_dict = ast.literal_eval(latest_messgs[publisher_id])
                kvsearch = kvsearch_rpc(publisher_id)

                # if username is set via KV show it
                if 'value' in kvsearch:
                    #print(kvsearch['value'])
                    print(datetime.utcfromtimestamp(message_dict['t']).strftime('%D %H:%M') + '[' + kvsearch['value'] + '-' + publisher_id[0:int(VERLEN)] + ']:' + message_dict['m'])
                else:
                    print(datetime.utcfromtimestamp(message_dict['t']).strftime('%D %H:%M') + '[' + publisher_id[0:int(VERLEN)] + ']:' + message_dict['m'])

                latest_printed[publisher_id] = latest_messgs[publisher_id]
        except:
            latest_printed[publisher_id] = latest_messgs[publisher_id]
            #print('what')

