import hashlib
import socket
from typing import Dict, Set

import httpx

from hibpcli.exceptions import ApiError


class LeaksStore:
    def __init__(self) -> None:
        self._pages: Dict[str, Set[str]] = {}

    def __contains__(self, password: str) -> bool:
        hex_digest = self._generate_hash(password)
        hash_head, hash_tail = hex_digest[:5], hex_digest[5:]
        if hash_head not in self._pages:
            self._pages[hash_head] = self._load_page(hash_head)
        return hash_tail in self._pages[hash_head]

    @staticmethod
    def _generate_hash(password: str) -> str:
        # using sha1 here is no security issue
        # the API uses it, so there is no other way to access the data
        hash_object = hashlib.sha1(bytes(password, "UTF-8"))  # nosec
        hex_digest = hash_object.hexdigest().upper()
        return hex_digest

    @staticmethod
    def _load_page(hash_head: str) -> Set[str]:
        """Load a list of hash/occurrence pairs for a given hash_head.

        Returns a set of hash_tails only.
        """
        try:
            result = httpx.get(f"https://api.pwnedpasswords.com/range/{hash_head}").text
        except socket.gaierror:
            raise ApiError("Error: Could not get a result from the API.")
        else:
            # the result is text with entries split by new line
            # one entry consists of the rest of the hash and count of
            # leak, separated by a colon
            # cut off string - information after the hash is of no interest
            return {line[:35] for line in result.splitlines()}
