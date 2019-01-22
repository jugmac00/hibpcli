from pykeepass import PyKeePass

from hibpcli import password


def check_passwords_from_db(path, master_password):
    """ - """
    kp = PyKeePass(path, password=master_password)

    leaked_entries = []
    for entry in kp.entries:
        p = password.Password(password=entry.password)
        if p.is_password_leaked():
            leaked_entries.append(entry)
        
    return leaked_entries
