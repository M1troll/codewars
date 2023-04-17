import re


def alphanumeric(password: str) -> bool:
    """Check that password is alphanumeric."""             
    return re.search(re.compile("^[A-Za-z\d]{1,}$" ) , password) is not None


if __name__ == "__main__":
    print(alphanumeric("hello world_") is False)
    print(alphanumeric("PassW0rd") is True)
    print(alphanumeric("    ") is False)
