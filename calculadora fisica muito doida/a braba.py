import numpy as np

# Dados conhecidos
n = ...                 # Número de ventres (adimensional)
L = ...                 # Comprimento do fio no gerador (m)
m_objeto = ...        # Massa do objeto que gera a tensão (kg)
m_fio = ...             # Massa do fio (kg)
l_fio = ...           # Comprimento total do fio esticado (m)

# Incertezas
sigma_L = ...         # Incerteza do comprimento L (m)
sigma_m_objeto = ...    # Incerteza da massa do objeto (kg)
sigma_m_fio = ...      # Incerteza da massa do fio (kg)
sigma_l_fio = ...      # Incerteza do comprimento do fio (m)

# Constante da gravidade
g = 9.8  # m/s²

# Cálculo de T e μ
T = m_objeto * g
mu = m_fio / l_fio

# Cálculo da frequência
f = (n / (2 * L)) * np.sqrt(T / mu)

# Derivadas parciais
# Derivadas em relação a L
df_dL = - (n / (2 * L**2)) * np.sqrt(T / mu)

# Derivada em relação a T
df_dT = (n / (4 * L)) * (1 / np.sqrt(T * mu))

# Derivada em relação a μ
df_dmu = - (n / (4 * L)) * (np.sqrt(T) / (mu ** (3/2)))

# Incerteza da tensão (T = m_objeto * g)
sigma_T = sigma_m_objeto * g

# Incerteza da densidade linear (μ = m_fio / l_fio)
sigma_mu = mu * np.sqrt(
    (sigma_m_fio / m_fio) ** 2 +
    (sigma_l_fio / l_fio) ** 2
)

# Propagação da incerteza da frequência
sigma_f = np.sqrt(
    (df_dL * sigma_L) ** 2 +
    (df_dT * sigma_T) ** 2 +
    (df_dmu * sigma_mu) ** 2
)

# Saída dos resultados
print(f"Frequência f = {f:.4f} Hz")
print(f"Incerteza da frequência σ_f = {sigma_f:.4f} Hz")
