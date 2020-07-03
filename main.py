from bit import Bit
from two_bit import TwoBytes
from core_helper import Bus
from core_helper import connect_light

def main():
    x = TwoBytes(Bit.init_with_value(False), Bit.init_with_value(False))
    y = TwoBytes(Bit.init_with_value(False), Bit.init_with_value(False))

    res, car = x + y

    print(":)")

if __name__ == '__main__':
    main()
