import numpy as np
import matplotlib.pyplot as plt

temperaturas = np.linspace(-20, 100, 500)

R0 = 10000 
B = 3950 

def resistencia_ntc(temperatura):
    return R0 * np.exp(B * (1 / (temperatura + 273.15) - 1 / (25 + 273.15)))

resistencias = resistencia_ntc(temperaturas)

plt.figure(figsize=(10, 6))
plt.plot(temperaturas, resistencias, label='Resistência NTC', color='blue')
plt.title('Gráfico NTC')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Resistência (Ω)')
plt.yscale('log')
plt.grid(True)
plt.legend()
plt.show()