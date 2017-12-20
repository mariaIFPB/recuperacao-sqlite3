from Database.UsuarioDAO import UsuarioDAO
from Database.ComentarioDAO import ComentarioDAO
from Model.Usuario import Usuario
from Model.Comentario import Comentario

'''
Função para exibir o menu
'''
def exibirMenu():
    print("\n====== Bem Vindo!! =======\n"
        "Opções:\n"
        "1 - Cadastrar usuário.\n"
        "2 - Atualizar dados do usuário. \n"
        "3 - Listar usuário\n"
        "4 - Excluir conta usuário \n"
        "5 - Comentar\n"
        "6 - Listar comentário\n"
        "0 - Sair\n"
        "===========================")

    opcao = int(input("\nInforme sua opção: "))

    if (opcao == 1):
        nome = input("informe seu nome: ")
        email = input("informe seu email: ")
        telefone = input("informe seu telefone: ")
        senha = input("informe a senha: ")
        genero = input("informe o seu gênero: ")
        data_nasc = input("informe sua data de nascimento: ")
        profissao = input("informe sua profissão: ")
        cidade = input("informe sua cidade: ")
        global u
        u = Usuario(nome, email, telefone, senha, genero, data_nasc, profissao, cidade)
        global uDAO
        uDAO = UsuarioDAO()
        uDAO.inserirUsuario(u)
        exibirMenu()

    elif(opcao == 2):
        telefone = input("Informe seu novo número de telefone: ")
        email = input("informe o seu novo email: ")
        u = Usuario("", email, telefone, "", "", "", "", "")
        uDAO = UsuarioDAO()
        uDAO.atualizarFoneEmail(u)
        exibirMenu()

    elif(opcao == 3):
        uDAO = UsuarioDAO()
        uDAO.listarUsuarios()
        exibirMenu()

    elif(opcao == 4):
        email = input("Informe o email da conta a ser deletada: ")
        uDAO.deletarUsuario(email)
        exibirMenu()

    elif(opcao==5):
        texto = input("informe o texto: ")
        c = Comentario(texto)
        cDAO = ComentarioDAO()
        cDAO.postar_comentario(c)
        print("Comentário realizado com sucesso.")
        exibirMenu()

    elif(opcao == 6):
        cDAO = ComentarioDAO()
        cDAO.listarComentarios()
        exibirMenu()

    elif(opcao == 0):
        print("Programa finalizado.")

    else:
        print("opção inválida.")

if __name__ == "__main__":
    exibirMenu()
