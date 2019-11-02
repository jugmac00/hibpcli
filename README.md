[![Build Status](https://travis-ci.org/jugmac00/hibpcli.svg?branch=master)](https://travis-ci.org/jugmac00/hibpcli)
[![Current version on PyPI](https://img.shields.io/pypi/v/hibpcli.svg)](https://pypi.org/project/hibpcli/)
[![Requirements Status](https://requires.io/github/jugmac00/hibpcli/requirements.svg?branch=master)](https://requires.io/github/jugmac00/hibpcli/requirements/?branch=master)
![](https://img.shields.io/pypi/l/hibpcli.svg)

# hibpcli

A command line interface for the "haveibeenpwned.com" API - speaks keepass.

## current state

A little bit alpha.

## usage

```
$ hibpcli keepass --path PATHTOKEEPASSDB --password PASSWORDFORKEEPASSDB

The passwords of following entries are leaked:
[Entry: "test_title (test_user)"]
```

```
$ hibpcli password --password test

Please change your password!
```


## scope

- check all passwords in a keepass db via hibp online API
- check a single password

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
