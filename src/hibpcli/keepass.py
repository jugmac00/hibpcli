from typing import List

from hibpcli.exceptions import KeepassError
from hibpcli.password import Password
from pykeepass import PyKeePass  # type: ignore
from pykeepass.exceptions import CredentialsError


def check_passwords_from_db(path: str, master_password: str) -> List[str]:
    """ - """
    try:
        kp = PyKeePass(path, password=master_password)
    except CredentialsError:
        raise KeepassError
    else:
        return [
            entry
            for entry in kp.entries
            if Password(password=entry.password).is_leaked()
        ]
