SELECT descUF,
        count(DISTINCT idPedido) as qtdePedido

FROM pedido

GROUP BY 1