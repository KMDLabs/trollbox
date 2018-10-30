#!/usr/bin/env python3
# NOT READY, need to rethink the logic of this
import sys
import getconf
import ast
from datetime import datetime

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
            str(10)
        ]
    }
    # make oraclessamples rpc call
    orclsamples_result = getconf.post_rpc(RPCURL, orclsamples_payload)
    samples = orclsamples_result['result']['samples']
    return(samples)

#mydict.sort(key=lambda x:x['Timestamp'])


latest_batontxids = get_latest_batontxids()

fullmsg_dict = {}
a = 0
message_lists = []
hello = 0

for publisher_id in latest_batontxids:
    # get samples
    #print(publisher_id)
    batontxid = latest_batontxids[publisher_id]
    samples = get_oracle_samples(ORCLID, batontxid, str(HISTORY))
    
    
    for message in samples:
        #print(message[0])
        #print(message[0][0])
        #print(hello)
        blah = ast.literal_eval(message[0])
        fullmsg_dict[blah[0]] = blah[1]
        #print(str(blah[0]) + '.' + str(blah[1]))
        #print(type(blah[hello]))
        hello = hello + 1


sorted_messages = sorted(fullmsg_dict.items())
print(sorted_messages)
#print(type(sorted_messages))
for i in sorted_messages:
    print(i)
    #print(publisher_id)
    #print(sorted_messages[i][0])
    #print(sorted_messages[0][i])
#print(sorted_messages[3][0])
#print(type(sorted_messages[3][0]))
#for key in sorted(fullmsg_dict.items()):
 #   print(key)
  #  print("%s: %s" % (key, fullmsg_dict[key]))

#mydict.sort(key=lambda x:x['Timestamp'])
#thisdict["color"] = "red"
   # print('samples', samples)
   # print('samples[0]', samples[2])
   # print('sampels[0][0]', samples[0][0])
    
    #0 is timestamp, 1 is message 
    #print(publisher_id)
    #message_lists.insert(1, ast.literal_eval(samples[0][0]))
    #print(message_list[0])
    #print(type(message_list))
    #print(publisher_id)
    #a = a + 1

#for 
#print(message_lists[0][0])
#print(message_lists[0][1])
#print(message_lists[1][1])
#print(message_lists)

#for message in message_lists:
    #print( datetime.utcfromtimestamp(message[0]).strftime('%D %H:%M'))
    #print(message[1])
 #  print('time', message_list[0])
  # print('message', message_list[1])
        #print('what', i[0])
        #print(type(i[0]))
        #print(i)
        #print(type(i))
        #print(i[1])
        #print(i[1])
        #message_time = ast.literal_eval(i[0])
        #message = ast.literal_eval(i[1])
        #for message_timestamp in message_list:
          #  print(message_timestamp)
           # print(message)
            #print(g)
            #message_list[g] = i['batontxid']
        #a.update(what)
        #print(what)
        #print(type(what))
        
    #print(a)
    #msg_dict = ast.literal_eval(samples[0][0])
    #fullmsg_dict = {**msg_dict, **fullmsg_dict}
    #print('msgdict', msg_dict)
    #print('fullmsg', fullmsg_dict)
    #print(fullmsg_dict)
    #print(type(fullmsg_dict))
    #print(msg_dict['t'])
    #print(type(msg_dict))
#oraclessamples_result = get_oracle_samples(ORCLID, 
