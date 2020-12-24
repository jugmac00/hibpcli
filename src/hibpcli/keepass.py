from typing import List

from pykeepass import PyKeePass  # type: ignore
from pykeepass.exceptions import CredentialsError  # type: ignore

from hibpcli.exceptions import KeepassError
from hibpcli.leaks import LeaksStore


def check_passwords_from_db(path: str, master_password: str) -> List[str]:
    """ - """
    try:
        kp = PyKeePass(path, password=master_password)
    except CredentialsError:
        raise KeepassError
    else:
        leaksstore = LeaksStore()
        return [entry for entry in kp.entries if entry.password in leaksstore]
