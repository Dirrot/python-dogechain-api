'''
Created on 21.01.2014

@author: Dirk Rother
@contact: dirrot@web.de
@license: GPL
@version: 0.1

'''

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