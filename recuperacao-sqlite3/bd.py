import sqlite3

# Criando as tabelas: usuario, comentário


conn = sqlite3.connect('IFNetwork.db')
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE tb_usuario(
        id INTEGER AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        email VARCHAR(100) NOT NULL,
        telefone VARCHAR (15),
        senha VARCHAR(15) NOT NULL,
        genero VARCHAR(15),
        data_nasc DATE,
        profissao VARCHAR(50),
        cidade VARCHAR(50)
        );
        """)

cursor.execute("""
    CREATE TABLE tb_comentaario(
        id INTEGER AUTO_INCREMENT PRIMARY KEY,
        data_coment DATE
        texto VARCHAR(500)
        );
        """)

print("banco criado.")
