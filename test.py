from logic import *

def init_buses(first_value, second_value):
    return (Bus(first_value), Bus(second_value))

def test():
    and_gate(*init_buses(False, False)).test(False)
    and_gate(*init_buses(False, True)).test(False)
    and_gate(*init_buses(True, False)).test(False)
    and_gate(*init_buses(True, True)).test(True)

    or_gate(*init_buses(False, False)).test(False)
    or_gate(*init_buses(False, True)).test(True)
    or_gate(*init_buses(True, False)).test(True)
    or_gate(*init_buses(True, True)).test(True)

    xor_gate(*init_buses(False, False)).test(False)
    xor_gate(*init_buses(False, True)).test(True)
    xor_gate(*init_buses(True, False)).test(True)
    xor_gate(*init_buses(True, True)).test(False)

