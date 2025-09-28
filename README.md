🐍 Projeto de Adaptação de Schema e Validação C.R.U.D.
Demonstração de proficiência em Engenharia de Dados e ORM, aplicando mudanças de schema em projetos legados e validando a integridade dos dados.

✨ Habilidades Técnicas em Destaque
Este projeto prova a capacidade de gerenciar o ciclo de vida de um banco de dados, desde a definição do esquema até a manipulação de dados em tempo real, utilizando diferentes abordagens de acesso, vou explicar o codigo basicamente: 

Habilidade

Descrição

Modelagem de Dados

Capacidade de entender e aplicar alterações de DDL (remoção e adição de colunas) em um modelo relacional.

Integração ORM

Implementação e adaptação de classes Python para mapeamento com SQLAlchemy, garantindo a persistência.

SQL Nativo

Domínio do uso de comandos DML (INSERT, UPDATE, DELETE) em implementações raw com MySQL Connector (simulado).

Testes de Cobertura

Validação do C.R.U.D. completo para garantir que as alterações do schema não introduziram inconsistências.

⚙️ Modificações do Schema Relacional
O esquema original do banco de dados de pedidos foi modificado com foco em otimização e granularidade de dados:

❌ Remoção Estratégica
Tabela pedido: A coluna data_pedido foi removida.

(Rationale: Simplicidade e delegação da gestão de tempo para timestamps automáticos do BD ou lógica da aplicação.)

✅ Adição Funcional
Tabela item_pedido: Adição da nova coluna categoria (VARCHAR 100).

(Rationale: Maior capacidade analítica e classificação granular dos produtos, suportando filtros e relatórios.)

🚀 Validação C.R.U.D. (Testes de Integração)
O código garante que, após as alterações de schema, todas as operações fundamentais funcionam perfeitamente em ambas as implementações (SQLAlchemy e MySQL Connector).

Operação

Teste Realizado

Ponto de Checagem do Novo Schema

CREATE (Inserção)

Cria um Pedido e insere o Item.

Confirma a obrigatoriedade da nova coluna categoria durante o INSERT.

READ (Leitura)

Lista os detalhes do Pedido e seus Itens.

Valida a leitura correta do valor de categoria e confirma a ausência da data_pedido.

UPDATE (Atualização)

Modifica o valor da categoria do Item.

Demonstra a capacidade de alterar o valor da nova coluna categoria.

DELETE (Deleção)

Remove todos os registros criados (Item, Pedido e Cliente).

Confirma a integridade referencial e a limpeza completa do BD.
