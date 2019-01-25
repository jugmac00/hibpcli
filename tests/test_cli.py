from click.testing import CliRunner

from hibpcli.cli import main


def test_keepass_subcommand_returns_leaked_entry():
    runner = CliRunner()
    result = runner.invoke(main, ["keepass"], input="\n".join(["tests/test.kdbx", "test"]))
    expected_output = """Please enter the path to the database: tests/test.kdbx
Please enter the master password for the database: 
The passwords of following entries are leaked:
[b'Entry: "test_title (test_user)"']
"""
    assert result.output == expected_output
