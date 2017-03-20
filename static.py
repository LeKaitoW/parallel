import math
import numpy as np
import matplotlib.pyplot as plot

N = 2  # количество процессоров: 2, 4, 8, 16, 32, 64

a = 1.0
b = -0.1
# x_2 = a*x_1+b
# C_f = const

C_omega = 0
C_g = 0
C_functional = 0

x_min = 0
x_max = 1
points = 256
Z = pow(points, 2)

m = 100
l = 8
t = 10 * pow(10, -9)
t_s = 50 * pow(10, -6)
t_c = 1 / 80 * pow(10, -6)
d = 2 * math.sqrt(N) - 1


class Point:
    def __init__(self, x_one, x_two):
        self.x_one = x_one
        self.x_two = x_two


def decomposition_p():
    subdomains = []
    current = 0
    for i in range(N):
        current += x_max / N
        subdomains.append(current)
    z = math.ceil(Z / N)


def create_points():
    points_list = []
    x_one = 0
    x_two = 0
    delta = 1 / points
    for i in range(points):
        for j in range(points):
            points_list.append(Point(x_one, x_two))
            x_one += delta
        x_two += delta


create_points()
decomposition_p()

plot.plot([x_max, x_max])
plot.plot([x_max, x_max], [x_min, x_max])
x_1 = np.arange(x_min, x_max+0.1, 0.05)
plot.plot(x_1, a * x_1 + b, 'r--')
plot.axis([0, 1.5, 0, 1.5])
plot.show()
