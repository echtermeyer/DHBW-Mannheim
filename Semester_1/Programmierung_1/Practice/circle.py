import math


class Circle:
    __seriennummer = 0

    @classmethod
    def get_series(cls):
        return cls.__seriennummer

    def __init__(self, x: float, y: float, r: float) -> None:
        Circle.__seriennummer += 1
        self.__seriennummer = Circle.__seriennummer

        self.__x = x
        self.__y = y
        self.__r = r

    def get_radius(self) -> float:
        return self.__r

    def set_radius(self, r) -> None:
        if r >= 0:
            self.__r = r

    def get_area(self) -> float:
        return self.__r ** 2 * math.pi

    def get_serie(self) -> int:
        return self.__seriennummer


c1 = Circle(0, 0, 1)
c2 = Circle(1, 4, 7.5)
c3 = Circle(2.1, -12, 0.01)

print("Areas: ", c1.get_area(), c2.get_area(), c3.get_area())

print("Set c2: ", c2.set_radius(20))
print("Get c2: ", c2.get_radius())
print("Get c2 Area: ", c2.get_area())

try:
    c1.__r = 100

    print(c1.get_area())
    print(c1.__r)
except:
    print("Alles wie geplant")


print(c1.get_serie(), c2.get_serie())
print(Circle.get_series())

