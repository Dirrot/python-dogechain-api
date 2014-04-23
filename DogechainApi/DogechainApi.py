#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 21.01.2014

@author: Dirk Rother
@contact: dirrot@web.de
@license: GPL
@version: 0.1


modified by @c0ding
  - added network hashrate

'''

from urllib2 import Request, urlopen, URLError, HTTPError

class API(object):
    '''
    This class is a wrapper class for the dogechain.info api.
    '''
    
    API_PATH = "http://www.dogechain.info/chain/Dogecoin/"
    API_QUERY = API_PATH + "q/"
        
    def addressbalance(self, address):
        '''
        Amount ever received minus amount ever sent by a given address.
        Usage: API_QUERY + addressbalance/ADDRESS
        '''
        url = self.API_QUERY + 'addressbalance/' + address
        return self._getdata(url)
    
    def addresstohash(self, address):
        '''
        Shows the public key hash encoded in an address.
        Usage: API_QUERY + addresstohash/ADDRESS
        '''
        url = self.API_QUERY + 'addresstohash/' + address
        return self._getdata(url)
    
    def checkaddress(self, address):
        '''
        Checks an address for validity.
        Usage: API_QUERY + checkaddress/ADDRESS
        '''
        url = self.API_QUERY + 'checkaddress/' + address
        return self._getdata(url)
    
    def decode_address(self, address):
        '''
        Shows the version prefix and hash encoded in an address.
        Usage: API_QUERY + decode_address/ADDRESS
        '''
        url = self.API_QUERY + 'decode_address/' + address
        return self._getdata(url)
    
    def getblockcount(self):
        '''
        Shows the current block number.
        Usage: API_QUERY + getblockcount
        '''
        url = self.API_QUERY + 'getblockcount'
        return self._getdata(url)
    
    def getdifficulty(self):
        '''
        Shows the last solved block"s difficulty.
        Usage: API_QUERY + getdifficulty
        '''
        url = self.API_QUERY + 'getdifficulty'
        return self._getdata(url)
    
    def getreceivedbyaddress(self, address):
        '''
        Shows the amount ever received from a given address.
        (not balance, sends are not subtracted)
        Usage: API_QUERY + getreceivedbyaddress/ADDRESS
        '''
        url = self.API_QUERY + 'getreceivedbyaddress/' + address
        return self._getdata(url)
    
    def getsentbyaddress(self, address):
        '''
        Shows the amount ever sent from a given address.
        Usage: API_QUERY + getsentbyaddress/ADDRESS
        '''
        url = self.API_QUERY + 'getsentbyaddress/' + address
        return self._getdata(url)
	
    def hashrate(self):
        '''
            Shows network hashrate.
            Usage: API_QUERY + nethash + last_block
        '''
        
        blocks = self.getblockcount()
        url = self.API_QUERY + 'nethash/' + blocks + '?format=json'
        data = self._getdata(url)
        clean_data = data.strip('[]')
        split_data = clean_data.split(',')
        return split_data[4]
    
    def hashtoaddress(self, hash):
        '''
        Shows the address with the given version prefix an hash.
        Converts a 160-bit hash and address version to an address.
        Usage: API_QUERY + hashtoaddress/HASH
        '''
        url = self.API_QUERY + 'hashtoaddress/' + hash
        return self._getdata(url)
    
    def nethash(self):
        '''
        Shows statistics about difficulty and network power.
        Usage: API_QUERY + nethash
        '''
        url = self.API_QUERY + 'nethash'
        return self._getdata(url)
    
    def totalbc(self):
        '''
        Shows the amount of currency ever mined.
        Usage: API_QUERY + totalbc
        '''
        url = self.API_QUERY + 'totalbc'
        return self._getdata(url)
    
    def transactions(self):
        '''
        Shows the amount transactions of the last blocks.
        Usage: API_QUERY + transactions
        '''
        url = self.API_QUERY + 'transactions'
        return self._getdata(url)
    
    def _getdata(self, url):
        '''
        Wrapper method
        '''
        request = Request(url)
        try:
            response = urlopen(request)
        except HTTPError as e:
            print 'The Server couldn\'t fulfill the request.'
            print 'Error code: ', e.code
        except URLError as e:
            print 'We failed to reach a server.'
            print 'Reason: ', e.code
        else:
            # Everything is fine.
            return response.read()
