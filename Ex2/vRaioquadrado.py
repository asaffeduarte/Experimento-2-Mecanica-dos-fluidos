import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simps

# Dados fornecidos
velocidades = np.array([0, 0.700, 0.9280, 1.0281, 1.0701, 1.0701, 1.0927, 1.0792, 1.0375, 0.9591, 0.804, 0])
incertezas_velocidades = np.array([0, 0.003, 0.0026, 0.0024, 0.0023, 0.0023, 0.0022, 0.0023, 0.0024, 0.0026, 0.003, 0])
posicoes_quadrado = np.array([0.000729, 0.00059049, 0.00035721, 0.00018225, 0.00006561, 0.00000729, 0.00000729, 0.00006561, 0.00018225, 0.00035721, 0.00059049, 0.000729])

# Ajuste de curva de segundo grau (parábola)
coefs = np.polyfit(posicoes_quadrado, velocidades, 2)
p = np.poly1d(coefs)

# Criar pontos ao longo da curva ajustada
x_fit = np.linspace(min(posicoes_quadrado), max(posicoes_quadrado), 100)
y_fit = p(x_fit)

# Calcular a área sob a curva ajustada usando a regra de Simpson
area = simps(y_fit, x_fit)

# Plotar os dados originais e a curva ajustada
plt.errorbar(posicoes_quadrado, velocidades, yerr=incertezas_velocidades[:len(posicoes_quadrado)], fmt='o', label='Dados Originais')
plt.plot(x_fit, y_fit, label='Curva Ajustada', color='red')
plt.ylim(bottom=0)
plt.xlabel('r² (m²)')
plt.ylabel('v (m/s)')
plt.title('Velocidades em função de r² com interpolação')
plt.legend()
plt.grid(True)

# Adicionar a área sob a curva como texto no gráfico, movendo mais para a esquerda
plt.text(0.0001, 0.2, f'Área sob a curva: {area:.4f}', fontsize=12, bbox=dict(facecolor='white', alpha=0.5))

plt.show()
