from mock import patch

from hibpcli.keepass import check_passwords_from_db


@patch("hibpcli.keepass.Password.is_leaked")
def test_check_passwords_from_db(mock_is_leaked):
    path = 'tests/test.kdbx'
    password = 'test'
    mock_is_leaked.return_value = lambda x: x == "test"
    expected_output = '''[b'Entry: "test_title (test_user)"']'''
    assert str(check_passwords_from_db(path, password)) == expected_output
