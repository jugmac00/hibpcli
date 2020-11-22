import hashlib
import socket

import httpx
from hibpcli.exceptions import ApiError


class Password:
    def __init__(self, password):
        self.password = password

    def is_leaked(self):
        hex_digest = self._generate_hash()
        first_hash_part, second_hash_part = hex_digest[:5], hex_digest[5:]
        try:
            result = httpx.get(
                f"https://api.pwnedpasswords.com/range/{first_hash_part}"
            ).text
        except socket.gaierror:
            raise ApiError("Error: Could not get a result from the API.")
        else:
            # the result is text with entries split by new line
            # one entry consists of the rest of the hash and count of
            # leak, separated by a colon
            # cut off string - information after the hash is of no interest
            return second_hash_part in (line[:35] for line in result.splitlines())

    def _generate_hash(self):
        # using sha1 here is no security issue
        # the API uses it, so there is no other way to access the data
        hash_object = hashlib.sha1(bytes(self.password, "UTF-8"))  # nosec
        hex_digest = hash_object.hexdigest().upper()
        return hex_digest
