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
        main, ["check-keepass", "tests/test.kdbx"], input="\n".join(["test"])
    )
    expected_output = textwrap.dedent(
        """\
        Please enter the master password for the database: 
        The passwords of following entries are leaked:
        [b'Entry: "test_title (test_user)"']
    """  # noqa: W291
    )
    assert result.output == expected_output


@patch("hibpcli.cli.check_passwords_from_db")
def test_keepass_subcommand_returns_all_ok(mock_check):
    mock_check.return_value = list()
    runner = CliRunner()
    result = runner.invoke(
        main, ["check-keepass", "tests/test.kdbx"], input="\n".join(["test"])
    )
    expected_output = textwrap.dedent(
        """\
        Please enter the master password for the database: 
        Your passwords have not been reported leaked until now.
    """  # noqa: W291
    )
    assert result.output == expected_output


@patch("hibpcli.cli.check_passwords_from_db")
def test_keepass_subcommand_with_path(mock_check):
    mock_check.return_value = [b'Entry: "test_title (test_user)"']
    runner = CliRunner()
    result = runner.invoke(main, ["check-keepass", "tests/test.kdbx"], input="test")
    expected_output = textwrap.dedent(
        """\
        Please enter the master password for the database: 
        The passwords of following entries are leaked:
        [b'Entry: "test_title (test_user)"']
    """  # noqa: W291
    )
    assert result.output == expected_output


@patch("hibpcli.cli.check_passwords_from_db")
def test_keepass_subcommand_with_path_and_password_options(mock_check):
    mock_check.return_value = [b'Entry: "test_title (test_user)"']
    runner = CliRunner()
    result = runner.invoke(
        main, ["check-keepass", "tests/test.kdbx", "--password", "test"]
    )
    expected_output = textwrap.dedent(
        """\
        The passwords of following entries are leaked:
        [b'Entry: "test_title (test_user)"']
    """
    )
    assert result.output == expected_output


@patch.object(Password, "is_leaked")
def test_keepass_subcommand_error_handling(mock_password):
    mock_password.side_effect = ApiError("Error")
    runner = CliRunner()
    result = runner.invoke(
        main, ["check-keepass", "tests/test.kdbx", "--password", "test"]
    )
    expected_output = "Error\n"
    assert result.output == expected_output
