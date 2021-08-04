import re
# List of tuples
# Each tuple contains a test: the first element are the inputs, the second are the output, and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    (
        # Inputs
        ["7918"],
        # Outputs
        [re.compile(".*"), re.compile(".*7907")],
        # Error message
        "El primo mas cercano a 7918 es 7907"
    ),
    (
        # Inputs
        ["600"],
        # Outputs
        [re.compile(".*"), re.compile(".*599")],
        # Error message
        "El primo mas cercano a 600 es 599"
    ),
    (
        # Inputs
        ["112"],
        # Outputs
        [re.compile(".*"), re.compile(".*109")],
        # Error message
        "El primo mas cercano a 112 es 109"
    ),
    (
        # Inputs
        ["15"],
        # Outputs
        [re.compile(".*"), re.compile(".*13")],
        # Error message
        "El primo mas cercano a 15 es 13"
    )
]
