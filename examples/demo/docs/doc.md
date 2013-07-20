---
title: DEMO API
brand: api.no.de
version: 0.0.1
---

# DEMO API

### All API calls start with

<pre class="base">http://localhost:7778</pre>

### Path

For this documentation, we will assume every request begins with the above path.

### Format

All calls are returned in **JSON**.

### Status Codes

- **200** Successful OPTIONS, GET and DELETE.
- **201** Successful POST.
- **202** Successful PUT.
- **400** Bad Request.
- **401** Unauthorized.
- **403** Forbidden.
- **404** Not Found.
- **500** Internal Server Error.

### Auth Headers

Basic base64(username:password) used for basic auth

Client base64(client_key:client_secret) used for client auth


# users

    
        
## GET /users/(\d+)

DESCRIPTION: 用户详细信息

PARAMS: []

### request

    curl -u test:test http://localhost:7778/users/1 -X GET

### response

    
    {
        "error": {
                "message": "请求资源不存在", 
                "code": 404
        }
    }
    

        
## DELETE /users/(\d+)

DESCRIPTION: 删除用户

PARAMS: []

### request

    curl -u test:test http://localhost:7778/users/1 -X DELETE

### response

    
    {
        "error": {
                "message": "请求资源不存在", 
                "code": 404
        }
    }
    

        
    
        
## GET /users

DESCRIPTION: 用户列表

PARAMS: [u'offset', u'limit']

### request

    curl -u test:test http://localhost:7778/users -X GET

### response

    
    {
        "paging": {
                "previous": "http://localhost:7778/users?limit=10&offset=0", 
                "next": "http://localhost:7778/users?limit=10&offset=10"
        }, 
        "data": []
    }
    

        
## POST /users

DESCRIPTION: 添加用户

PARAMS: []

### request

    curl -u test:test http://localhost:7778/users -X POST -d params

### response

    
    Sorry, not support for docing currently!
    

        
    

