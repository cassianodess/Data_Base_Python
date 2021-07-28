import mysql.connector
from os import system


# Cria conexão
while True:
    system("clear || cls")
    try:
        print("=========================")
        print("      LOGIN  MYSQL       ")
        print("=========================")
        usuario = input("Digite o usuário:\n>>> ")
        senha = input("Digite a senha:\n>>> ")

        bd = mysql.connector.connect(
            host="localhost",
            user=usuario,
            password=senha,
            database=""
        )
        cursor = bd.cursor()  # Cursor que executará as Querys
        input(">>> Conectado com sucesso!\nPressione para continuar...")
        system("clear || cls")
        break
    except:
        system("clear || cls")
        op = int(input("""=========================        
Usuário ou senha inválida
=========================
[ 1 ] - Tentar novamente
[ 2 ] - Sair
>>> """))
        if op == 2:
            break


def CriarDataBase(dataBase="exemplo"):  # Criar uma database
    cursor.execute(f"create database {dataBase}")
    cursor.execute(f"use {dataBase}")
    input(
        f"Data Base '{dataBase}'criado com sucesso!\nPressione para continuar...")


def ShowDataBases():
    cursor.execute("show databases")
    print(f"""==================
    DATA BASES
==================""")
    for x in cursor:
        print("> ", x[0])
    input("Pressione para continuar...")


def DropDataBase(dataBase):  # Apagar um database
    cursor.execute(f"drop database {dataBase}")
    input(
        f"Data Base '{dataBase}' excluído com sucesso!\nPressione para continuar...")


def CreateTable(schema, tabela):
    cursor.execute(
        f"create table if not exists {schema}.{tabela}(id int not null auto_increment primary key, nome varchar(20), idade int)")
    input(f"Tabela {tabela} criada com sucesso!\nPressione para continuar...")


def Inserir(schema, tabela, nome, cpf):  # Exemplo de tabela estilo "CLIENTE"
    sql = f"insert into {schema}.{tabela} (nome, cpf) values (%s, %s)"
    val = (nome, cpf)
    cursor.execute(sql, val)
    bd.commit()


def ListarTabelas(schema):
    cursor.execute(f"use {schema}")
    cursor.execute(f"show tables")
    print(f"""===============
    TABELAS
===============""")
    for x in cursor:
        print("> ", x[0])
    input("Pressione para continuar...")


def Menu():

    while True:
        system("clear || cls")
        op = int(input("""===============================
   Integração MySQL x PYTHON
===============================
[ 1 ] - Criar Data Base
[ 2 ] - Mostra Data Bases
[ 3 ] - Criar Tabela
[ 4 ] - Inserir Dados na Tabela
[ 5 ] - Mostrar Tabelas
[ 6 ] - Remover Data Base
[ 7 ] - Sair
>>>>  """))
        if op == 1:
            system("clear || cls")
            nome = input("Digite o nome do Data Base: ")
            CriarDataBase(nome)
        elif op == 2:
            system("clear || cls")
            ShowDataBases()
        elif op == 3:
            system("clear || cls")
            schema = input("Digite o nome do Data Base a ser usado:")
            tabela = input("Digite o nome da tabela:")
            CreateTable(schema, tabela)
        elif op == 4:
            system("clear || cls")
            schema = input("Digite o nome do Data Base a ser usado:")
            tabela = input("Digite o nome da tabela:")
            nome = input("Digite o nome do cliente: ")
            cpf = input("Digite o CPF do cliente: ")
            Inserir(schema, tabela, nome, cpf)

        elif op == 5:
            system("clear || cls")
            schema = input("Digite o nome do Data Base a ser usado:")
            ListarTabelas(schema)
        elif op == 6:
            schema = input("Digite o nome do Data base a ser removido: ")
            DropDataBase(schema)

        elif op == 7:
            break
        else:
            input(">> Opção inválida! Tente novamente! ")


if __name__ == "__main__":
    Menu()
