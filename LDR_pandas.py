import pandas as pd
import matplotlib.pyplot as plt

pwm = list(range(6))
A0 = [0.0, 0.5, 1.2, 2.3, 3.8, 4.5]
A1 = [0.0, 0.4, 0.9, 1.4, 2.2, 2.8]

df = pd.DataFrame({
    "pwm (v)": pwm,
    "A0 (V)": A0,
    "A1 (V)": A1,
})

df["Corrente (I) [A]"] = (df["A0 (V)"] - df["A1 (V)"]) / 47

print("GRÁFICO LDR")
print(df)

plt.figure(figsize=(6, 4))
plt.plot(df["A0 (V)"], df["Corrente (I) [A]"], marker='o', color='blue')
plt.xlabel("Tensão A0 (V)")
plt.ylabel("Corrente I (A)")
plt.title("Gráfico LDR (I vs V)")
plt.grid(True)
plt.tight_layout()
plt.show()