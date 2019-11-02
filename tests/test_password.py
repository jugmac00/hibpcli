import pytest
import socket

from unittest.mock import patch

from hibpcli.exceptions import ApiError
from hibpcli.password import Password

# this is just a small part of a real response
RESPONSE_TEXT = "FE5CCB19BA61C4C0873D391E987982FBBD3:74831\r\nFF36DC7D3284A39991ADA90CAF20D1E3C0D:1\r\nFFF983A91443AE72BD98E59ADAB93B31974:2"


def test_password_signature():
    with pytest.raises(TypeError):
        Password()  # pylint: disable=E1120


@patch("hibpcli.password.httpx.get")
def test_is_leaked_password(mock_get):
    mock_get.return_value.text = RESPONSE_TEXT
    p = Password("test")
    assert p.is_leaked() is True
    mock_get.assert_called_with("https://api.pwnedpasswords.com/range/A94A8")


@patch("hibpcli.password.httpx.get")
def test_is_leaked_raises_api_error(mock_get):
    mock_get.side_effect = socket.gaierror
    p = Password("test")
    with pytest.raises(ApiError):
        p.is_leaked()
