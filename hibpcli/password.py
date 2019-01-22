import hashlib
import requests


class Password:
    def __init__(self, password):
        self.password = password

    def is_password_leaked(self):
        hex_digest = self._generate_hash()
        first_hash_part, second_hash_part = hex_digest[:5], hex_digest[5:]
        result = requests.get(f"https://api.pwnedpasswords.com/range/{first_hash_part}").text
        # the result is text with entries split by new line
        # one entry consists of the rest of the hash and count of
        # leak, separated by a colon
        # cut off string - information after the hash is of no interest
        partial_hash_list = [line[:35] for line in result.splitlines()]
        return second_hash_part in partial_hash_list

    def _generate_hash(self):
        hash_object = hashlib.sha1(bytes(self.password, "UTF-8"))
        hex_digest = hash_object.hexdigest().upper()
        return hex_digest
