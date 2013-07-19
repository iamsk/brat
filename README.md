    ____________________    ________________
    \______   \______   \  /  _  \__    ___/
     |    |  _/|       _/ /  /_\  \|    |   
     |    |   \|    |   \/    |    \    |   
     |______  /|____|_  /\____|__  /____|   
            \/        \/         \/          

A [framework|practice] of RESTful API based on Tornado

[![Build Status](https://secure.travis-ci.org/iamsk/brat.png?branch=master)](http://travis-ci.org/iamsk/brat)

##Installation

    git clone git@github.com:iamsk/brat.git
    cd brat
    python setup.py install

##Requirements

* python 2.6 or 2.7
* tornado
* ujson
* requests

##Minimal Demo

###$ more examples/miminal.py

    from brat import Brat
	from brat import BratHandler
	
	brat = Brat()
	
	
	class HelloWorld(BratHandler):
	    def get(self):
	        return {'hello': 'world'}
	
	brat.add_handler('/', HelloWorld)
	
	if __name__ == '__main__':
	    brat.run()

###$ python miminal.py

###$ curl http://localhost:7777/ -X GET

    {"hello": "world"}

##Completion Demo

    use buildout for building application

###$ ls examples/demo/src

    app.py used for the enter of the application
    views.py used for handlers of the application
    models.py used for data
    
###$ bin/doc_gen init & bin/doc_gen

    used for generate docs for api

1. write options method for each handler
2. change your docs/doc.conf

you will see doc at docs/doc.html
    
###$ curl http://localhost:7778/users -X POST -u test:test -d 'email=test1@gmail.com&password=test1'

    {"email":"test1@gmail.com","id":1,"password":"test1"}

###$ curl http://localhost:7778/users -X GET -u test:test

    {
         "paging":{"next":"http://localhost:7778/users?limit=10&offset=20",
         "previous":"http://localhost:7778/users?limit=10&offset=0"},
         "data":[{"email":"test1@gmail.com","id":1,"password":"test1"}]
    }

###$ curl http://localhost:7778/users/1 -X GET -u test:test

    {"email":"test1@gmail.com","id":1,"password":"test1"}

###$ curl http://localhost:7778/users/1 -X DELETE -u test:test

    {}

##brat

'brat' is the acronym of '__B__rat is a [framework|practice] of __R__estful __A__pi based on __T__ornado'.
