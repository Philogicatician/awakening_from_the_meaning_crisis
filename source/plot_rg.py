import matplotlib.pyplot as plt
import numpy as np


def v(y):
    return h**2 - y**2


h = 2
x = np.linspace(0, 5, 101)
y = np.linspace(-2, 2, 101)
v = v(y)

plt.plot(x, v)
plt.xlabel('Reflectiveness Gap')
plt.ylabel('Agency')
plt.title('Gaining and Losing Agency through the Reflectiveness Gap')
plt.setp(plt.gcf().get_axes(), xticks=[], yticks=[]);
plt.savefig('images/rg_agency.png')


if __name__ == '__main__':
    pass

