Projeto de Conexão e ORM com Schema Modificado
Este projeto demonstra a adaptação de implementações de acesso a banco de dados (BD) com foco em manipulação de pedidos (pedido) e itens de pedido (item_pedido), refletindo alterações no esquema (schema) original do MySQL.

🎯 Objetivo Principal
O objetivo foi modificar a estrutura de dados existente e validar a completa funcionalidade C.R.U.D. (Create, Read, Update, Delete) nas seguintes plataformas:

MySQL Connector (Simulado via SQLite): Demonstração do uso de comandos SQL brutos.

SQLAlchemy ORM (Em Memória): Demonstração do uso de Mapeamento Objeto-Relacional.

⚙️ Modificações Estruturais (Schema)
As seguintes alterações foram implementadas no esquema das tabelas pedido e item_pedido para modernizar a estrutura:

Remoção da Coluna data_pedido: A coluna de data de criação de pedidos foi removida da tabela pedido, simplificando a entidade.

Adição da Coluna categoria: Uma nova coluna categoria (VARCHAR 100) foi adicionada à tabela item_pedido, permitindo classificar os produtos de forma granular (ex.: 'Eletrônicos', 'Tecnologia').

✅ Testes C.R.U.D. Validados
Ambos os projetos contêm rotinas de teste automatizadas que validam as quatro operações essenciais:

Operação

Teste Realizado

Foco na Nova Estrutura

CREATE (Inserção)

Criação de um Cliente, um Pedido e um Item.

Confirma que a inserção do Item Pedido requer o campo categoria.

READ (Listagem)

Consulta do Pedido e listagem detalhada do Item.

Valida a leitura da categoria do item e a ausência da data_pedido no Pedido.

UPDATE (Atualização)

Modificação da categoria de um Item Pedido específico.

Confirma a alteração bem-sucedida no novo campo categoria.

DELETE (Deleção)

Remoção completa do Cliente, Pedido e todos os Itens relacionados.

Garante a integridade referencial e a limpeza completa dos registros.
