#!/usr/bin/env python3
import sys
import getconf
import ast


CHAIN = sys.argv[1]
ORCLID = sys.argv[2]
HISTORY = sys.argv[3]
RPCURL = getconf.def_credentials(CHAIN)

def get_latest_batontxids():
    # create orclinfo payload
    orclinfopayload = {
        "jsonrpc": "1.0",
        "id": "python",
        "method": "oraclesinfo",
        "params": [ORCLID]}
    # make oraclesdata rpc call
    orclinfo_result = getconf.post_rpc(RPCURL, orclinfopayload)
    latest_batontxids = {}
    # fill "latest_batontxids" dictionary with publisher:batontxid data
    for i in orclinfo_result['result']['registered']:
        latest_batontxids[i['publisher']] = i['batontxid']
    return(latest_batontxids)

def get_oracle_samples(ORCLID, batontxid, samples):
    # create dynamic oraclessamples payload
    orclsamples_payload = {
        "jsonrpc": "1.0",
        "id": "python",
        "method": "oraclessamples",
        "params": [
            ORCLID,
            batontxid,
            str(samples)
        ]
    }
    # make oraclessamples rpc call
    orclsamples_result = getconf.post_rpc(RPCURL, orclsamples_payload)
    samples = orclsamples_result['result']['samples']
    return(samples)

#mydict.sort(key=lambda x:x['Timestamp'])


latest_batontxids = get_latest_batontxids()

fullmsg_dict = {}

for publisher_id in latest_batontxids:
    # get samples
    #print(publisher_id)
    batontxid = latest_batontxids[publisher_id]
    samples = get_oracle_samples(ORCLID, batontxid, str(3))
    for i in samples:
        print(i[0])
        print(type(i[0]))
        what = ast.literal_eval(i[0])
        print(what)
        print(type(what))
    msg_dict = ast.literal_eval(samples[0][0])
    fullmsg_dict = {**msg_dict, **fullmsg_dict}
    #print('msgdict', msg_dict)
    #print('fullmsg', fullmsg_dict)
    #print(fullmsg_dict)
    #print(type(fullmsg_dict))
    #print(msg_dict['t'])
    #print(type(msg_dict))
#oraclessamples_result = get_oracle_samples(ORCLID, 
