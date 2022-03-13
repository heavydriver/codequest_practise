import math

g_and_n = input()
g = float(g_and_n.split(" ")[0])
n = int(g_and_n.split(" ")[1])

m = []
angle = []

for x in range(0, n, 1):
    m_and_angle = input()
    m.append(float(m_and_angle.split(" ")[0]))
    angle.append(float(m_and_angle.split(" ")[1]))

for x in range(0, n, 1):
    f = (m[x] * g * math.sin(math.radians(angle[x])))
    print("%0.2f" % f)