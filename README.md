[![Build Status](https://travis-ci.org/jugmac00/hibpcli.svg?branch=master)](https://travis-ci.org/jugmac00/hibpcli)
[![Coverage Status](https://coveralls.io/repos/github/jugmac00/hibpcli/badge.svg?branch=introduce-coverage)](https://coveralls.io/github/jugmac00/hibpcli?branch=introduce-coverage)
[![Current version on PyPI](https://img.shields.io/pypi/v/hibpcli.svg)](https://pypi.org/project/hibpcli/)
[![Requirements Status](https://requires.io/github/jugmac00/hibpcli/requirements.svg?branch=master)](https://requires.io/github/jugmac00/hibpcli/requirements/?branch=master)
![](https://img.shields.io/pypi/l/hibpcli.svg)

# hibpcli

A command line interface for the "haveibeenpwned.com" API - speaks keepass.

## usage

### check all passwords in your keepass database

```
$ hibpcli keepass --path PATHTOKEEPASSDB --password PASSWORDFORKEEPASSDB

The passwords of following entries are leaked:
[Entry: "test_title (test_user)"]
```

### check a single password

```
$ hibpcli password --password PASSWORD

Please change your password!
```

## contributions, feature requests, bug reports

Please create an issue at https://github.com/jugmac00/hibpcli/issues

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
