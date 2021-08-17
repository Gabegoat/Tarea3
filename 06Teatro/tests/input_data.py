import re
# List of tuples
# Each tuple contains a test: the first element are the inputs, the second are the output, and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    (
        # Inputs
        ["5", "15", "20", "46", "66", "0"],
        # Outputs
        [re.compile(".*"), re.compile(".*35[ ]?[%]"), re.compile(".*"), re.compile(".*25[ ]?[%]"),
         re.compile(".*"), re.compile(".*10[ ]?[%]"), re.compile(".*"), re.compile(".*25[ ]?[%]"),
         re.compile(".*"), re.compile(".*35[ ]?[%]"), re.compile(".*"), re.compile(".*[ ]260[.]?[0]?")],
        # Error message
        "Verifica el funcionamiento, el total perdido es de 260. Verificar limites inferiores de las edades"
    ),
    (
        # Inputs
        ["14", "19", "45", "65", "100", "0"],
        # Outputs
        [re.compile(".*"), re.compile(".*35[ ]?[%]"), re.compile(".*"), re.compile(".*25[ ]?[%]"),
         re.compile(".*"), re.compile(".*10[ ]?[%]"), re.compile(".*"), re.compile(".*25[ ]?[%]"),
         re.compile(".*"), re.compile(".*35[ ]?[%]"), re.compile(".*"), re.compile(".*[ ]260[.]?[0]?")],
        # Error message
        "Verifica el funcionamiento, el total perdido es de 260. Verificar limites superiores de las edades"
    ),
    (
        # Inputs
        ["12", "17", "43", "62", "70", "0"],
        # Outputs
        [re.compile(".*"), re.compile(".*35[ ]?[%]"), re.compile(".*"), re.compile(".*25[ ]?[%]"),
         re.compile(".*"), re.compile(".*10[ ]?[%]"), re.compile(".*"), re.compile(".*25[ ]?[%]"),
         re.compile(".*"), re.compile(".*35[ ]?[%]"), re.compile(".*"), re.compile(".*[ ]260[.]?[0]?")],
        # Error message
        "Verifica el funcionamiento, el total perdido es de 260. Verificar los rangos de edad"
    ),
    (
        # Inputs
        ["10", "10", "20", "0"],
        # Outputs
        [re.compile(".*"), re.compile(".*35[ ]?[%]"), re.compile(".*"), re.compile(".*35[ ]?[%]"),
         re.compile(".*"), re.compile(".*10[ ]?[%]"), re.compile(".*"), re.compile(".*[ ]160[.]?[0]?")],
        # Error message
        "Verifica el funcionamiento, el total perdido es de 160"
    )
]
