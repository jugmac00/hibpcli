[![Build Status](https://travis-ci.org/jugmac00/hibpcli.svg?branch=master)](https://travis-ci.org/jugmac00/hibpcli)

# hibpcli

A command line interface for the "haveibeenpwned.com" API - talks keepass.

## current state

Very alpha.

## usage

```
$ python -m hibpcli.cli

Please enter the path to the database: tests/test.kdbx
Please enter the master password for the database: test
The passwords of following entries are leaked:
[b'Entry: "test_title (test_user)"']
```

## scope

- check passwords in db via hibp online API (currently)
- check passwords in db via offline check (future)
- enter passwords manually (future)

## contributions, feature requests, bug reports

Please use https://github.com/jugmac00/hibpcli

## release history

### 0.0.2 (22.01.2019)

- add dependencies to pyproject.toml

### 0.0.1 (22.01.2019)

- initial release

## thank you
- click - https://click.palletsprojects.com
- pykeepass - https://github.com/pschmitt/pykeepass
- requests - https://github.com/requests/requests
