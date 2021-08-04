import re
# List of tuples
# Each tuple contains a test: the first element are the inputs, the second are the output, and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    (
        # Inputs
        ["2"],
        # Outputs
        [re.compile(".*"), re.compile(".*True")],
        # Error message
        "El numero 2 es primo"
    ),
    (
        # Inputs
        ["3"],
        # Outputs
        [re.compile(".*"), re.compile(".*True")],
        # Error message
        "El numero 3 es primo"
    ),
    (
        # Inputs
        ["7907"],
        # Outputs
        [re.compile(".*"), re.compile(".*True")],
        # Error message
        "El numero 7907 es primo"
    ),
    (
        # Inputs
        ["80"],
        # Outputs
        [re.compile(".*"), re.compile(".*False")],
        # Error message
        "El numero 80 no es primo"
    ),
    (
        # Inputs
        ["7920"],
        # Outputs
        [re.compile(".*"), re.compile(".*False")],
        # Error message
        "El numero 7920 no es primo"
    )
]
