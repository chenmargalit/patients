# An example of validation as expected value ranges were not discussed
# (e.g. length of text etc.).

def validate_inp(value, should_be_type):

    if should_be_type == str:
        if (value.isdigit()): return False

    if type(value) != should_be_type: return False
    else: return True

