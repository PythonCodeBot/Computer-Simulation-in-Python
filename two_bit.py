from bit import Bit
from i_bit import IBit

class TwoBytes(IBit):

    small: Bit
    big: Bit

    def __init__(self, small, big):
        self.small = small
        self.big = big

    def __invert__(self):
        return TwoBytes(~self.small, ~self.big)

    def __or__(self, other):
        return TwoBytes(self.small | other.small,
                        self.big | other.big)

    def __and__(self, other):
        return TwoBytes(self.small & other.small,
                        self.big & other.big)

    def __xor__(self, other):
        return TwoBytes(self.small ^ other.small,
                        self.big ^ other.big)

    def __add__(self, other):
        small_bit, carry_small_bit = self.small + other.small

        big_bit, carry_big_bit = carry_small_bit + other.big

        big_bit, _ = big_bit + self.big

        return (TwoBytes(small_bit, big_bit), carry_big_bit)
