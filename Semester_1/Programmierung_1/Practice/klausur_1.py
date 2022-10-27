def f(x, y, z):
    x = x + 1
    y + [1, 2, 3]
    z.append(1)

def g(x):
    def h(y):
        return x * y
    return h

def k(x, z=1, **kwargs):
    return f'x={x}, z={z}, kwargs={kwargs}'

def k2(x: str):
    return x(5)


w = 9
x = 1
y = [5, "hallo"]
z = ["x"]

f(x, y, z)
i = g(x)
j = g(10)

print(" 1.) ", x)
print(" 2.) ", y)
print(f" 3.) {z}")
print(" 4.) ", i(5))
print(" 5.) ", j(5))
print(" 6.)", w > 5)
print(" 7.)", w % 4)
print(" 7.)", w / 4)
print(" 8.)", w // 4)
print(" 9.)", w > 10 or w < 0)
print(" 9.)", w << 2)
print(" 9.)", w >> 2)
print("10.)", w & 0b101011001)
print("11.)", k(5, a=5, u=987))
print("12.)", k2(lambda i: i+5))


class Rectangle:
    def __init__(self, h, b):
        self.b = b
        self.h = h

    def get_area(self):
        return self.b * self.h


class Square(Rectangle):
    def __init__(self, w):
        super(Square, self).__init__(w, w)


s = Square(10)
print(s.get_area())