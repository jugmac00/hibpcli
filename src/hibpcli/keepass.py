from hibpcli.password import Password
from pykeepass import PyKeePass


def check_passwords_from_db(path, master_password):
    """ - """
    kp = PyKeePass(path, password=master_password)

    leaked_entries = []
    for entry in kp.entries:
        p = Password(password=entry.password)
        if p.is_leaked():
            leaked_entries.append(entry)

    return leaked_entries
