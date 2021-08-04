import re
# List of tuples
# Each tuple contains a test: the first element are the inputs, the second are the output, and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    (
        # Inputs
        ["5", "17", "8", "9", "45", "87", "0"],
        # Outputs
        [re.compile(".*"), re.compile(".*35[ ]?[%]"), re.compile(".*"), re.compile(".*25[ ]?[%]"),
         re.compile(".*"), re.compile(".*35[ ]?[%]"), re.compile(".*"), re.compile(".*35[ ]?[%]"),
         re.compile(".*"), re.compile(".*10[ ]?[%]"), re.compile(".*"), re.compile(".*35[ ]?[%]"),
         re.compile(".*"), re.compile(".*")],
        # Error message
        "Puedes recibir numeros negativos"
    )
]
