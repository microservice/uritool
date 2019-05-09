#!/usr/bin/env python


import sys
import json
import urllib.parse

import micro
import rfc3986

service = micro.Service(name='uritool')


def flatten(x):
    if len(x) == 1:
        x = x[0]
    else:
        x = x

    return x


def parse(uri):
    # Parse the incoming URI
    return rfc3986.urlparse(uri)


def query(uri):
    parsed = parse(uri)

    collection = {}
    for (k, v) in urllib.parse.parse_qsl(parsed.query, keep_blank_values=True):
        collection[k] = v

    return collection


@service.register(path='/parse', method='get')
def do_parse(uri: str):

    # Parse the incoming URI.
    parsed = parse(uri)

    # Create a representable body.
    result = {
        'uri': uri,
        'scheme': parsed.scheme,
        'userinfo': parsed.userinfo,
        'host': parsed.host,
        'path': parsed.path,
        'query': parsed.query,
        # Special attribute for parsed query string:
        '?': parse(uri),
        'fragment': parsed.fragment,
        'netloc': parsed.netloc,
    }
    return result


@service.register(path='/query', method='get')
def do_query(uri: str):
    return query(uri)


if __name__ == '__main__':
    service.serve()
