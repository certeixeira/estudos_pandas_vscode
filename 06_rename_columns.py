# %%

import pandas as pd
# %%

df = pd.read_csv("data/pedido.csv")
# %%

df
# %%

# renomeando colunas
# utiliza-se um dicionário "de para" com o valor atual para o novo valor
df.rename(columns={"descUF": "descEstado"})
# %%

# puxando o df verificamos que o nome não foi alterado
df
# %%

# para salvar o resultado devemos atribuir a alteração a uma variável
df = df.rename(columns={"descUF": "descEstado"})
df
# %%

# outra maneira:
# implace altera o próprio objeto no caso o df
df.rename(columns={"descUF": "descEstado"}, inplace=True)
df
# %%
