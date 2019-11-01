[![Build Status](https://travis-ci.org/jugmac00/hibpcli.svg?branch=master)](https://travis-ci.org/jugmac00/hibpcli)
[![Current version on PyPI](https://img.shields.io/pypi/v/hibpcli.svg)](https://pypi.org/project/hibpcli/)
[![Requirements Status](https://requires.io/github/jugmac00/hibpcli/requirements.svg?branch=master)](https://requires.io/github/jugmac00/hibpcli/requirements/?branch=master)
![](https://img.shields.io/pypi/l/hibpcli.svg)

# hibpcli

A command line interface for the "haveibeenpwned.com" API - speaks keepass.

## current state

Very alpha.

## usage

```
$ python -m hibpcli.cli keepass

Please enter the path to the database: tests/test.kdbx
Please enter the master password for the database:
The passwords of following entries are leaked:
[Entry: "test_title (test_user)"]
```

## scope

- check passwords in db via hibp online API (currently)
- check passwords in db via offline check (future)
- enter passwords manually (future)

## contributions, feature requests, bug reports

Please use https://github.com/jugmac00/hibpcli

## run tests

```
pytest
```

## run tests with coverage

```
pytest --cov=hibpcli --cov=tests --cov-report term-missing
```

## thank you
- click - https://click.palletsprojects.com
- pykeepass - https://github.com/pschmitt/pykeepass
- httpx - https://github.com/encode/httpx
