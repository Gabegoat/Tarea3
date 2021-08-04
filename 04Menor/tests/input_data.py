import re
# List of tuples
# Each tuple contains a test: the first element are the inputs, the second are the output, and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    (
        # Inputs
        ["5 4 8 -9 45 878 54564 45 0"],
        # Outputs
        [re.compile(".*"), re.compile(".*-9")],
        # Error message
        "Puedes recibir numeros negativos"
    ),
    (
        # Inputs
        ["0 1 2 3 4 5 6 7 8 9"],
        # Outputs
        [re.compile(".*"), re.compile(".*0")],
        # Error message
        "El cero tambien es un numero"
    ),
    (
        # Inputs
        ["2 3 4 5 6 7 8 9 0"],
        # Outputs
        [re.compile(".*"), re.compile(".*0")],
        # Error message
        "El numero menor puede estar en cualquier lugar del conjunto de datos"
    ),
    (
        # Inputs
        ["987 987 789 582 65716 165 158 4569 450 457 9853 157 12859 1252 5458 121 999"],
        # Outputs
        [re.compile(".*"), re.compile(".*121")],
        # Error message
        "El numero menor puede estar en cualquier lugar del conjunto de datos"
    )
]
