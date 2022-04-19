"""module for checking from an external API. https://haveibeenpwned.com/"""
# system module
from hashlib import sha1
# external module
from requests import get
# local code
from password_validators.validator import Validator


PWNED_URL = "https://api.pwnedpasswords.com/range/"


class PasswordPWNEDValidator(Validator):
    """Validator that checks if password is safe"""
    def __init__(self, password: str | None = None):
        """
        :param password:
        :type password: str | None
        """
        self.password = password
        self._strong = 0
        self.is_valid = self._is_valid()

    def __bool__(self):
        return self.is_valid

    def _is_valid(self) -> bool:
        """Check if text is valid

        :rtype: bool
        """
        hash_password = sha1(self.password.encode("utf-8")).hexdigest().upper()
        with get(PWNED_URL + hash_password[:5]) as content:
            self._strong = 5 if hash_password[5:] not in content.text else 0
            return hash_password[5:] not in content.text

    def info(self) -> str:
        """Returns information about the correctness of the password

        :return: password strength with API
        :rtype: int
        """

        if self.is_valid is True:
            return "Check PWNED: OK"
        return "Check PWNED: NOT"

    def get_strong(self) -> int:
        """Getter for self._strong

        :return: password strength with uppercase letters
        :rtype: int
        """
        return self._strong
