from hibpcli.password import Password
from pykeepass import PyKeePass


def check_passwords_from_db(path, master_password):
    """ - """
    kp = PyKeePass(path, password=master_password)
    return [
        entry for entry in kp.entries if Password(password=entry.password).is_leaked()
    ]
