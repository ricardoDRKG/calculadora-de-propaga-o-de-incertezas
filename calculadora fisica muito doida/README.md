
# Cálculo da Frequência de Oscilação em um Fio Esticado com Propagação de Incertezas

## Descrição

Este código em Python calcula a **frequência de oscilação** de um fio esticado baseado nas condições de tensão, densidade linear e número de ventres. Além disso, faz a **propagação das incertezas** considerando os erros experimentais associados às grandezas medidas.

O modelo físico se baseia na equação da frequência para ondas estacionárias em um fio:

\[
f = \frac{n}{2L} \cdot \sqrt{\frac{T}{\mu}}
\]

Onde:

- \( f \) = frequência (Hz)  
- \( n \) = número de ventres (adimensional)  
- \( L \) = comprimento do segmento do fio (m)  
- \( T \) = tensão no fio (N)  
- \( \mu \) = densidade linear de massa do fio (kg/m)  

## Funcionalidades

- Cálculo da frequência de oscilação do fio
- Cálculo da incerteza da frequência através de derivadas parciais
- Consideração das incertezas associadas a:
  - Comprimento do fio
  - Massa do objeto que gera a tensão
  - Massa do fio
  - Comprimento total do fio

## Dependências

- Python 3.x
- Biblioteca NumPy

Instalação da dependência (se necessário):

```bash
pip install numpy
```

## Como usar

1. Substitua os valores `...` no código pelos valores do seu experimento:

```python
n = ...           # Número de ventres
L = ...           # Comprimento do fio no gerador (m)
m_objeto = ...    # Massa do objeto (kg)
m_fio = ...       # Massa do fio (kg)
l_fio = ...       # Comprimento total do fio esticado (m)

sigma_L = ...             # Incerteza do comprimento L (m)
sigma_m_objeto = ...      # Incerteza da massa do objeto (kg)
sigma_m_fio = ...         # Incerteza da massa do fio (kg)
sigma_l_fio = ...         # Incerteza do comprimento do fio (m)
```

2. Execute o script:

```bash
python nome_do_arquivo.py
```

3. O programa irá exibir no terminal:

- A frequência calculada (`f`)
- A incerteza da frequência (`σ_f`)

## Saída Exemplo

```
Frequência f = 120.4567 Hz
Incerteza da frequência σ_f = 1.2345 Hz
```

## Fórmulas utilizadas

- **Tensão no fio:**  
  \[
  T = m_{objeto} \cdot g
  \]

- **Densidade linear de massa:**  
  \[
  \mu = \frac{m_{fio}}{l_{fio}}
  \]

- **Incerteza da densidade linear:**  
  \[
  \sigma_\mu = \mu \cdot \sqrt{\left( \frac{\sigma_{m_{fio}}}{m_{fio}} \right)^2 + \left( \frac{\sigma_{l_{fio}}}{l_{fio}} \right)^2 }
  \]

- **Propagação da incerteza da frequência:**  
  Através das derivadas parciais da função em relação a \(L\), \(T\) e \(\mu\).

## Licença

Este projeto é livre para uso acadêmico e educacional.
