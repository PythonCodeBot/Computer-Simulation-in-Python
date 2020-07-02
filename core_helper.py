
class Bus:
    __value: bool
    name: str = None

    def __init__(self, value: bool):
        self.__value = value

    @classmethod
    def type(cls, value: bool, name: str):
        bus = Bus(value)
        bus.name = name
        return bus

    def __add__(self, other):
        """
        or gate, connecting two buses together
        :param other: the secend bus
        :return: new bus of or logic
        """
        return Bus(self.__value or other.__value)

    def no(self):
        """
        not gate, invert the bit
        :return: new bus with the opposite bit
        """
        return Bus(not self.__value)

    def __repr__(self):

        name = self.name if self.name is not None else "light bulb"

        return (f"{name} is {'on' if (self.__value) else 'off'}")

    def test(self, value: bool):
        assert self.__value == value

connect_light = print
