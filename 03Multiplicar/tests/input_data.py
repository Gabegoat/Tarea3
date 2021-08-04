import re
# List of tuples
# Each tuple contains a test: the first element are the inputs, the second are the output, and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    (
        # Inputs
        ["1"],
        # Outputs
        [re.compile(".*"), re.compile(".*1 x 0 = 0"), re.compile(".*1 x 1 = 1"), re.compile(".*1 x 2 = 2"),
         re.compile(".*1 x 3 = 3"), re.compile(".*1 x 4 = 4"), re.compile(".*1 x 5 = 5"), re.compile(".*1 x 6 = 6"),
         re.compile(".*1 x 7 = 7"), re.compile(".*1 x 8 = 8"), re.compile(".*1 x 9 = 9"), re.compile(".*1 x 10 = 10")],
        # Error message
        "Verifica el comportamiento del programa"
    ),
    (
        # Inputs
        ["2"],
        # Outputs
        [re.compile(".*"), re.compile(".*2 x 0 = 0"), re.compile(".*2 x 1 = 2"), re.compile(".*2 x 2 = 4"),
         re.compile(".*2 x 3 = 6"), re.compile(".*2 x 4 = 8"), re.compile(".*2 x 5 = 10"), re.compile(".*2 x 6 = 12"),
         re.compile(".*2 x 7 = 14"), re.compile(".*2 x 8 = 16"), re.compile(".*2 x 9 = 18"), re.compile(".*2 x 10 = 20")],
        # Error message
        "Verifica el comportamiento del programa"
    ),
    (
        # Inputs
        ["99"],
        # Outputs
        [re.compile(".*"), re.compile(".*99 x 0 = 0"), re.compile(".*99 x 1 = 99"), re.compile(".*99 x 2 = 198"),
         re.compile(".*99 x 3 = 297"), re.compile(".*99 x 4 = 396"), re.compile(".*99 x 5 = 495"), re.compile(".*99 x 6 = 594"),
         re.compile(".*99 x 7 = 693"), re.compile(".*99 x 8 = 792"), re.compile(".*99 x 9 = 891"), re.compile(".*99 x 10 = 990")],
        # Error message
        "Verifica el comportamiento del programa"
    ),
    (
        # Inputs
        ["15"],
        # Outputs
        [re.compile(".*"), re.compile(".*15 x 0 = 0"), re.compile(".*15 x 1 = 15"), re.compile(".*15 x 2 = 30"),
         re.compile(".*15 x 3 = 45"), re.compile(".*15 x 4 = 60"), re.compile(".*15 x 5 = 75"), re.compile(".*15 x 6 = 90"),
         re.compile(".*15 x 7 = 105"), re.compile(".*15 x 8 = 120"), re.compile(".*15 x 9 = 135"), re.compile(".*15 x 10 = 150")],
        # Error message
        "Verifica el comportamiento del programa"
    )
]
