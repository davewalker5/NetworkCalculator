def prompt_for_string(prompt):
    """
    Prompt for a string

    :param prompt: User-friendly prompt
    :return: A string or None if cancelled
    """
    user_input = input(prompt + ("?" if not prompt.endswith("?") else "") + " ")
    return None if user_input == "" else user_input


def prompt_for_number(prompt, data_type_name, converter, minimum_value=None, maximum_value=None):
    """
    Prompt for an integer

    :param prompt: User-friendly prompt
    :param data_type_name: Name of the data type
    :param converter: Function to use to convert the user input to a number
    :param minimum_value: Minimum acceptable value
    :param maximum_value: Maximum acceptable value
    :return: Integer value or None if cancelled
    """
    while True:
        try:
            # Prompt for user input - if the input is empty, return nothing
            user_input = input(prompt + ("?" if not prompt.endswith("?") else "") + " ")
            if user_input == "":
                return None

            # Convert to an integer
            number = converter(user_input)
            if minimum_value and number < minimum_value:
                print("Number must be >= ", minimum_value)
            elif maximum_value and number > maximum_value:
                print("Number must be <= ", maximum_value)
            else:
                return number

        except ValueError:
            print("Please enter a valid " + data_type_name)


def prompt_for_integer(prompt, minimum_value=None, maximum_value=None):
    """
    Prompt for an integer

    :param prompt: User-friendly prompt
    :param minimum_value: Minimum acceptable value
    :param maximum_value: Maximum acceptable value
    :return: Integer value or None if cancelled
    """
    return prompt_for_number(prompt, "integer", int, minimum_value, maximum_value)


def prompt_for_option_with_values(options, values, prompt):
    """
    Prompt for an option from a list of options

    :param options: List of options
    :param values: Corresponding values
    :param prompt: User prompt
    :return: Corresponding value for the selected option
    """
    label_length = len(str(len(options)))
    for i, option in enumerate(options):
        label = str(i + 1).rjust(label_length, " ")
        print(label + ": " + str(option))

    print()

    selection = prompt_for_integer(prompt, minimum_value=1, maximum_value=len(options))
    value = values[selection - 1] if selection is not None and values else selection
    return value


def prompt_for_option(options, prompt):
    """
    Prompt for an option from a list of options

    :param options: List of options
    :param prompt: User prompt
    :return: Index for the selected option
    """
    return prompt_for_option_with_values(options, None, prompt)
