f1 = open("C:/Work/JAVA/NumericalAnalysis/Cond1.txt")
f2 = open("C:/Work/JAVA/NumericalAnalysis/Cond1PreTreatment.txt")
s1 = f1.read()
sn1 = s1.split(" ")
st1 = list(map(float, sn1))
print(st1)
s2 = f2.read()
sn2 = s2.split(" ")
st2 = list(map(float, sn2))
print(st2)
import numpy as np
import matplotlib.pyplot as plt

f, ax = plt.subplots(1, 1)
plt.plot(np.linspace(1,100,100,endpoint=True), st2)
plt.plot(np.linspace(1,100,100,endpoint=True), st1,"-")
# plt.plot(np.linspace(1,15,15,endpoint=True), st2[0:15])
# plt.plot(np.linspace(1,15,15,endpoint=True), st1[0:15],"-")
plt.ylabel("Cond1")
plt.xlabel("n")
ax.set_yscale('log')
# plt.locator_params("x",nbins = 14)
plt.title("Pretreatment Hilbert's Cond1 in Different Dimension")
plt.show()