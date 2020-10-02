import os


def test_usage_of_module_as_main_program():
    """Make sure module can be executed.

    More info about this interesting way of testing:
    https://mail.python.org/pipermail/tutor/2016-February/108119.html
    """
    assert os.system("python -m hibpcli.cli") == 0  # nosec


def test_script_is_callable():
    """Make sure "hibpcli" is available after installation."""
    assert os.system("hibpcli") == 0  # nosec
