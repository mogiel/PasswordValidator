from password_validators.password_validator import (
    PasswordMarkValidator,
    PasswordPWNEDValidator,
    PasswordValidator
)


# PasswordUppercaseCharacterValidator
# PasswordLowercaseCharacterValidator
# PasswordNumberValidator
# PasswordSpecialCharValidator
# PasswordLengthValidator
# PasswordMarkValidator
# PasswordPWNEDValidator
# PasswordValidator


# PasswordMarkValidator


def test_if_has_good_password():
    # given & when
    validator = PasswordMarkValidator('Aa9!1241213')

    # then
    assert validator.is_valid is True
    assert bool(validator) is True


def test_if_has_bad_password():
    # given & when
    validator = PasswordMarkValidator('Adw')

    assert validator.is_valid is False
    assert bool(validator) is False


def test_if_has_None():
    # given & when
    validator = PasswordMarkValidator()

    # then
    assert validator.is_valid is False
    assert bool(validator) is False


def test_if_has_good_password_with_4_4ign():
    # given & when
    validator = PasswordMarkValidator('Aa9!', min_char=4)

    # then
    assert validator.is_valid is True
    assert bool(validator) is True


# PasswordPWNEDValidator


def test_if_password_not_exist_in_PWND(requests_mock):
    content = "0982FCA069D559E5C78B4677476DC80851C:31151\r\n099FCA72D4DA56DC3B2874028189BBE25B1:4"

    requests_mock.get("https://api.pwnedpasswords.com/range/C7478", text=content)

    validator = PasswordPWNEDValidator("mateusz")
    # when
    assert validator.is_valid is False
    assert bool(validator) is False


def test_if_password_exist_in_PWND(requests_mock):
    content = "0982FCA069D559E5C7834677476DC80851C:31151\r\n099FCA72D4DA56DC3B2874028189BBE25B1:4"

    requests_mock.get("https://api.pwnedpasswords.com/range/C7478", text=content)

    # when
    validator = PasswordPWNEDValidator("mateusz")
    # then
    assert validator.is_valid is True


# PasswordValidator


def test_PasswordValidator_good(requests_mock):
    content = "0982FCA069D559E5C7834677476DC80851C:31151\r\n099FCA72D4DA56DC3B2874028189BBE25B1:4"

    requests_mock.get("https://api.pwnedpasswords.com/range/3B9B8", text=content)

    password_for_check = '11AAaa!!'
    validator = PasswordValidator(password_for_check)

    assert validator.__bool__() is True
    assert validator.get_strong() == 2


def test_PasswordValidator_bad(requests_mock):
    content = "1409823d602729f8421c7b3a175178d5aef:31151\r\n099FCA72D4DA56DC3B2874028189BBE25B1:4".upper()

    requests_mock.get("https://api.pwnedpasswords.com/range/3B9B8", text=content)

    password_for_check = '11AAaa!!'
    validator = PasswordValidator(password_for_check)

    assert validator.__bool__() is False

