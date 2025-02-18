def adicionar_contato(lista_contatos, nome, telefone, email):
    try:
        if not nome or not telefone or not email:
            raise ValueError("\nPor favor, é necessário preencher todos os campos!")
        else:
            contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": False}
    except Exception as e:
        print(f"\nErro ao realizar a operação de inclusão do novo contato: {e}")
    else:
        lista_contatos.append(contato)
        print(f"\nO contato '{contato["nome"]}' foi adicionado com sucesso!")

def visualizar_contatos(lista_contatos):
    try:
        if not lista_contatos:
            raise ValueError("\nNão há contatos cadastrados!")           
        else:
            for indice, contato in enumerate(lista_contatos, start=1):
                status = "★" if contato["favorito"] else ""
                nome_contato = contato["nome"]
                telefone_contato = contato["telefone"]
                email_contato = contato["email"]
                print(f"\n{indice}. [ {status} ] - {nome_contato} ({email_contato}) -> {telefone_contato}")
    except Exception as e:
        print(f"\nErro ao realizar a operação: {e}")

def editar_contato(lista_contatos, contato_para_alteracao, nome_alterado, telefone_alterado, email_alterado, favorito):
    try:
        if not contato_para_alteracao:
            raise ValueError("\nPor favor, digite um número de acordo com a lista!") 
        else:          
            indice_arrumado = int(contato_para_alteracao) - 1
            nome = lista_contatos[indice_arrumado]["nome"] = nome_alterado if nome_alterado != "" else lista_contatos[indice_arrumado]["nome"]
            telefone = lista_contatos[indice_arrumado]["telefone"] = telefone_alterado if telefone_alterado != "" else lista_contatos[indice_arrumado]["telefone"]
            email = lista_contatos[indice_arrumado]["email"] = email_alterado if email_alterado != "" else lista_contatos[indice_arrumado]["email"]
            status = lista_contatos[indice_arrumado]["favorito"] = "★" if favorito == "S" or favorito == "s" else ""
    except Exception as e:
        print(f"\nErro ao realizar a operação de alteração do contato: {e}")
    else:
        print(f"""\nO contato foi alterado com sucesso:
            
        {indice_arrumado + 1}. [{status}] - {nome} ({email}) -> {telefone}""")
        
def visualizar_contatos_favoritos(lista_contatos):
    try:
        if not lista_contatos:
            raise ValueError("\nNão há contatos cadastrados!")           
        else:
            for indice, contato in enumerate(lista_contatos, start=1):
                if contato["favorito"] == "★":
                    nome_contato = contato["nome"]
                    telefone_contato = contato["telefone"]
                    email_contato = contato["email"]
                else:
                    raise ValueError("\nNão há contatos favoritados!")                        
    except Exception as e:
        print(f"\nErro ao realizar a operação de visualização da lista de favoritos: {e}")
    else:
        for indice, contato in enumerate(lista_contatos, start=1):
            if contato["favorito"] == "★":
                nome_contato = contato["nome"]
                telefone_contato = contato["telefone"]
                email_contato = contato["email"]
                print(f"\n{indice}. [ ★ ] - {nome_contato} ({email_contato}) -> {telefone_contato}")

def deletar_contato(lista_contatos, contato_para_delecao):
    try:
        if not contato_para_delecao:
            raise ValueError("\nPor favor, é necessário informar o contato para deleção!")
        elif not lista_contatos:
            raise ValueError("\nNão há contatos para serem deletados!")
        else:
            indice_contato_arrumado = int(contato_para_delecao) - 1
    except Exception as e:
        print(f"\nErro ao realizar a operação de inclusão do novo contato: {e}")
    else:
        lista_contatos.remove(lista_contatos[indice_contato_arrumado])
        print("O contato foi deletado com sucesso!")

lista_contatos = []

while True:
    print("\n Menu de utilização da agenda")
    print("\n1. Adicionar um novo contato")
    print("2. Visualizar todos os contatos")
    print("3. Editar um contato")
    print("4. Visualizar contatos favoritos")
    print("5. Apagar um contato")
    print("6. Sair")
    
    escolha = input("\nDigite um número de acordo com a ação desejada: ")
    
    if escolha == "1":
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        email = input("Digite o email do contato: ")
        adicionar_contato(lista_contatos, nome, telefone, email)
    if escolha == "2":
        visualizar_contatos(lista_contatos)
    if escolha == "3":
        if not lista_contatos:
            print("\nNão há contatos cadastrados para edição!")
        else:
            visualizar_contatos(lista_contatos)
            contato_para_alteracao = input("\nPor favor, digite o número do contato a ser editado: ")
            print("\nAbaixo, seguem os itens para alteração, e caso não deseje alterar, deixe o campo vazio e aperte 'enter'")
            nome = input("Novo nome: ")
            telefone = input("Novo telefone: ")
            email = input("Nome email: ")
            favorito = input("Gostaria de incluir o contato como favorito (S = Sim ou N = Nao)?: ")
            editar_contato(lista_contatos, contato_para_alteracao, nome, telefone, email, favorito)
    if escolha == "4":
        visualizar_contatos_favoritos(lista_contatos)
    if escolha == "5":
        visualizar_contatos(lista_contatos)
        contato_para_delecao = input("\nPor favor, digite o número do contato a ser deletado: ")
        deletar_contato(lista_contatos, contato_para_delecao)
    if escolha == "6":
        break