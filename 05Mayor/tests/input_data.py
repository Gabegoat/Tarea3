import re
# List of tuples
# Each tuple contains a test: the first element are the inputs, the second are the output, and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    (
        # Inputs
        ["9", "5", "4", "8", "-9", "45", "878", "545", "45", "0"],
        # Outputs
        [re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*"),
         re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*878")],
        # Error message
        "Puedes recibir numeros negativos, el resultado deberia ser 878"
    ),
    (
        # Inputs
        ["10", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
        # Outputs
        [re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*"),
         re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*"),
         re.compile(".*9")],
        # Error message
        "Verifica el programa, deberia regresar un 9"
    ),
    (
        # Inputs
        ["9", "2", "3", "4", "5", "6", "7", "8", "9", "0"],
        # Outputs
        [re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*"),
         re.compile(".*"), re.compile(".*"), re.compile(".*"),  re.compile(".*9")],
        # Error message
        "El numero mayor puede estar en cualquier lugar del conjunto de datos"
    ),
    (
        # Inputs
        ["17", "987", "987", "789", "582", "657", "165", "158", "456", "450", "457", "983", "157", "128", "252",
         "558", "121", "909"],
        # Outputs
        [re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*"),
         re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*"),
         re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*"), re.compile(".*"),
         re.compile(".*"), re.compile(".*987")],
        # Error message
        "El numero mayor puede estar en cualquier lugar del conjunto de datos"
    )
]
