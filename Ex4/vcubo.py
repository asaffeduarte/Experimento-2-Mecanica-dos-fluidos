import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simps

# Dados fornecidos
v_cubo = np.array([0, 0.342, 0.799, 1.087, 1.225, 1.225, 1.305, 1.257, 1.117, 0.882, 0.519, 0])
incertezas_v_cubo = np.array([0, 0.005, 0.007, 0.008, 0.008, 0.008, 0.008, 0.008, 0.008, 0.007, 0.006, 0])
r_quadrado = np.array([0.000729, 0.00059049, 0.00035721, 0.00018225, 0.00006561, 0.00000729, 0.00000729, 0.00006561, 0.00018225, 0.00035721, 0.00059049, 0.000729])

# Ajuste de interpolação polinomial de segundo grau
p_interp = np.polyfit(r_quadrado, v_cubo, 2)
f_interp = np.poly1d(p_interp)

# Valores para plotagem suave
r_quadrado_plot = np.linspace(min(r_quadrado), max(r_quadrado), 100)
v_cubo_plot_interp = f_interp(r_quadrado_plot)

# Calcular a área sob a curva ajustada usando a regra de Simpson
area = simps(v_cubo_plot_interp, r_quadrado_plot)

plt.figure(figsize=(10, 6))

# Plotar os dados originais e a curva ajustada
plt.errorbar(r_quadrado, v_cubo, yerr=incertezas_v_cubo, fmt='o', label='Dados Originais')
plt.plot(r_quadrado_plot, v_cubo_plot_interp, label='Interpolação', color='red')
plt.ylim(bottom=0)
plt.xlabel('r² (m²)')
plt.ylabel('v³ (m³/s³)')
plt.title('Velocidade ao Cubo em função da Posição Radial ao Quadrado (Interpolação)')
plt.legend()
plt.grid(True)

# Adicionar a área sob a curva como texto no gráfico, movendo mais para a esquerda
plt.text(0.0001, 0.2, f'Área sob a curva: {area:.4f}', fontsize=12, bbox=dict(facecolor='white', alpha=0.5))

plt.show()
