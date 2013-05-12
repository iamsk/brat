---
title: {{ title }} API
brand: api.no.de
version: {{ version }}
---

# {{ title }} API

### All API calls start with

<pre class="base">
{{ base_url }}
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

{% for group_url, true_urls in group_urls.items() %}
# {{ group_url }}

{% for true_url, options in true_urls.items() %}
{% for option in options %}
## {{ option['method'] }} {{ true_url }}

DESCRIPTION: {{ option['description'] }}

PARAMS: {{ option.get('params', []) }}

#### example request

    {{ option['request'] }}

#### response
    {% autoescape None %}
    {{ option['response'] }}
    {% autoescape %}

{% end %}
{% end %}
{% end %}
