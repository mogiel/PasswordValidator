"""module for checking with use regular expression"""
# system module
import re
from typing import Literal
# local code
from password_validators.special_char_choice import special_char_choice
from password_validators.validator import Validator


class PasswordMarkValidator(Validator):
    """Validator that checks if password is safe"""
    def __init__(self,
                 password: str | None = None,
                 min_char: int = 8,
                 max_char: int = 128,
                 special_char: Literal["min", "max", None] = "max"
                 ):
        """
        :type password: str | None
        :type min_char: int
        :type max_char: int
        :type special_char: Literal["min", "max", None]
        :rtype: object
        """
        self.special_char = special_char_choice(special_char)
        self.max_char = min(max(max_char, min_char), 128)
        self.min_char = max(min(max_char, min_char), 4)
        self.password = password
        self.is_valid = self._is_valid()

    def __bool__(self):
        return self.is_valid

    def _is_valid(self) -> bool:

        if self.password is None:
            return False
        # pylint: disable=consider-using-f-string
        password_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[' + self.special_char \
                         + r"])[A-Za-z\d" + self.special_char + "]{" \
                         + r"{},{}".format(self.min_char, self.max_char) + r"}$"

        return re.compile(password_regex).match(self.password) is not None

    def info(self) -> str:
        """Returns information about the correctness of the password

        :return: password strength with mark
        :rtype: int
        """

        if self.is_valid is True:
            return f"Check minimum {self.min_char} and maximum {self.max_char} characters," \
                   f"at least one uppercase letter, one lowercase letter," \
                   f"one number and one special character: OK"
        return f"Check minimum {self.min_char} and maximum {self.max_char} characters," \
               f"at least one uppercase letter, one lowercase letter," \
               f"one number and one special character: NOT"

    def get_strong(self) -> int:
        """Getter for self._strong

        :return: password strength with uppercase letters
        :rtype: int
        """
        return self._strong
