import numpy as np
import matplotlib.pyplot as plt

MAX_LEVEL = 6


def sierpinski(p1, p2, p3, level=0):
    if level >= MAX_LEVEL:
        yield plt.Polygon([p1, p2, p3], color='green')
        return

    yield from sierpinski(p1, (p1+p2) / 2, (p1+p3) / 2, level+1)
    yield from sierpinski((p1+p2) / 2, p2, (p2+p3) / 2, level+1)
    yield from sierpinski((p1+p3) / 2, (p2+p3) / 2, p3, level+1)


plt.figure()
plt.scatter([0, 0, 10, 10], [0, 10, 0, 10], color='blue')

for patch in sierpinski(
        np.array([1.0, 1.0]), np.array([9.0, 1.0]), np.array([5.0, 9.0])):
    plt.gca().add_patch(patch)

plt.show()

# изменения