from logic import *
from i_bit import IBit

class Bit(IBit):
    bus: Bus

    def __init__(self, value: Bus):
        self.bus = value

    @classmethod
    def init_with_value(cls, value):
        return Bit(Bus(value))

    def __invert__(self):
        return Bit(not_gate(self.bus))

    def __or__(self, other):
        return Bit(or_gate(self.bus, other.bus))

    def __and__(self, other):
        return Bit(and_gate(self.bus, other.bus))

    def __xor__(self, other):
        return Bit(xor_gate(self.bus, other.bus))

    def __add__(self, other):
        carry = self & other
        rem = self ^ other
        return (rem, carry)
