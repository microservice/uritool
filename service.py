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


def do_parse(uri):
    # Parse the incoming URI
    return rfc3986.urlparse(uri)


def do_query(uri):
    parsed = do_parse(uri)

    collection = {}
    for (k, v) in urllib.parse.parse_qsl(parsed.query, keep_blank_values=True):
        collection[k] = v

    return collection


@service.register()
def parse(uri: str) -> dict:
    """Parse a given URI into its parts."""

    # Parse the incoming URI.
    parsed = do_parse(uri)

    # Create a representable body.
    result = {
        'uri': uri,
        'scheme': parsed.scheme,
        'userinfo': parsed.userinfo,
        'host': parsed.host,
        'path': parsed.path,
        'query': parsed.query,
        # Special attribute for parsed query string:
        '?': do_query(uri),
        'fragment': parsed.fragment,
        'netloc': parsed.netloc,
    }
    return result


@service.register()
def query(uri: str) -> dict:
    """Parse a given URI's query fragment."""
    return do_query(uri)


@service.register(name="is_valid")
def validate(uri: str) -> bool:
    """Is the given URI valid?"""
    return rfc3986.is_valid_uri(uri=uri)


if __name__ == '__main__':
    service.serve()
