import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline

# Dados de velocidade e posição radial
velocidades = np.array([0, 0.700, 0.9280, 1.0281, 1.0701, 1.0701, 1.0927, 1.0792, 1.0375, 0.9591, 0.804, 0])
incertezas_velocidades = np.array([0, 0.003, 0.0026, 0.0024, 0.0023, 0.0023, 0.0022, 0.0023, 0.0024, 0.0026, 0.003, 0])
posicoes_radiais = np.array([0.0270, 0.0243, 0.0189, 0.0135, 0.0081, 0.0027, -0.0027, -0.0081, -0.0135, -0.0189, -0.0243, -0.0270])

# Ordenar os dados pela posição radial
indices_ordenados = np.argsort(posicoes_radiais)
posicoes_radiais_ordenadas = posicoes_radiais[indices_ordenados]
velocidades_ordenadas = velocidades[indices_ordenados]
incertezas_velocidades_ordenadas = incertezas_velocidades[indices_ordenados]

# Interpolação spline suavizada
spline_suave = UnivariateSpline(posicoes_radiais_ordenadas, velocidades_ordenadas, s=0.01)

# Valores para plotagem suave
posicoes_plot = np.linspace(posicoes_radiais_ordenadas.min(), posicoes_radiais_ordenadas.max(), 100)
velocidades_plot_spline_suave = spline_suave(posicoes_plot)

# Plotagem do gráfico
plt.errorbar(posicoes_radiais_ordenadas, velocidades_ordenadas, yerr=incertezas_velocidades_ordenadas, fmt='o', label='Dados')
plt.plot(posicoes_plot, velocidades_plot_spline_suave, label=f'Interpolação Suavizada', color='red')
plt.ylim(bottom=0)
plt.xlabel('Posição Radial (m)')
plt.ylabel('v (m/s)')
plt.title('Perfil de Velocidades em Relação à Posição Radial (Interpolação)')
plt.legend()
plt.grid(True)
plt.show()
