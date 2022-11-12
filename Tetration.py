import matplotlib.pyplot as plt
import numpy as np

# Variables
tet_base = 0.8
x_range = [1, 30]


# Put your function here
def recur_tet(b, n):
    if n == 1:
        return b
    else:
        return b ** recur_tet(b, n - 1)


def tetration(base, power):
    output = np.empty(len(power))
    for i in range(len(power)):
        output[i] = recur_tet(base, power[i])
    return output


x_data = np.arange(x_range[0], x_range[1] + 1)

s = tetration(tet_base, x_data)

fig, ax = plt.subplots()
ax.plot(x_data, s)
plt.yscale(value="linear")
ax.set(xlabel='x', ylabel='$\ ^x$b', title='$\ ^x${}'.format(str(tet_base)))
ax.grid()

plt.show()
