---
title: demo API
brand: api.no.de
version: 0.0.1
---

# demo API

### All API calls start with

<pre class="base">
http://localhost:5000
</pre>

### Path

For this documentation, we will assume every request begins with the above path.

### Format

All calls are returned in **JSON**.

### Status Codes

- **200** Successful GET and PUT.
- **201** Successful POST.
- **202** Successful Provision queued.
- **204** Successful DELETE
- **401** Unauthenticated.
- **409** Unsuccessful POST, PUT, or DELETE (Will return an errors object)


# users



## GET /users/(\d+)

用户详细信息

#### example request

    $ curl -u jill:secret https://api.no.de/account -X PUT \
      -F 'phone=6041234567'

#### response

    pass

## DELETE /users/(\d+)

删除用户

#### example request

    $ curl -u jill:secret https://api.no.de/account -X PUT \
      -F 'phone=6041234567'

#### response

    pass



## GET /users

用户列表

#### example request

    $ curl -u jill:secret https://api.no.de/account -X PUT \
      -F 'phone=6041234567'

#### response

    pass

## DELETE /users

添加用户

#### example request

    $ curl -u jill:secret https://api.no.de/account -X PUT \
      -F 'phone=6041234567'

#### response

    pass



