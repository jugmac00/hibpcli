import textwrap
from unittest.mock import patch

from click.testing import CliRunner

from hibpcli.cli import main
from hibpcli.exceptions import ApiError
from hibpcli.password import Password


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
    """  # noqa
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
    """  # noqa
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
    """  # noqa
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


@patch.object(Password, "is_leaked", return_value=True)
def test_password_subcommand_for_leaked_password(mock_password):
    runner = CliRunner()
    result = runner.invoke(
        main, ["password", "--password", "test"]
    )
    expected_output = "Please change your password!\n"
    assert result.output == expected_output


@patch.object(Password, "is_leaked", return_value=False)
def test_password_subcommand_for_safe_password(mock_password):
    runner = CliRunner()
    result = runner.invoke(
        main, ["password", "--password", "test"]
    )
    expected_output = "Your password is safe!\n"
    assert result.output == expected_output


@patch.object(Password, "is_leaked", return_value=False)
def test_password_subcommand_with_prompt(mock_password):
    runner = CliRunner()
    result = runner.invoke(
        main, ["password"], input="test"
    )
    expected_output = """\
        Please enter a password which should be checked: 
        Your password is safe!
    """  # noqa
    assert result.output == textwrap.dedent(expected_output)


@patch.object(Password, "is_leaked")
def test_keepass_subcommand_error_handling(mock_password):
    mock_password.side_effect = ApiError("Error")
    runner = CliRunner()
    result = runner.invoke(
        main, ["keepass", "--path", "tests/test.kdbx", "--password", "test"]
    )
    expected_output = "Error\n"
    assert result.output == expected_output


@patch.object(Password, "is_leaked", side_effect=ApiError("Error"))
def test_password_subcommand_error_handling(mock_password):
    runner = CliRunner()
    result = runner.invoke(
        main, ["password", "--password", "test"]
    )
    expected_output = "Error\n"
    assert result.output == expected_output
