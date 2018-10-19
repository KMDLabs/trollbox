#!/usr/bin/env python3
import sys
import codecs
import subprocess
import requests
import json
import time
from getconf import *

orclid = sys.argv[2]
chain = sys.argv[1]


# construct daemon url
rpcurl = def_credentials(chain)

# define function that posts json data
def post_rpc(url, payload, auth=None):
    try:
        r = requests.post(url, data=json.dumps(payload), auth=auth)
        return(json.loads(r.text))
    except Exception as e:
        raise Exception("Couldn't connect to " + url + ": ", e)

while True:
    message = "\"" + str(int(time.time())) + "." + input("Type message: ") + "\""

    #convert message to hex
    rawhex = codecs.encode(message).hex()

    #get length in bytes of hex in decimal
    bytelen = int(len(rawhex) / int(2))
    hexlen = format(bytelen, 'x')

    #get length in big endian hex
    if bytelen < 16:
        bigend = "000" + str(hexlen)
    elif bytelen < 256:
        bigend = "00" + str(hexlen)
    elif bytelen < 4096:
        bigend = "0" + str(hexlen)
    elif bytelen < 65536:
        bigend = str(hexlen)
    else:
        print("message too large, must be less than 65536 characters")
        continue

    #convert big endian length to little endian, append rawhex to little endian length
    lilend = bigend[2] + bigend[3] + bigend[0] + bigend[1]
    fullhex = lilend + rawhex

    orclpayload = {
        "jsonrpc": "1.0",
        "id": "python",
        "method": "oraclesdata",
        "params": [orclid, fullhex]}

    # make oraclesdata rpc call, assign result to rawtx
    call_result = post_rpc(rpcurl, orclpayload)
    rawtx = call_result['result']['hex']
    
    sendrawpayload = {
        "jsonrpc": "1.0",
        "id": "python",
        "method": "sendrawtransaction",
        "params": [rawtx]}
    #send raw tx
    post_rpc(rpcurl, sendrawpayload)

