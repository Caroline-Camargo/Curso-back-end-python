import sqlite3 as sql

# 1. Crie uma tabela chamada "alunos" com os seguintes campos: id (inteiro), nome (texto), idade (inteiro) e curso (texto).
def ex_01(cursor):
    cursor.execute('CREATE TABLE alunos (id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100))')


# 2. Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.
def ex_02(cursor):
    cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (1, "Caroline", 22, "Ciência da Computação")')
    cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (2, "Yasmin", 23, "Ciência da Computação")')
    cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (3, "Ana", 25, "Engenharia")')
    cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (4, "João", 20, "Engenharia")')
    cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (5, "Maria", 18, "Medicina")')


'''
3. Consultas Básicas
    a) Escreva consultas SQL para realizar as seguintes tarefas:
        i) Selecionar todos os registros da tabela "alunos".
        ii) Selecionar o nome e a idade dos alunos com mais de 20 anos.
        iii) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
        iv) Contar o número total de alunos na tabela.
'''
def ex_03(cursor):
    consulta = cursor.execute('SELECT * FROM alunos')
    print('Todos os alunos:')
    for aluno in consulta:
        print(aluno)

    consulta = cursor.execute('SELECT nome, idade FROM alunos WHERE idade > 20')
    print('\nAlunos com mais de 20 anos:')
    for aluno in consulta:
        print(aluno)

    consulta = cursor.execute('SELECT nome, idade FROM alunos WHERE curso == "Engenharia" ORDER BY nome')
    print('\nAlunos do curso de Engenharia em ordem alfabética:')
    for aluno in consulta:
        print(aluno)

    consulta = cursor.execute('SELECT COUNT(*) FROM alunos')
    print('\nNúmero total de alunos:')
    for aluno in consulta:
        print(aluno[0])


'''
4. Atualização e Remoção
    a) Atualize a idade de um aluno específico na tabela.
    b) Remova um aluno pelo seu ID.
'''
def ex_04(cursor):
    cursor.execute('UPDATE alunos SET idade = 21 WHERE nome = "Ana"')
    cursor.execute('DELETE FROM alunos WHERE id = 5')


'''
5. Criar uma Tabela e Inserir Dados
    a) Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float).
    b) Insira alguns registros de clientes na tabela.
'''
def ex_05(cursor):
    cursor.execute('CREATE TABLE clientes (id INT PRIMARY KEY, nome VARCHAR(100), idade INT, saldo REAL)')
    cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (1, "Caroline", 22, 1000.0)')
    cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (2, "Yasmin", 23, 2000.0)')
    cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (3, "Ana", 25, 55000.0)')
    cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (4, "João", 20, 500.0)')
    cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (5, "Maria", 18, 10000.0)')


'''
6. Consultas e Funções Agregadas
    a) Escreva consultas SQL para realizar as seguintes tarefas:
        i) Selecionar o nome e a idade dos clientes com idade superior a 30 anos.
        ii) Calcular o saldo médio dos clientes.
        iii) Encontrar o cliente com o saldo máximo.
        iv) Contar quantos clientes têm saldo acima de 1000.
'''
def ex_06(cursor):
    consulta = cursor.execute('SELECT nome,idade FROM clientes WHERE idade > 30')
    print('Clientes com idade superior a 30 anos:')
    for cliente in consulta:
        print(cliente)

    consulta = cursor.execute('SELECT AVG(saldo) FROM clientes')
    print('\nSaldo médio dos clientes')
    for cliente in consulta:
        print(cliente[0])

    consulta = cursor.execute('SELECT nome FROM clientes WHERE saldo == (SELECT MAX(saldo) FROM clientes)')
    print('\nNome do cliente com maior saldo: ')
    for cliente in consulta:
        print(cliente[0])
    
    consulta = cursor.execute('SELECT COUNT(saldo) FROM clientes WHERE saldo > 1000')
    print('\nQuantidade de clientes com saldo acima de 1000: ')
    for cliente in consulta:
        print(cliente[0])


'''
7. Atualização e Remoção com Condições
    a) Atualize o saldo de um cliente específico.
    b) Remova um cliente pelo seu ID.
'''
def ex_07(cursor):
    cursor.execute('UPDATE clientes SET saldo = 10000.0')
    cursor.execute('DELETE FROM clientes WHERE id == 5')


'''
8. Junção de Tabelas
    a) Crie uma segunda tabela chamada "compras" com os campos: id (chave primária), cliente_id (chave estrangeira referenciando o id da tabela "clientes"), produto (texto) e valor (real).
    b) Insira algumas compras associadas a clientes existentes na tabela "clientes".
    c) Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.
'''
def ex_08(cursor):
    cursor.execute('''
        CREATE TABLE compras(
                   id INT PRIMARY KEY, 
                   cliente_id INT, 
                   produto VARCHAR(100), 
                   valor REAL,
                   FOREIGN KEY(cliente_id) REFERENCES clientes(id)
        )
    ''')

    cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (1, 2, "notebook", 3000.0)')
    cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (2, 2, "cadeira", 500.0)')
    cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (3, 1, "celular", 200.0)')
    cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (4, 3, "telefone", 1000.0)')
    cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (4, 4, "farinha", 12.0)')

    consulta = cursor.execute('SELECT nome,produto,valor FROM compras INNER JOIN clientes ON cliente_id = clientes.id')
    print('\nConsulta compras clientes')
    for aluno in consulta:
        print(aluno)


conection = sql.connect('database_exercicios') 
cursor = conection.cursor() 

#ex_01(cursor)
#ex_02(cursor)
#ex_03(cursor)
#ex_04(cursor)
#ex_04(cursor)
#ex_05(cursor)
#ex_06(cursor)
#ex_07(cursor)
#ex_08(cursor)

conection.commit() 
conection.close()  