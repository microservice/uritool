# _URITool_ OMG Microservice

[![Open Microservice Guide](https://img.shields.io/badge/OMG%20Enabled-👍-green.svg?)](https://microservice.guide)
<!-- [![Docker Build Status](https://img.shields.io/docker/build/microservices/uritool.svg?style=for-the-badge)](https://hub.docker.com/r/microservices/uritool/) -->

This microservice exists to provide utilities for dealing with URIs:

## Direct usage in [Storyscript](https://storyscript.io/):

##### Parse
```coffee
>>> uritool parse uri:'https://github.com/'
{"uri": "https://github.com/", "scheme": "https", "userinfo": null, "host": "github.com", "path": "/", "query": null, "?": {}, "fragment": null, "netloc": "github.com"}
```
##### Query
```coffee
>>> uritool query uri:'https://httpbin.org/get?hello=world'
{"hello": "world"}
```
##### IsValid
```coffee
>>> uritool isValid uri:'https://github.com/'
true
```
Curious to [learn more](https://docs.storyscript.io/)?

✨🍰✨

## Usage with [OMG CLI](https://www.npmjs.com/package/omg)

##### Parse
```shell
$ omg run parse -a uri=<URI_TO_PARSE>
```
##### Query
```shell
$ omg run query -a uri=<URI>
```
##### Is Valid
```shell
$ omg run isValid -a uri=<URI>
```

**Note**: The OMG CLI requires [Docker](https://docs.docker.com/install/) to be installed.

## License
[MIT License](https://github.com/omg-services/uritool/blob/master/LICENSE).
