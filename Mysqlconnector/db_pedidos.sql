CREATE DATABASE db_pedidos;
USE db_pedidos;

CREATE TABLE pedido (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente VARCHAR(100)
);

CREATE TABLE item_pedido (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pedido_id INT,
    produto VARCHAR(100),
    quantidade INT,
    preco DECIMAL(10,2),
    categoria VARCHAR(100),
    FOREIGN KEY (pedido_id) REFERENCES pedido(id)
);
-- Exemplo de inserção
INSERT INTO pedido (cliente) VALUES ('João Silva');
INSERT INTO item_pedido (pedido_id, produto, quantidade, preco, categoria) VALUES (1, 'Notebook', 2, 3500.00, 'Eletrônicos');

-- Exemplo de atualização
UPDATE item_pedido SET quantidade = 3, categoria = 'Informática' WHERE id = 1;

-- Exemplo de listagem
SELECT p.id AS pedido_id, p.cliente, i.id AS item_id, i.produto, i.quantidade, i.preco, i.categoria
FROM pedido p
JOIN item_pedido i ON p.id = i.pedido_id;

-- Exemplo de deleção
DELETE FROM item_pedido WHERE id = 1;
DELETE FROM pedido WHERE id = 1;