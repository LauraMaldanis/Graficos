import numpy as np
import matplotlib.pyplot as plt

k = 2

V = np.linspace(0, 10, 100)

I = k * V

plt.figure(figsize=(8, 6))
plt.plot(V, I, label='I = 2V', color='blue')
plt.title('Resistores Lineares')
plt.xlabel('Tensão (V)')
plt.ylabel('Corrente (I)')
plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.legend()
plt.xlim(0, 10)
plt.ylim(0, 20)
plt.show()
