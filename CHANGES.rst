CHANGELOG
=========

0.5.0 (06.01.2021)
------------------

added
~~~~~
- add the `bandit` security checker
- add support for Python 3.9
- add type annotations
- improve message when there are no known leaks for a password (@eumiro)
- provide user friendly error message when given password is wrong
- provide caching for password lookups (@eumiro)

changed
~~~~~~~
- run coverage directly instead of pytest-cov
- use gh actions instead of Travis

0.4.1 (30.09.2020)
------------------

added
~~~~~
- add packaging guideline

changed
~~~~~~~
- run linters via `pre-commit`

0.4.0 (25.05.2020)
------------------

added
~~~~~
- introduce tox
- introduce flake8
- introduce flake8-click
- introduce coverage via coveralls
- add beta classifier

changed
~~~~~~~
- improve readme
- convert README and CHANGES to rst format
- use setup.py instead of flit for packaging
- move source code in src directory
- update versions of installation dependencies
- subcommand to check a single password now is `check-password`
- subcommand to check a keepass db now is `check-keepass`

0.3.0 (03.11.2019)
------------------

added
~~~~~

- add new subcommand "password" for checking a single password
- add pdb++ to dev dependencies
- add some basic error handling
- add some classifiers

0.2.0 (02.11.2019)
------------------

added
~~~~~

- add path option to keepass subcommand
- add password option to keepass subcommand

changed
~~~~~~~

- update dependencies

0.1.0 (01.11.2019)
------------------

added
~~~~~

- add support for Python 3.7
- add support for Python 3.8
- create a "hibpcli" script

changed
~~~~~~~

- use "black" code formatter
- update dependencies
- remove requirements-dev.txt
- put test requirements in pyproject.toml

0.0.3 (29.01.2019)
------------------

added
~~~~~

- add a separate file for changes
- add info about testing and coverage
- add more info for --help dialog

changed
~~~~~~~

- do not show password when being entered
- move keepass check into subcommand
- check "path input" whether it is a file
- improved tests and coverage (currently 100%)


0.0.2 (22.01.2019)
------------------

added
~~~~~

- add dependencies to pyproject.toml

0.0.1 (22.01.2019)
------------------

- initial release
