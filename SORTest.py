f = open("C:/Work/JAVA/NumericalAnalysis/SORTimes.txt")
s = f.read()
sn = s.split(" ")
st = list(map(int, sn))
print(st)
import numpy as np
import matplotlib.pyplot as plt

plt.plot(np.linspace(1,100,100,endpoint=True), st)
plt.xlabel("n")
plt.ylabel("Times")
plt.title("SORIteration Times in Different Dimension")
plt.show()