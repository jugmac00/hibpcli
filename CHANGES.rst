CHANGELOG
=========

unreleased
----------

- introduce tox
- introduce flake8
- introduce flake8-click
- introduce coverage via coveralls
- improve readme
- add beta classifier
- convert README and CHANGES to rst format
- use setup.py instead of flit for packaging
- move source code in src directory


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
