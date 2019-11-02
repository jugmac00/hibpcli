import textwrap

from click.testing import CliRunner
from unittest.mock import patch

from hibpcli.cli import main


@patch("hibpcli.cli.check_passwords_from_db")
def test_keepass_subcommand_returns_leaked_entry(mock_check):
    mock_check.return_value = [b'Entry: "test_title (test_user)"']
    runner = CliRunner()
    result = runner.invoke(
        main, ["keepass"], input="\n".join(["tests/test.kdbx", "test"])
    )
    expected_output = """\
        Please enter the path to the database: tests/test.kdbx
        Please enter the master password for the database: 
        The passwords of following entries are leaked:
        [b'Entry: "test_title (test_user)"']
    """
    assert result.output == textwrap.dedent(expected_output)


@patch("hibpcli.cli.check_passwords_from_db")
def test_keepass_subcommand_returns_all_ok(mock_check):
    mock_check.return_value = list()
    runner = CliRunner()
    result = runner.invoke(
        main, ["keepass"], input="\n".join(["tests/test.kdbx", "test"])
    )
    expected_output = """\
        Please enter the path to the database: tests/test.kdbx
        Please enter the master password for the database: 
        Hooray, everything is safe!
    """
    assert result.output == textwrap.dedent(expected_output)


@patch("hibpcli.cli.check_passwords_from_db")
def test_keepass_subcommand_with_path_option(mock_check):
    mock_check.return_value = [b'Entry: "test_title (test_user)"']
    runner = CliRunner()
    result = runner.invoke(
        main, ["keepass", "--path", "tests/test.kdbx"], input="test"
    )
    expected_output = """\
        Please enter the master password for the database: 
        The passwords of following entries are leaked:
        [b'Entry: "test_title (test_user)"']
    """
    assert result.output == textwrap.dedent(expected_output)


@patch("hibpcli.cli.check_passwords_from_db")
def test_keepass_subcommand_with_path_and_password_options(mock_check):
    mock_check.return_value = [b'Entry: "test_title (test_user)"']
    runner = CliRunner()
    result = runner.invoke(
        main, ["keepass", "--path", "tests/test.kdbx", "--password", "test"]
    )
    expected_output = """\
        The passwords of following entries are leaked:
        [b'Entry: "test_title (test_user)"']
    """
    assert result.output == textwrap.dedent(expected_output)
