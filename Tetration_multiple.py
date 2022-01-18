import matplotlib
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
    return output


# Generate an array
x_data = np.arange(1, 30)
fig, ax = plt.subplots()

# Variables
tet_bases = np.arange(0.05, 0.2, 0.01)
print(tet_bases)
for base in tet_bases:
    s = tetration(base, x_data)
    ax.plot(x_data, s, label=str(np.around(base, decimals=3)))

# ax.plot(x_data, tetration(np.exp(1 / np.e), x_data), label='$e^{1/e}$', linewidth=2.0, color='k')
ax.plot(x_data, tetration(np.exp(-np.e), x_data), label='$e^{-e}$', linewidth=0.5, color='k')

matplotlib.rcParams['figure.dpi']=1000
plt.yscale(value="linear")
plt.ylim(0, 1)
# Shrink current axis by 20%
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

# Put a legend to the right of the current axis
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax.set(xlabel='x', ylabel='y',
       title=str(tet_bases[0]) + '\u2191\u2191x to ' + str(
           np.around(tet_bases[len(tet_bases) - 1], decimals=3)) + '\u2191\u2191x')
ax.grid()

plt.show()
