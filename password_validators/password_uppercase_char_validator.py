"""module for checking uppercase letters"""
# local code
from password_validators.validator import Validator


class PasswordUppercaseCharValidator(Validator):
    """Validator that checks if password is safe"""
    def __init__(self, password: str | None):
        """
        :param password:
        :type password: str | None
        """
        self.password = password
        self._strong = 0
        self.is_valid: bool = self._is_valid()

    def __bool__(self):
        return self.is_valid

    def _is_valid(self) -> bool:
        """Check if text is valid

        :rtype: bool
        """
        count = 0
        for char in self.password:
            if char.isupper():
                count += 1

        self._strong = 1 + count // 2
        return self._strong > 0

    def info(self) -> str:
        """Return info about strength password

        :return: password strength with uppercase letters
        :rtype: int
        """

        if self.is_valid is True:
            return "Check uppercase character: OK"
        return "Check uppercase character: NOT"

    def get_strong(self) -> int:
        """Getter for self._strong

        :return: password strength with uppercase letters
        :rtype: int
        """
        return self._strong
