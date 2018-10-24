#!/usr/bin/env python3
import re
import os
import requests
import json

def def_credentials(chain):

    #TODO: add osx/windows support for ac_dir
    ac_dir = os.environ['HOME'] + '/.komodo'

    # define config file path
    if chain == 'KMD':
        coin_config_file = str(ac_dir + '/komodo.conf')
    else:
        coin_config_file = str(ac_dir + '/' + chain + '/' + chain + '.conf')
    #define rpc creds
    with open(coin_config_file, 'r') as f:
        #print("Reading config file for credentials:", coin_config_file)
        for line in f:
            l = line.rstrip()
            if re.search('rpcuser', l):
                rpcuser = l.replace('rpcuser=', '')
            elif re.search('rpcpassword', l):
                rpcpassword = l.replace('rpcpassword=', '')
            elif re.search('rpcport', l):
                rpcport = l.replace('rpcport=', '')
    return('http://' + rpcuser + ':' + rpcpassword + '@127.0.0.1:' + rpcport)

# define function that posts json data
def post_rpc(url, payload, auth=None):
    try:
        r = requests.post(url, data=json.dumps(payload), auth=auth)
        return(json.loads(r.text))
    except Exception as e:
        raise Exception("Couldn't connect to " + url + ": ", e)
