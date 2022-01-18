import matplotlib.pyplot as plt
import numpy as np


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
        print(output[i])
    return output


# Generate an array
x_data = np.arange(1, 4)
print(x_data)

# Variables
tet_base = -1.1
s = tetration(tet_base, x_data)

fig, ax = plt.subplots()
ax.plot(x_data, s, label='test')
plt.yscale(value="linear")
plt.legend()
ax.set(xlabel='x', ylabel='y',
       title=str(tet_base) + '\u2191\u2191x')
ax.grid()

plt.show()
