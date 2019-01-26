import os


def test_usage_of_module_as_main_programm():
    """Make sure module can be executed.

    More info about this interesting way of testing:
    https://mail.python.org/pipermail/tutor/2016-February/108119.html
    """
    assert os.system("python -m hibpcli.cli") == 0
