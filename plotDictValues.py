import matplotlib.pyplot as plt
#import pickle

#with open('loc_dict.pkl','rb') as fp:
#    loc = pickle.load(fp)

fig, ax = plt.subplots()
x_data = []
y_data = []
for pt in loc.values():
    x_data.append(pt[0])
    y_data.append(pt[1])
ax.plot(x_data,y_data)
plt.yscale(value="linear")
ax.set(xlabel='x', ylabel='y')
ax.grid()

plt.show()
