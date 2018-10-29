#!/usr/bin/env python3
import sys
import codecs
import requests
import time
import getconf
import readline

ORCLID = sys.argv[2]
CHAIN = sys.argv[1]

while True:
    message = "[" + str(int(time.time())) + " ,\"" + input("Type message: ") + "\"]"
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

    #print(fullhex)
    oraclesdata_result = getconf.oraclesdata_rpc(CHAIN, ORCLID, fullhex)
    #print(oraclesdata_result)
    result = oraclesdata_result['result']
    if result == 'error':
        print('ERROR:' + oraclesdata_result['error'] + ', try using oraclesregister if you have not already')
        continue
    rawtx = oraclesdata_result['hex']

    sendrawtx_result = getconf.sendrawtx_rpc(CHAIN, rawtx)
    #print(sendrawtx_result)
