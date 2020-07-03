from bit import Bit
from i_bit import IBit

class TwoBytes(IBit):

    small: Bit
    big: Bit

    def __init__(self, big, small):
        self.small = small
        self.big = big

    def __invert__(self):
        return TwoBytes(~self.big, ~self.small)

    def __or__(self, other):
        return TwoBytes(self.big | other.big, self.small | other.small)

    def __and__(self, other):
        return TwoBytes(self.big & other.big, self.small & other.small)

    def __xor__(self, other):
        return TwoBytes(self.big ^ other.big, self.small ^ other.small)

    def __add__(self, other):
        small_bit, carry_small_bit = self.small + other.small

        big_bit, carry = Bit.full_add(self.big, other.big, carry_small_bit)

        return (TwoBytes(big_bit, small_bit), carry)
