from typing import List

from hibpcli.leaks import LeaksStore
from pykeepass import PyKeePass  # type: ignore


def check_passwords_from_db(path: str, master_password: str) -> List[str]:
    """ - """
    kp = PyKeePass(path, password=master_password)
    leaksstore = LeaksStore()
    return [entry for entry in kp.entries if entry.password in leaksstore]
