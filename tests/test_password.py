import socket
import textwrap
from unittest.mock import patch

import pytest

from hibpcli.exceptions import ApiError
from hibpcli.leaks import LeaksStore

# this is just a small part of a real response
RESPONSE_TEXT = textwrap.dedent(
    """\
    FE5CCB19BA61C4C0873D391E987982FBBD3:74831\r\n
    FF36DC7D3284A39991ADA90CAF20D1E3C0D:1\r\n
    FFF983A91443AE72BD98E59ADAB93B31974:2
    """
)


def test_password_signature():
    leaksstore = LeaksStore()
    with pytest.raises(TypeError):
        None in leaksstore  # type: ignore


@patch("hibpcli.leaks.httpx.get")
def test_is_leaked_password(mock_get):
    mock_get.return_value.text = RESPONSE_TEXT
    leaksstore = LeaksStore()
    assert "test" in leaksstore
    mock_get.assert_called_with("https://api.pwnedpasswords.com/range/A94A8")


@patch("hibpcli.leaks.httpx.get")
def test_is_leaked_raises_api_error(mock_get):
    mock_get.side_effect = socket.gaierror
    leaksstore = LeaksStore()
    with pytest.raises(ApiError):
        "test" in leaksstore
