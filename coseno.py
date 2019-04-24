import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.2)
coseno = np.cos(x)
seno = np.sin(x)

plt.plot(x, coseno, '-', linewidth=3, color='r')
plt.plot(x, seno, '-', linewidth=2, color='g')
plt.grid()
plt.axis('equal')
plt.xlabel('x')
plt.ylabel('y')
plt.title('grafica para maicol')
plt.show()
