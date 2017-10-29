import math
import matplotlib.pyplot as plot

# количество процессоров:
proc = [2, 4, 8, 16, 32, 64, 128, 256]

a = 1.0
b = -0.1
# x_2 = a*x_1+b
C_f_list = [pow(10, 5), pow(10,7)]

n = 2
C_omega = 0
C_g = 0
C_functional = 0

x_min = 0
x_max = 1
points = 32 #256
Z = pow(points, 2)

m = 100
l = 8
t = 10 * pow(10, -9)
t_s = 50 * pow(10, -6)
t_c = 1 / 80 * pow(10, -6)


class Point:
    def __init__(self, x_one, x_two):
        self.x_one = x_one
        self.x_two = x_two


def decomposition_p(N, point_list, C_f):
    d = math.ceil(2 * math.sqrt(N) - 1)
    subdomains = [0, ]
    current = 0
    for i in range(N):
        current += x_max / N
        subdomains.append(current)
    z = math.ceil(Z / N)

    points_dict = {}
    points_number = []
    i = 0
    while i < N:
        k = 0
        for point in points_list:
            if point in points_dict:
                continue
            left = subdomains[i]
            right = subdomains[i + 1]
            is_last = (i == N - 1)
            if (left <= point.x_one < right) or (is_last and point.x_one == right):
                if point.x_two - a * point.x_one - b >= 0:
                    points_dict.update({point: i})
                    k += 1
        points_number.append(k)
        i += 1
    points_in_subdomains = sum(points_number)

    T_1 = t * points_in_subdomains * C_f
    times = []
    for i in range(N):
        times.append(2 * t_s + z * n * l * d * t_c + points_number[i] * m * l * d * t_c + t * points_number[i] * C_f)
    T_N = max(times)
    S_1 = T_1 / T_N
    return round(S_1, 3)


def decomposition_node(N, points_list, C_f):
    d = math.ceil(2 * math.sqrt(N) - 1)
    points_number = 0
    for point in points_list:
        if point.x_two - a * point.x_one - b >= 0:
            points_number += 1

    print('point_num=', points_number)
    z = math.ceil(points_number / N)
    print('z=', z)
    T_N = 2 * t_s + z * ((n + m) * l * d * t_c + t * C_f)
    T_1 = t * points_number * C_f
    S_2 = T_1 / T_N
    return round(S_2, 3)


def create_points(points):
    points_list = []
    x_one = 0
    x_two = 0
    delta = (x_max - x_min) / (points - 1)
    for i in range(points):
        x_one = 0
        for j in range(points):
            points_list.append(Point(x_one, x_two))
            x_one += delta
        x_two += delta
    return points_list


boosts_p_0 = []
boosts_p_1 = []
boosts_nodes_0 = []
boosts_nodes_1 = []
points_list = create_points(points)
for p in proc:
    #boosts_p_0.append(decomposition_p(p, points_list, C_f_list[0]))
    #boosts_p_1.append(decomposition_p(p, points_list, C_f_list[1]))
    boosts_nodes_0.append(decomposition_node(p, points_list, C_f_list[0]))
    #boosts_nodes_1.append(decomposition_node(p, points_list, C_f_list[1]))
    #approx_boosts.append(p * (1 - a / 2) / (1 - a / (2 * p)))
#print(boosts_p_0)
#print(boosts_p_1)
#print(boosts_nodes_0)
#print(boosts_nodes_1)

#figure_1 = plot.figure()
#graph_1 = figure_1.add_subplot(111)
#graph_1.plot([x_max, x_max])
#graph_1.plot([x_max, x_max], [x_min, x_max])
#x_1 = np.arange(x_min, x_max + 0.05, 0.05)
#graph_1.plot(x_1, a * x_1 + b)
#graph_1.axis([0, 1.5, 0, 1.5])
#plot.xlabel('x1')
#plot.ylabel('x2')

#figure_2 = plot.figure()
#graph_2 = figure_2.add_subplot(111)
#line = np.arange(0, proc[len(proc)-1], 0.05)
#graph_2.plot(line, line)
#graph_2.plot(proc, boosts_p_0)
#graph_2.plot(proc, boosts_p_1)
#graph_2.axis([0, 65, 0, 65])
#plot.xlabel('N')
#plot.ylabel('S1')

#figure_3 = plot.figure()
#graph_3 = figure_3.add_subplot(111)
#graph_3.plot(line, line)
#graph_3.plot(proc, boosts_nodes_0)
#graph_3.plot(proc, boosts_nodes_1)
#graph_3.axis([0, 65, 0, 65])
#plot.xlabel('N')
#plot.ylabel('S2')

plot.show()
