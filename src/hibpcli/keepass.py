from typing import List

from hibpcli.password import Password
from pykeepass import PyKeePass  # type: ignore


def check_passwords_from_db(path: str, master_password: str) -> List[str]:
    """ - """
    kp = PyKeePass(path, password=master_password)
    return [
        entry for entry in kp.entries if Password(password=entry.password).is_leaked()
    ]
