def cadastrar_usuario():

    usuario = input("Digite o nome de usuário: ")
    print()
    while usuario.strip() == "":
        print("O nome de usuário não pode ser vazio. Tente novamente.")
        print()
        usuario = input("Digite o nome de usuário: ")
        print()
    arquivo = open("usuarios.txt", "r")

    for linha in arquivo.readlines():

        dados = linha.strip().split(";")

        if usuario == dados[0]:
            while True:
                arquivo.close()

                print()
                print("Usuário já existe. Tente novamente.")

                return
        elif usuario == " ":
            print("O nome de usuário não pode ser vazio. Tente novamente.")
            print()
            usuario = input("Digite o nome de usuário: ")
            print()
    senha = input("Digite a senha: ")

    arquivo = open("usuarios.txt", "a")

    arquivo.write(usuario + ";" + senha + "\n")

    arquivo.close()

    print()
    print("Usuário cadastrado!")


def fazer_login():

    usuario = input("Usuário: ")
    print()
    senha = input("Senha: ")

    arquivo = open("usuarios.txt", "r")

    for linha in arquivo.readlines():

        dados = linha.strip().split(";")

        if usuario == dados[0] and senha == dados[1]:

            arquivo.close()

            print()
            print("Login realizado!")

            return usuario

    arquivo.close()

    print()
    print("Usuário ou senha incorretos!")

    return ""

def criar_filmes():

    arquivo = open("filmes.txt", "w")

    arquivo.write("Vingadores Ultimato;3h;Acao;2019;Anthony Russo;0;0\n")
    arquivo.write("O Poderoso Chefao;2h 55m;Crime;1972;Francis Ford Coppola;0;0\n")
    arquivo.write("Euphoria;3 temp.;Drama;2019;Sam Levinson;0;0\n")
    arquivo.write("Clube da Luta;2h 19m;Acao;1999;David Fincher;0;0\n")
    arquivo.write("Titanic;3h 14m;Romance;1997;James Cameron;0;0\n")
    arquivo.write("Jurassic World - Recomeco;2h 14m;Ficcao Cientifica;2025;Gareth Edwards;0;0\n")
    arquivo.write("A Baleia;1h 57m;Drama;2022;Darren Aronofsky;0;0\n")
    arquivo.write("Super Mario Galaxy;1h 39m;Aventura;2026;Michael Jelenic;0;0\n")
    arquivo.write("Sonic;1h 39m;Infantil;2020;Jeff Fowler;2;0\n")
    arquivo.write("Uma Noite no Museu;1h 48m;Comedia;2005;Shawn Levy;0;0\n")
    arquivo.write("Deu a louca na Chapeuzinho;1h 20m;Infantil;2005;Cory Edwards;0;0\n")

    arquivo.close()


def listar_filmes():

    arquivo = open("filmes.txt", "r")

    print()
    print("========== FILMES ==========")

    for linha in arquivo.readlines():

        dados = linha.strip().split(";")

        print()
        print("Nome:", dados[0])
        print("Duração:", dados[1])
        print("Gênero:", dados[2])
        print("Ano:", dados[3])
        print("Diretor:", dados[4])
        print("Curtidas:", dados[5])
        print("Descurtidas:", dados[6])

    arquivo.close()


def buscar_filme():

    busca = input("Digite o nome do filme: ")

    arquivo = open("filmes.txt", "r")

    achou = False

    for linha in arquivo.readlines():

        dados = linha.strip().split(";")

        if busca.lower() in dados[0].lower():

            achou = True

            print()
            print("========== FILME ==========")
            print("Nome:", dados[0])
            print("Duração:", dados[1])
            print("Gênero:", dados[2])
            print("Ano:", dados[3])
            print("Diretor:", dados[4])
            print("Curtidas:", dados[5])
            print("Descurtidas:", dados[6])

    arquivo.close()

    if achou == False:

        print()
        print("Filme não encontrado!")


