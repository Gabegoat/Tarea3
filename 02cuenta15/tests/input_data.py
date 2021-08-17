import re
# List of tuples
# Each tuple contains a test: the first element are the inputs, the second are the output, and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    (
        # Inputs
        ["-86", "-44", "-24", "-76", "-46",
         "-2", "-6", "-4", "-2", "-6",
         "-2", "-6", "-4", "-2", "-6"],
        # Outputs
        [re.compile(".*"), re.compile(".*86[.]?[0]?$"), re.compile(".*"), re.compile(".*44[.]?[0]?$"), re.compile(".*"),
        re.compile(".*24[.]?[0]?$"), re.compile(".*"), re.compile(".*76[.]?[0]?$"), re.compile(".*"),
        re.compile(".*46[.]?[0]?$"), re.compile(".*"), re.compile(".*2[.]?[0]?$"), re.compile(".*"),
        re.compile(".*6[.]?[0]?$"), re.compile(".*"), re.compile(".*4[.]?[0]?$"), re.compile(".*"), re.compile(".*2[.]?[0]?$"), re.compile(".*"),
        re.compile(".*6[.]?[0]?$"), re.compile(".*"), re.compile(".*2[.]?[0]?$"), re.compile(".*"), re.compile(".*6[.]?[0]?$"), re.compile(".*"),
        re.compile(".*4[.]?[0]?$"), re.compile(".*"), re.compile(".*2[.]?[0]?$"), re.compile(".*"), re.compile(".*6[.]?[0]?$")],
        # Error message
        "Verifica el comportamiento del programa"
    ),
    (
        # Inputs
        ["-1", "-2", "-3", "-4", "-5",
         "-6", "-7", "-8", "-9", "-10",
         "-11", "-12", "-13", "-14", "-15"],
        # Outputs
        [re.compile(".*"), re.compile(".*1[.]?[0]?$"), re.compile(".*"), re.compile(".*2[.]?[0]?$"), re.compile(".*"),
        re.compile(".*3[.]?[0]?$"), re.compile(".*"), re.compile(".*4[.]?[0]?$"), re.compile(".*"), re.compile(".*5[.]?[0]?$"),
        re.compile(".*"), re.compile(".*6[.]?[0]?$"), re.compile(".*"), re.compile(".*7[.]?[0]?$"), re.compile(".*"), re.compile(".*8[.]?[0]?$"),
        re.compile(".*"), re.compile(".*9[.]?[0]?$"), re.compile(".*"), re.compile(".*10[.]?[0]?$"), re.compile(".*"), re.compile(".*11[.]?[0]?$"),
        re.compile(".*"), re.compile(".*12[.]?[0]?$"), re.compile(".*"), re.compile(".*13[.]?[0]?$"), re.compile(".*"), re.compile(".*14[.]?[0]?$"),
        re.compile(".*"), re.compile(".*15[.]?[0]?$")],
        # Error message
        "Verifica el comportamiento del programa"
    )
]
