import re
# List of tuples
# Each tuple contains a test: the first element are the inputs, the second are the output, and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    (
        # Inputs
        ["6", "4", "2", "6", "4",
         "2", "6", "4", "2", "6",
         "6", "4", "2", "6", "4",
         "2", "6", "4", "2", "6"],
        # Outputs
        [re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*"),
        re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*"),
        re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*"),
        re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*"),
        re.compile(".*20$"), re.compile(".*0$"), re.compile(".*0$")],
        # Error message
        "Verifica el comportamiento del programa"
    ),
    (
        # Inputs
        ["86", "44", "24", "76", "46",
         "-2", "-6", "-4", "-2", "-6",
         "0", "0", "0", "0", "0",
         "-2", "-6", "-4", "-2", "-6"],
        # Outputs
        [re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*"),
        re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*"),
        re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*"),
        re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*"),
        re.compile(".*5$"), re.compile(".*10$"), re.compile(".*5$")],
        # Error message
        "Verifica el comportamiento del programa"
    ),
    (
        # Inputs
        ["86", "44", "24", "76", "46",
         "0", "0", "0", "0", "0",
         "0", "0", "0", "0", "0",
         "-9", "-25", "-44", "-22", "-79"],
        # Outputs
        [re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*"),
        re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*"),
        re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*"),
        re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*"),
        re.compile(".*5$"), re.compile(".*5$"), re.compile(".*10$")],
        # Error message
        "Verifica el comportamiento del programa"
    ),
(
        # Inputs
        ["1", "2", "3", "4", "5",
         "0", "0", "0", "-1", "79",
         "0", "0", "0", "-999", "82",
         "-9", "-25", "-44", "-22", "-79"],
        # Outputs
        [re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*"),
        re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*"),
        re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*"),
        re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*"),
        re.compile(".*7$"), re.compile(".*7$"), re.compile(".*6$")],
        # Error message
        "Verifica el comportamiento del programa"
    )
]
