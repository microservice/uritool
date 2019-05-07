#!/usr/bin/env python

"""Naval Fate.

Usage:
  uritool.py parse <uri>
  uritool.py query <uri>

Options:
  -h --help     Show this screen.
"""

import sys
import json
import urllib.parse

import rfc3986
from docopt import docopt


def flatten(x):
    if len(x) == 1:
        x = x[0]
    else:
        x = x

    return x


def parse(uri):
    # Parse the incoming URI
    return rfc3986.urlparse(uri)


def parse_qs(uri):
    parsed = parse(uri)

    collection = {}
    for (k, v) in urllib.parse.parse_qsl(parsed.query, keep_blank_values=True):
        collection[k] = v

    return collection


def do_parse(uri):

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
        '?': parse_qs(uri),
        'fragment': parsed.fragment,
        'netloc': parsed.netloc,
    }
    # Print json to console.
    sys.stdout.write(json.dumps(result))
    sys.exit(0)


def do_query(uri):

    # Parse the incoming URI.
    parsed = rfc3986.urlparse(uri)
    # Print json to console.
    sys.stdout.write(json.dumps(parse_qs(uri)))
    sys.exit(0)

def scrub_incoming(uri_like):
    try:
        v = json.loads(uri_like)['uri']
    except ValueError:
        v = uri_like
        
    return v

if __name__ == '__main__':
    # Parse the CLI arguments...
    
    args = docopt(__doc__)
    uri = scrub_incoming(args['<uri>'])

    # Execute the proper sub-command.
    if args['parse']:
        do_parse(uri=uri)
    elif args['query']:
        do_query(uri=uri)
