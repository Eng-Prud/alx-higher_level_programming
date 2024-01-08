def say_my_name(first_name, last_name=""):
    """
    Prints My name is <first name> <last name>

    Prototype: def say_my_name(first_name, last_name=""):
    first_name must be a string, otherwise,
    raise a TypeError exception with the message
    first_name must be a string
    last_name must be a string, otherwise,
    raise a TypeError exception with the message
    last_name must be a string
    You are not allowed to import any module
    """

    # Validate first_name input
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    # Validate last_name input
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Print the formatted name
    print("My name is {} {}".format(first_name, last_name))
