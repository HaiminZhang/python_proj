
from scipy.stats import beta
import matplotlib.pyplot as plt

import numpy as np

a, b = 2, 2 

mean, var, skew, kurt = beta.stats(a, b, moments='mvsk')

x = np.linspace(0, 1, 100)
plt.plot(x, beta.pdf(x, a, b), 'r-', lw=5, alpha=0.6, label='beta pdf')
plt.show()
