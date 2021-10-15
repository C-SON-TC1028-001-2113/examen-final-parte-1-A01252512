# List of tuples
# Each tuple contains a test: the first element are the inputs, the second are the output, and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1
    (
        # Inputs
        ["123"],
        # Outputs
        ["Enter a number: ", "321"],
        # Message in case of failure
        "Invert the digits of a positive integer"
    ),
    # Test case 2
    (
        # Inputs
        ["-8534"],
        # Outputs
        ["Enter a number: ", "-4358"],
        # Message in case of failure
        "Invert the digits of a negative integer"
    ),
    # Test case 3
    (
        # Inputs
        ["12345678"],
        # Outputs
        ["Enter a number: ", "Too long"],
        # Message in case of failure
        "Detect numbers that have more than 6 digits"
    ),
    # Test case 4
    (
        # Inputs
        ["984341"],
        # Outputs
        ["Enter a number: ", "143489"],
        # Message in case of failure
        "Invert the digits of a positive integer"
    ),
]