def curtir_filme():

    filme = input("Nome do filme: ")

    arquivo = open("filmes.txt", "r")

    linhas = arquivo.readlines()

    arquivo.close()

    arquivo = open("filmes.txt", "w")

    for linha in linhas:

        dados = linha.strip().split(";")

        if filme.lower() == dados[0].lower():

            dados[5] = str(int(dados[5]) + 1)

        nova_linha = ";".join(dados) + "\n"

        arquivo.write(nova_linha)

    arquivo.close()

    print()
    print("Filme curtido!")


def descurtir_filme():

    filme = input("Nome do filme: ")

    arquivo = open("filmes.txt", "r")

    linhas = arquivo.readlines()

    arquivo.close()

    arquivo = open("filmes.txt", "w")

    for linha in linhas:

        dados = linha.strip().split(";")

        if filme.lower() == dados[0].lower():

            dados[6] = str(int(dados[6]) + 1)

        nova_linha = ";".join(dados) + "\n"

        arquivo.write(nova_linha) #Ele reescreve a linha com a quantidade nova de descurtidas

    arquivo.close()

    print()
    print("Filme descurtido!")


def adicionar_favorito(usuario):

    filme = input("Digite o filme favorito: ")

    arquivo = open("favoritos.txt", "a")

    arquivo.write(usuario + ";" + filme + "\n")

    arquivo.close()

    print()
    print("Favoritado!")


def listar_favoritos(usuario):

    arquivo = open("favoritos.txt", "r")

    print()
    print("====== FAVORITOS ======")

    for linha in arquivo.readlines():

        dados = linha.strip().split(";")

        if usuario == dados[0]:

            print(dados[1])

    arquivo.close()


def remover_favorito(usuario):

    filme = input("Filme para remover: ")

    arquivo = open("favoritos.txt", "r")

    linhas = arquivo.readlines()

    arquivo.close()

    arquivo = open("favoritos.txt", "w")

    for linha in linhas:

        dados = linha.strip().split(";")

        if not(usuario == dados[0] and filme.lower() == dados[1].lower()):

            arquivo.write(linha)

    arquivo.close()

    print()
    print("Favorito removido!")


def menu_logado(nome):

    print()
    print()
    print()
    print("         ", end="")
    print("MENU DO USUÁRIO")
    print("        ", end="")
    print("-"*16)
    print()
    print("        ", end="")
    print("Bem-vindo, " + nome + "!")
    print()
    while True:
        print("(1) Listar Filmes")
        print("(2) Buscar Filme")
        print("(3) Curtir Filme")
        print("(4) Descurtir Filme")
        print("(5) Adicionar Favorito")
        print("(6) Listar Favoritos")
        print("(7) Remover Favorito")
        print("(0) Logout")

        print()

        x = input(": ")

        if x == "1":

            listar_filmes()

        elif x == "2":

            buscar_filme()

        elif x == "3":

            curtir_filme()

        elif x == "4":

            descurtir_filme()

        elif x == "5":

            adicionar_favorito(nome)

        elif x == "6":

            listar_favoritos(nome)

        elif x == "7":

            remover_favorito(nome)

        elif x == "0":

            print()
            print("Logout realizado!")

            break

        else:

            print()
            print("Opção inválida!")


def feitv():

    open("usuarios.txt", "a").close()
    open("favoritos.txt", "a").close()
    criar_filmes()

    print()

    print("     ", end="")
    print("-"*30)

    print("     ", end="")
    print("|          FEI TV 📺         |")

    print("     ", end="")
    print("-"*30)

    while True:

        print()
        print()
        print()

        print("         ", end="")
        print("SELECIONE UMA OPÇÃO")

        print("        ", end="")
        print("-"*21)

        print()

        print("(1) Cadastrar Usuário")
        print("(2) Fazer Login")
        print("(0) Sair")

        print()

        x = input(": ")

        print()
        print()

        if x == "1":

            cadastrar_usuario()

        elif x == "2":

            nome = fazer_login()

            if nome != "":

                menu_logado(nome)

        elif x == "0":

            print()
            print("Volte logo :( ")

            break

        else:

            print()
            print("Opção inválida!")


feitv()