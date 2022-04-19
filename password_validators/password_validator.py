"""Main module"""
# local code
from password_validators.validator import Validator
from password_validators.password_uppercase_char_validator import PasswordUppercaseCharValidator
from password_validators.password_lowercase_char_validator import PasswordLowercaseCharValidator
from password_validators.password_number_validator import PasswordNumberValidator
from password_validators.password_special_char_validator import PasswordSpecialCharValidator
from password_validators.password_length_validator import PasswordLengthValidator
from password_validators.password_pwned_validator import PasswordPWNEDValidator


class PasswordValidator(Validator):
    """Validator that checks if password is safe"""
    def __init__(self, password: str | None):
        """
        :param password:
        :type password: str | None
        """
        self.password = password
        self._strong: int = 0
        self.validators = [
            PasswordUppercaseCharValidator,
            PasswordLowercaseCharValidator,
            PasswordNumberValidator,
            PasswordSpecialCharValidator,
            PasswordLengthValidator,
            PasswordPWNEDValidator,
        ]
        self.is_valid = self._is_valid()

    def __bool__(self):
        return self.is_valid

    def _is_valid(self) -> bool:
        """Check if text is valid
        :raises

        :rtype: bool
        """
        strong = [class_name(self.password).get_strong() for class_name in self.validators]
        self._strong = min(strong)
        result = [bool(class_name(self.password)) for class_name in self.validators]
        return all(result)

    def info(self) -> str:
        """Returns information about the correctness of the password

        :return: password strength
        :rtype: int
        """

        if self.is_valid is True:
            return "Check all: OK"
        return "Check all: NOT"

    def get_strong(self) -> int:
        """Getter for self._strong

        :return: password strength with uppercase letters
        :rtype: int
        """

        return self._strong

    def get_detail_info(self):
        """Return info about strength password

        :return: password strength with uppercase letters
        :rtype: str
        """

        if self._strong > 3:
            return 'Excellent password'
        if self._strong == 3:
            return 'Good password'
        if self._strong == 2:
            return 'Medium password'
        if self._strong == 1:
            return 'Insufficient password'
        return 'Bad password'


if __name__ == "__main__":
    input_password = input("Enter the password to be checked: ")
    valid = PasswordValidator(input_password)
    print(valid.info())
    print(valid.get_detail_info())
