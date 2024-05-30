import numpy as np
import matplotlib.pyplot as plt

# Dados de velocidade e posição radial
velocidades = np.array([0, 0.700, 0.9280, 1.0281, 1.0701, 1.0701, 1.0927, 1.0792, 1.0375, 0.9591, 0.804, 0])
incertezas_velocidades = np.array([0, 0.003, 0.0026, 0.0024, 0.0023, 0.0023, 0.0022, 0.0023, 0.0024, 0.0026, 0.003, 0])
posicoes_radiais = np.array([0.0270, 0.0243, 0.0189, 0.0135, 0.0081, 0.0027, -0.0027, -0.0081, -0.0135, -0.0189, -0.0243, -0.0270])

# Ajuste de uma função quadrática
p_quadratico = np.polyfit(posicoes_radiais, velocidades, 2)
f_quadratico = np.poly1d(p_quadratico)

# Valores para plotagem suave
posicoes_plot = np.linspace(posicoes_radiais.min(), posicoes_radiais.max(), 100)
velocidades_plot_quadratico = f_quadratico(posicoes_plot)

# Coeficiente de correlação
correlacao = np.corrcoef(velocidades, f_quadratico(posicoes_radiais))[0, 1]

# Formatação da equação quadrática
a, b, c = p_quadratico
equacao_quadratica = f'{a:.4f}x² + {b:.4f}x + {c:.4f}'

# Plotagem do gráfico
plt.errorbar(posicoes_radiais, velocidades, yerr=incertezas_velocidades, fmt='o', label='Dados')
plt.plot(posicoes_plot, velocidades_plot_quadratico, label=f'Interpolação', color='red')
plt.ylim(bottom=0)
plt.xlabel('Posição Radial (m)')
plt.ylabel('v (m/s)')
plt.title('Perfil de Velocidades em Relação à Posição Radial (Interpolação)')
plt.legend()
plt.grid(True)
plt.show()
