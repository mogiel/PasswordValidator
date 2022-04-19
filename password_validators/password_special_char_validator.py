"""module for checking special characters"""
# system module
from typing import Literal
# local code
from password_validators.special_char_choice import special_char_choice
from password_validators.validator import Validator


class PasswordSpecialCharValidator(Validator):
    """Validator that checks if password is safe"""
    def __init__(self, password: str | None, special_char: Literal["min", "max", None] = "max"):
        """
        :param password:
        :type password: str | None
        :param special_char
        :type special_char: Literal["min", "max", None]
        """
        self.password = password
        self._strong = 0
        self.special_char = special_char_choice(special_char)
        self.is_valid = self._is_valid()

    def __bool__(self):
        return self.is_valid

    def _is_valid(self) -> bool:
        """Check if text is valid

        :rtype: bool
        """
        self._strong = sum([char in self.special_char for char in self.password]) * 2
        return self._strong > 0

    def info(self) -> str:
        """Returns information about the correctness of the password

        :return: password strength with special character
        :rtype: int
        """

        if self.is_valid is True:
            return "Check special character: OK"
        return "Check special character: NOT"

    def get_strong(self) -> int:
        """Getter for self._strong

        :return: password strength with uppercase letters
        :rtype: int
        """
        return self._strong
