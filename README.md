**Autocomplete API using Flask + Redis + Docker**
=================================================

Application Architecture:
-------------------------

1) Flask + Python application created with reference from http://oldblog.antirez.com/post/autocomplete-with-redis.html. The `/words` API will add new words to the Redis datastore and `/autocomplete` API will suggest probable words to complete the query.

2) `Dockerfile` uses `python:3.8-alpine`. Application is hosted on `localhost:5000`. Redis is running on container port `6379`. 

3) `docker-compose` will spin up two separate containers - one `api_web_1` and `api_redis_1`. 

Steps to use:
-------------

1) Unzip the Tar Ball. 
    
    `tar -zxvf redis-auto-complete.tar.gz`
    
2) Change Directory to **_api_** directory.

    `cd redis-auto-complete/api/`

3) Run **_docker-compose_** to start the flask application.

    `docker-compose up -d`
    
4) Use cURL client or Browser to perform the following GET request to add words to the Redis keystore. 

    `curl GET 'http://localhost:5000/add_word?word=box8'` 
    
    Sample Output:
    
    `Added`
    
5) Use cURL client or Browser to to perform the following GET request to query auto-completion suggestions from the Redis keystore. 

    `curl GET 'http://localhost:5000/autocomplete?query=bo'`
    
    Sample Output:
    
    `[
        "box8"
    ]`
    
6) To shut the application enter the following command: 

    `docker-compose down`
    
Further Scope:
----------------
Case insensitive auto-completion.