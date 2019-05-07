# URITool Microservice

This microservice exists to provide utilities for dealing with URIs:

![Microservice](https://img.shields.io/badge/microservice-ready-brightgreen.svg?style=for-the-badge)
[![Docker Build Status](https://img.shields.io/docker/build/microservices/uritool.svg?style=for-the-badge)](https://hub.docker.com/r/microservices/uritool/)

## Direct usage in [Storyscript](https://storyscript.io/):

```coffee
>>> (uritool parse 'https://github.com/')
{"uri": "https://github.com/", "scheme": "https", "userinfo": null, "host": "github.com", "path": "/", "query": null, "?": {}, "fragment": null, "netloc": "github.com"}
```

Curious to [learn more](https://docs.storyscript.io/)?

✨🍰✨
