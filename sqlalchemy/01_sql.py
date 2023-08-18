# %% 
import pandas as pd
import sqlalchemy
# %%

# estudar sobre sqlalchemy
# criando uma engine para fazer a conexão
engine = sqlalchemy.create_engine("sqlite:///../data/database.db")
# %%

query = 'SELECT * FROM produto WHERE vlPreco > 10'

df_prod_10 = pd.read_sql_query(query, engine)
# %%
df_prod_10
# %%

# usando uma query em um arquivo separado
def import_query(path):
    with open(path, 'r') as open_file:
        query = open_file.read()
    return query


# %%
query = import_query('pedido_item_preco.sql')
print(query)
# %%
df_item_pedido_preco = pd.read_sql(import_query('pedido_item_preco.sql'), engine)
df_item_pedido_preco
# %%

query_uf_pedido = import_query('qtde_pedido_estado.sql')
df_pedido_estado = pd.read_sql_query(query_uf_pedido, engine)
df_pedido_estado
# %%

import matplotlib.pyplot as plt
# %%

df_pedido_estado.boxplot('qtdePedido')
# %%

top5_uf = df_pedido_estado.sort_values('qtdePedido', ascending=False).head(5)
# %%

import datetime
top5_uf.to_sql('top5_uf_pedido1', engine)

# %%
