"""Function for validator module"""


def special_char_choice(value: str | None) -> str:
    """Function generate special characters

    :param value: "min" | "max" | None
    :rtype: str
    """
    if value == "min":
        return r"@$!%*#?&"
    if value == "max":
        return r"\"!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    return r""
