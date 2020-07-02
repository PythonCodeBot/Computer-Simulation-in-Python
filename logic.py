from core_helper import Bus

def not_gate(bus: Bus) -> Bus:
    return bus.no()

def or_gate(bus_a: Bus, bus_b: Bus) -> Bus:
    return bus_a + bus_b

def nor_gate(inputA: Bus, inputB: Bus) -> Bus:
    return or_gate(inputA, inputB).no()

def and_gate(inputA: Bus, inputB: Bus) -> Bus:
    return (inputA.no() + inputB.no()).no()

def nand_gate(inputA: Bus, inputB: Bus) -> Bus:
    return and_gate(inputA, inputB).no()

def xor_gate(inputA: Bus, inputB: Bus) -> Bus:
    return and_gate(nand_gate(inputA, inputB), or_gate(inputA, inputB))

def nxor_gate(inputA: Bus, inputB: Bus) -> Bus:
    return xor_gate(inputA, inputB).no()
