from unittest.mock import patch

from hibpcli.keepass import check_passwords_from_db


@patch("hibpcli.keepass.LeaksStore.__contains__")
def test_check_passwords_from_db(mock_is_leaked):
    path = "tests/test.kdbx"
    password = "test"  # nosec
    mock_is_leaked.return_value = lambda x: x == "test"
    expected_output = """[Entry: "test_title (test_user)"]"""
    assert str(check_passwords_from_db(path, password)) == expected_output
