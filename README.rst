.. image:: https://github.com/jugmac00/hibpcli/actions/workflows/ci.yml/badge.svg?branch=master
    :target: https://github.com/jugmac00/hibpcli/actions/workflows/ci.yml
    :alt: CI Status

.. image:: https://img.shields.io/pypi/v/hibpcli   
    :alt: PyPI version
    :target: https://pypi.org/project/hibpcli/

.. image:: https://img.shields.io/pypi/pyversions/hibpcli   
    :alt: PyPI - Python Version
    :target: https://pypi.org/project/hibpcli/

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


run tests for Python 3.14 only
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    tox -e py314


pass through e.g. verbose argument to pytest
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    tox -e py314 -- -vv


generate coverage
~~~~~~~~~~~~~~~~~

.. code::

    tox -e coverage


thank you
---------

- click - https://click.palletsprojects.com
- pykeepass - https://github.com/libkeepass/pykeepass
- httpx - https://github.com/encode/httpx
