import pytest

from hibpcli.password import Password


def test_password_signature():
    with pytest.raises(TypeError):
        Password()  # pylint: disable=E1120

def test_is_password_leaked():
    # todo: until now, the test tests against the live API
    # todo: mock requests
    p = Password("test")
    assert p.is_password_leaked() is True
