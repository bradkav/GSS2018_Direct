import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import rc
from scipy.interpolate import interp1d
import numpy as np
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)

data = pd.read_csv("Tungsten", "\t")
data.x = [float(i.replace(",", ".")) for i in data.x.values]
data.y = [float(i.replace(",", ".")) for i in data.y.values]
x, y = zip(*sorted(zip(data.x.values, data.y.values), key= lambda x: x[0]))
for i in range(len(x)-1):
    if x[i] >= x[i+1]:
        x_new = np.delete(x,i)
        y_new = np.delete(y,i)

x = x_new
y = y_new

f = interp1d(np.array(x), np.array(y), kind='cubic')

plt.semilogy(np.linspace(0.2,78,100), [f(i) for i in np.linspace(0.2,78,100)], label="Tungsten (W)")

data2 = pd.read_csv("Argon", "\t")
data2.x = [float(i.replace(",", ".")) for i in data2.x.values]
data2.y = [float(i.replace(",", ".")) for i in data2.y.values]
x, y = zip(*sorted(zip(data2.x.values, data2.y.values), key= lambda x: x[0]))
f = interp1d(np.array(x), np.array(y), kind='cubic')
plt.semilogy(np.linspace(0.3,78,100), [f(i) for i in np.linspace(0.3,78,100)], label="Argon (Ar)")
plt.legend()
plt.ylim([5e-10, 5e-4])
plt.xlim([0,80])
plt.title(r"Influence of the mass of the nucleus")
plt.xlabel(r"Nuclear recoil energy [keV]")
plt.ylabel(r"Rate [Events kg$^{-1}$ d$^{-1}$ keV$^{-1}$]")
plt.savefig("mass_influence.png", dpi=300)
