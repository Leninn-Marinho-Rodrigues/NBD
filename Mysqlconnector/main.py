from database import Database
from models import Pedido, ItemPedido
from control import PedidoControl

if __name__ == "__main__":
    db = Database(host='localhost', user='root', password='', database='db_pedidos')
    control = PedidoControl(db)
    #pedido=Pedido(cliente="Claudio Ulisse")
    #pedido.id=7
    #control.atualizar_pedido(pedido)
    # Inserção
    novo_pedido = Pedido(cliente="João Silva")
    novo_item = ItemPedido(produto="Notebook", quantidade=1, preco=3500.0, categoria="Eletrônicos")
    novo_pedido.itens.append(novo_item)
    control.salvar_pedido(novo_pedido)

    # Atualização
    novo_pedido.cliente = "João S. Atualizado"
    novo_pedido.itens[0].categoria = "Informática"
    control.atualizar_pedido(novo_pedido)

    # Listagem
    pedidos = control.listar_pedidos_com_itens()
    for p in pedidos:
        print(f"Pedido {p.id} - Cliente: {p.cliente}")
        for i in p.itens:
            print(f"  Produto: {i.produto}, Quantidade: {i.quantidade}, Preço: {i.preco}, Categoria: {i.categoria}")

    # Deleção
    control.deletar_pedido(novo_pedido.id)
   # control.salvar_pedido(pedido)

    pedidos = control.listar_pedidos_com_itens()
    for p in pedidos:
        print(f"Pedido {p.id} - Cliente: {p.cliente} - Data: {p.data_pedido}")
        for i in p.itens:
            print(f"  Produto: {i.produto}, Quantidade: {i.quantidade}, Preço: {i.preco}")

    db.close()
