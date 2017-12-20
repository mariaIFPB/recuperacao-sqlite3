import sqlite3
from Model.Usuario import Usuario

class UsuarioDAO():

    def inserirUsuario(self, usuario: Usuario):
            conn = sqlite3.connect('IFNetwork.db')
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO tb_usuario(nome, email, telefone, senha, genero, data_nasc, profissao, cidade)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?);
                """, (usuario.nome, usuario.email, usuario.telefone, usuario.senha, usuario.genero, usuario.data_nasc, usuario.profissao, usuario.cidade))

            conn.commit()
            conn.close()

    def listarUsuarios(self):
        conn = sqlite3.connect('IFNetwork.db')
        cursor = conn.cursor()

        cursor.execute("""
        SELECT * FROM tb_usuario;
        """)
        for usuario in cursor.fetchall():
            print(usuario)

        conn.commit()
        conn.close()

    def atualizarFoneEmail(self, usuario: Usuario):
        emailAntigo = usuario.email
        opcao = int(input("\nDeseja mudar seu email?\n"
                      "1 - Sim"
                      "2 - Não"))
        if (opcao == 1):
            usuario.email = input("Informe o novo email: ")
        opcao = int(input("\nDeseja mudar seu numero de telefone?\n"
                      "1 - Sim"
                      "2 - Não"))
        if (opcao == 1):
            usuario.telefone = input('Informe o novo telefone: ')

        conn = sqlite3.connect('IFNetwork.db')
        cursor = conn.cursor()

        cursor.execute("""
            UPDADE tb_usuario
            SET email = ?, telefone = ?
            WHERE email = ?
        """, (usuario.email, usuario.telefone, emailAntigo))

    def deletarUsuario(self, email):

        conn = sqlite3.connect('IFNetwork.db')
        cursor = conn.cursor()
        cursor.execute("""
            DELETE FROM tb_usuario
            WHERE email = ?
            """, (email,))

        conn.commit()
        conn.close()
