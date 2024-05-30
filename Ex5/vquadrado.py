import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simps

# Dados fornecidos
v_quadrado = np.array([0, 0.489, 0.861, 1.057, 1.145, 1.145, 1.194, 1.165, 1.077, 0.920, 0.646, 0])
incertezas_v_quadrado = np.array([0, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0])
r_quadrado = np.array([0.000729, 0.00059049, 0.00035721, 0.00018225, 0.00006561, 0.00000729, 0.00000729, 0.00006561, 0.00018225, 0.00035721, 0.00059049, 0.000729])

# Ajuste de interpolação polinomial de segundo grau
p_interp = np.polyfit(r_quadrado, v_quadrado, 2)
f_interp = np.poly1d(p_interp)

# Valores para plotagem suave
r_quadrado_plot = np.linspace(min(r_quadrado), max(r_quadrado), 100)
v_quadrado_plot_interp = f_interp(r_quadrado_plot)

# Calcular a área sob a curva ajustada usando a regra de Simpson
area = simps(v_quadrado_plot_interp, r_quadrado_plot)

plt.figure(figsize=(10, 6))
# Plotar os dados originais e a curva ajustada
plt.errorbar(r_quadrado, v_quadrado, yerr=incertezas_v_quadrado, fmt='o', label='Dados Originais')
plt.plot(r_quadrado_plot, v_quadrado_plot_interp, label='Interpolação', color='red')
plt.ylim(bottom=0)
plt.xlabel('Posições Radiais ao Quadrado (m²)')
plt.ylabel('Velocidade ao Quadrado (m²/s²)')
plt.title('Relação entre Velocidade ao Quadrado e Posição Radial ao Quadrado (Interpolação)')
plt.legend()
plt.grid(True)

# Adicionar a área sob a curva como texto no gráfico, movendo mais para a esquerda
plt.text(0.0001, 0.2, f'Área sob a curva: {area:.4f}', fontsize=12, bbox=dict(facecolor='white', alpha=0.5))

plt.show()
