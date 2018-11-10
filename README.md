On chain trollbox for cc activated KMD assetchains based on oracles contract

## Dependencies/Prerequisites :
Komodo asset chains with oracles contract already running with `-pubkey=` set at startup. It is recommend to use a freshly created address. 

For the time being, komodod must be blackjok3r branch of StakedChain/komodo or FSM branch of jl777/komodo

The default komodo data directory is set to `$home/.komodo`. If this is not correct for your machine, change ac_dir in getconf.py. 

python3 and requests installed 
```shell 
sudo apt-get install python3 python3-pip libssl-dev
pip3 install python-bitcoinlib
pip3 install requests
```

## Tutorial
These examples will use CFEK, but this will work on any chain with oracles contract activated.

Clone this repo
```shell
git clone https://github.com/StakedChain/trollbox
cd trollbox
```

Set your display name
```shell
./setusername.py CFEK <username> <password>
```

List rooms or create a new one
```shell
./listrooms.py
Chain:CFEK
```
```shell
./createroom.py 
Chain:CFEK
Roomname:<ROOMNAME>
```
After creating a room, creator must register to it and send a message. The listrooms.py script will show the latest message from the creator pubkey for each room. This allows the room creator to update the description dynamically just by sending a message from creator pubkey. This means the creator pubkey should not be used for chat. It should only be used to update what is shown in listrooms output. Rooms will not appear in listrooms until creator has sent a message.

Register to a room, use the output of listrooms or createroom to find an oracletxid
```shell
./register CFEK <oracletxid>
```

Wait for oraclessubscribe txs to confirm, open send script
```shell
./send.py CFEK <oracletxid>
```

Open another shell and start receive script
```shell
./receive CFEK <oracletxid>
```
