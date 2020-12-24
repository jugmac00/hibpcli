import textwrap
from unittest.mock import patch

from click.testing import CliRunner

from hibpcli.cli import main
from hibpcli.exceptions import ApiError
from hibpcli.leaks import LeaksStore


@patch.object(LeaksStore, "__contains__", return_value=True)
def test_password_subcommand_for_leaked_password(mock_password):
    runner = CliRunner()
    result = runner.invoke(main, ["check-password", "--password", "test"])
    expected_output = "Please change your password!\n"
    assert result.output == expected_output


@patch.object(LeaksStore, "__contains__", return_value=False)
def test_password_subcommand_for_safe_password(mock_password):
    runner = CliRunner()
    result = runner.invoke(main, ["check-password", "--password", "test"])
    expected_output = "Your password has not been reported leaked until now.\n"
    assert result.output == expected_output


@patch.object(LeaksStore, "__contains__", return_value=False)
def test_password_subcommand_with_prompt(mock_password):
    runner = CliRunner()
    result = runner.invoke(main, ["check-password"], input="test")
    expected_output = """\
        Please enter a password which should be checked: 
        Your password has not been reported leaked until now.
    """  # noqa: W291
    assert result.output == textwrap.dedent(expected_output)


@patch.object(LeaksStore, "__contains__", side_effect=ApiError("Error"))
def test_password_subcommand_error_handling(mock_password):
    runner = CliRunner()
    result = runner.invoke(main, ["check-password", "--password", "test"])
    expected_output = "Error\n"
    assert result.output == expected_output
