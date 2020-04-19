api = {
  'key': '00c5d9ca4de7403889beb4beca08c1d3',
  'url': 'https://api.nytimes.com/svc/search/v2/articlesearch.json'
}

# This python script handles news api request
#created 4/2/2020
# Last Updated: 4/3/2020
# Credits:nóto

#Import request and parse from urllib so we can request from the api
from urllib import request as req
from urllib import parse
#Import json to manipulate api data
import json

class NewsApi():
    def __init__(self):
        self.url = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
        self.apiKey = '8ybuxiDjnm5V9WxJj3XSLGYzB5FIAqIm'
    
    def createQuery(self, ticker):
        self.queryParam = {
            "q":str(ticker),
            "apikey": str(self.apiKey)           
        }
        self.parseQuery()
    #END

    def parseQuery(self):
        #parse the api paramaters
        self.queryParam = parse.urlencode(self.queryParam)
        #create the api url query string
        self.query = self.url + "everything?" + self.queryParam
    #END

    def retrieveQuery(self):
        #query the srtring and the store api's response
        self.apiResp = req.urlopen(self.query)
        #if connection is connected
        if(self.apiResp.isclosed() == False):
            #Store json Data
            self.json = json.load(self.apiResp)
        else:
            raise ValueError('Error: Api Connection Failed')
    #END

    #to make life easy :)
    def autoQuery(self, t):
        self.createQuery(t)
        self.retrieveQuery()
        return(self.json)
    #END