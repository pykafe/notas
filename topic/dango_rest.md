# REST

## What is REST?

- Representational state transfer
- A method centered HTTTP verbs for getting and receiving resources.


## How does REST work?

- REST uses URLs and HTTP verbs to standardized the sharing of resources via APIs
- REST puts 3 things together to help create clear APIs
    1) a way give things on the internet a location (URLs)
    2) standard verbs / methods to act on those things (HTTP)
    3) common format for data (JSON)


## What is a URL?

- Uniform Resource Locator
- A URL is an Address like `www.github.com/pykafe`


## What is HTTP?

- HyperText Transfer Protocol
- It is the protocol of the web.
- It is the `http://` of a web address (URL)


## What is an HTTP verb?

- HTTP verbs are standard methods for URLs.
- We use `GET`, `POST`, `PUT`, 'HEAD', `DELETE` every day.


## What is an API?

- Application Programming Interface
- An API defines how programs can talk to each other.


## Example of a NON-REST API

    VERB        URL
========================================
    GET         /API/todo/my_task/view
    GET         /API/todo/my_task/delete
    GET         /API/todo/my_task/update
    GET         /API/todo/my_task/create


## Example of a REST API

    VERB        URL
==============================================
    GET         /API/todo/my_task/    # view
    DELETE      /API/todo/my_task/    # delete
    PUT         /API/todo/my_task/    # update
    POST        /API/todo/my_task/    # create


## What is JSON?

- JavaScript Object Notation
- JSON is a common format for sharing data
- JSON is just a set of key, value pairs just like a Python Dictionary (dict)
- example: `{'name': 'Jose Soares'}`


## What is AJAX?

- Asyncronus JavaScript and XML
    - but can use with JSON!
- A way to talk to a server from JavaScript


