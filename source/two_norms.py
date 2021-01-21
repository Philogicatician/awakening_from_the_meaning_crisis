import matplotlib.pyplot as plt
import numpy as np

from scipy.stats import norm

"""
Plot two overlapping normal distibutions.
Base on: https://stackoverflow.com/questions/32551610/overlapping-probability-of-two-normal-distribution-with-scipy
"""


def solve(m1, m2, std1, std2):
    """
    Get point of intersect.
    """
    a = 1/(2*std1**2) - 1/(2*std2**2)
    b = m2/(std2**2) - m1/(std1**2)
    c = m1**2 / (2*std1**2) - m2**2 / (2*std2**2) - np.log(std2/std1)

    return np.roots([a, b, c])


m1 = 2.5
std1 = 1.0
m2 = 5.5
std2 = 1.0

result = solve(m1, m2, std1, std2)
#print(result)

# Plot the two Gaussians with overlap.
x = np.linspace(-2, 10, 10000)
plot1 = plt.plot(x, norm.pdf(x, m1, std1))
plot2 = plt.plot(x, norm.pdf(x, m2, std2))

# Plot integrated area.
r = result[0]
olap = plt.fill_between(x[x>r], 0, norm.pdf(x[x>r], m1, std1), alpha=0.3)
olap = plt.fill_between(x[x<r], 0, norm.pdf(x[x<r], m2, std2), alpha=0.3)

# Prettify plot.
plt.title("Signal vs Noise")
plt.xlabel("Overlap")
plt.setp(plt.gcf().get_axes(), xticks=[], yticks=[])

plt.savefig("signal_vs_noise.png")
#plt.show()

if __name__ == '__main__':
    pass

