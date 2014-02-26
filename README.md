python-dogechain-api
=========================

This is a python wrapper class for the dogechain.info api.

 http://dogechain.info/chain/Dogecoin/q
 
___________________________________________________
 
_Methods_
* addressbalance - amount ever received minus amount ever sent by a given address.
* addresstohash - shows the public key hash encoded in an address.
* checkaddress - checks an address for validity.
* decode_address - shows the version prefix and hash encoded in an address.
* getblockcount - shows the current block number.
* getdifficulty - shows the last solved block's difficulty.
* getreceivedbyaddress - shows the amount ever received by a given address.
* getsentbyaddress - shows the amount ever sent from a given address.
* hashtoaddress - shows the address with the given version prefix and hash.
* nethash - shows statistics about difficulty and network power.
* totalbc - shows the amount of currency ever mined.
* transactions - shows the amount transactions of the last blocks.

___________________________________________________

_Install_
```bash
sudo pip install DogechainApi
```

___________________________________________________

Here's an example:

```python
from DogechainInfoApi import API

if __name__ == '__main__':
    
    address = 'YOUR WALLET ADDRESS'
    
    api = API()
    
    balance = api.addressbalance(address)
    print 'Balance: ', balance
    
    addresstohash = api.addresstohash(address)
    print 'AddressToHash: ', addresstohash
    
    checkaddress = api.checkaddress(address)
    print 'CheckAddress: ', checkaddress
    
    decodeaddress = api.decode_address(address)
    print 'DecodeAddress: ', decodeaddress
    
    blockcount = api.getblockcount()
    print 'BlockCount: ', blockcount
    
    difficulty = api.getdifficulty()
    print 'Difficulty: ', difficulty
    
    receivedbyaddress = api.getreceivedbyaddress(address)
    print 'ReceivedByAddress: ', receivedbyaddress
    
    sentbyaddress = api.getsentbyaddress(address)
    print 'SendByAddress: ', sentbyaddress
    
    hashtoaddress = api.hashtoaddress(api.addresstohash(address))
    print 'HashToAddress', hashtoaddress
    
    nethash = api.nethash()
    print 'Nethash: ', nethash
    
    totalbc = api.totalbc()
    print 'TotalBalance: ', totalbc
    
    transactions = api.transactions()
    print 'Transactions', transactions
```

___________________________________________________

**Please donate to "DQ6mBVyuboTGwS8JYW11oHwXtxsjNAzkzi" [DOGECOIN]** 

!["Dogecoin Donation QR-Code"](http://github.com/Dirrot/python-dogechain.info-api/blob/master/img/donation-qr-code.png?raw=true)
