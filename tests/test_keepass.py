from hibpcli.keepass import check_passwords_from_db


def test_check_passwords_from_db():
    path = 'tests/test.kdbx'
    password = 'test'
    assert str(check_passwords_from_db(path, password)) == '''[b'Entry: "test_title (test_user)"']'''
    
