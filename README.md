On chain trollbox for cc activated KMD assetchains based on oracles contract

## Dependencies/Prerequisites :
Komodo asset chains with oracles contract already running with `-pubkey=` set at startup. It is recommend to use a freshly created address. 

The default komodo data directory is set to `$home/.komodo`. If this is not correct for your machine, change ac_dir in getconf.py. 

python3 and requests installed 
```shell 
sudo apt-get install python3 python3-pip libssl-dev
pip3 install python-bitcoinlib
pip3 install requests
```

## Tutorial
These examples will use STAKEDW1, but this will work on any chain with oracles contract activated.

Clone this repo
```shell
git clone https://github.com/StakedChain/trollbox
cd trollbox
```

Set your display name
```shell
./setusername.py STAKEDW1 <username> <password>
```

List rooms or create a new one
```shell
./listrooms.py STAKEDW1
```
```shell
./createroom.py STAKEDW1 <ROOMNAME> <DESCRIPTION>
```

Register to a room, use the output of listrooms to find an oracletxid
```shell
./register STAKEDW1 <oracletxid>
```

Wait for oraclessubscribe txs to confirm, open send script
```shell
./send.py STAKEDW1 <oracletxid>
```

Open another shell and start receive script
```shell
./receive STAKEDW1 <oracletxid>
```
