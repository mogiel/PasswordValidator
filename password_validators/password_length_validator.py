"""length checking module"""
# local code
from password_validators.validator import Validator


class PasswordLengthValidator(Validator):
    """Validator that checks if password is safe"""
    def __init__(self, password: str | None, min_char: int = 8, max_char: int = 128):
        """
        :param password:
        :type password: str | None
        :param min_char:
        :type min_char: int(8, 128)
        :param max_char:
        :type max_char: int(8, 128)
        """
        self.max_char = min(max(max_char, min_char), 128)
        self.min_char = max(min(max_char, min_char), 4)
        self.password = len(password)
        self._strong = 0
        self.is_valid = self._is_valid()

    def __bool__(self):
        return self.is_valid

    def _is_valid(self) -> bool:
        """Check if text is valid

        :rtype: bool
        """

        self._strong = self.password // 4

        return self.min_char <= self.password <= self.max_char

    def info(self) -> str:
        """Returns information about the correctness of the password

        :return: password strength with length
        :rtype: int
        """

        if self.is_valid is True:
            return "Check password length: OK"
        return "Check password length: NOT"

    def get_strong(self) -> int:
        """Getter for self._strong

        :return: password strength with uppercase letters
        :rtype: int
        """
        return self._strong
