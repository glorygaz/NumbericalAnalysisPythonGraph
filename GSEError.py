f = open("C:/Work/JAVA/NumericalAnalysis/GSEError.txt")
s = f.read()
sn = s.split(" ")
st = list(map(float, sn))
print(st)
import numpy as np
import matplotlib.pyplot as plt

f, ax = plt.subplots(1, 1)
plt.plot(np.linspace(1,30,30,endpoint=True), st)
# plt.plot(np.linspace(1,14,14,endpoint=True), st[0:14])
plt.xlabel("n")
plt.ylabel("Error")
ax.set_yscale('log')
plt.title("GSElimination Error in Different Dimension")
plt.show()