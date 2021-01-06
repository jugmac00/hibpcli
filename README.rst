.. image:: https://github.com/jugmac00/hibpcli/workflows/CI/badge.svg?branch=master
   :target: https://github.com/jugmac00/hibpcli/actions?workflow=CI
   :alt: CI Status

.. image:: https://coveralls.io/repos/github/jugmac00/hibpcli/badge.svg?branch=master
  :target: https://coveralls.io/github/jugmac00/hibpcli?branch=master

.. image:: https://img.shields.io/pypi/v/hibpcli.svg
  :target: https://pypi.org/project/hibpcli/

.. image:: https://img.shields.io/pypi/pyversions/hibpcli.svg
  :target: https://pypi.org/project/hibpcli/

.. image:: https://requires.io/github/jugmac00/hibpcli/requirements.svg?branch=master
  :target: https://requires.io/github/jugmac00/hibpcli/requirements/?branch=master

.. image:: https://img.shields.io/pypi/l/hibpcli
  :target: https://github.com/jugmac00/hibpcli/blob/master/LICENSE


hibpcli
=======

A command line interface for the **haveibeenpwned.com** API - speaks keepass.

installation
------------

.. code::

    $ pip install hibpcli


usage
-----

check all passwords in your keepass database
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    $ hibpcli check-keepass PATHTOKEEPASSDB --password PASSWORDFORKEEPASSDB

    The passwords of following entries are leaked:
    [Entry: "test_title (test_user)"]


check a single password
~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    $ hibpcli check-password --password PASSWORD

    Please change your password!


contributions, feature requests, bug reports
--------------------------------------------

Please create an issue at https://github.com/jugmac00/hibpcli/issues

tests
-----

run all tests and linters
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    tox


run tests for Python 3.8 only
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    tox -e py38


pass through e.g. verbose argument to pytest
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    tox -e py38 -- -vv


generate coverage
~~~~~~~~~~~~~~~~~

.. code::

    tox -e coverage


thank you
---------

- click - https://click.palletsprojects.com
- pykeepass - https://github.com/pschmitt/pykeepass
- httpx - https://github.com/encode/httpx
