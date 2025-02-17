def adicionar_contato(lista_contatos, nome, telefone, email):
    contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": False}
    lista_contatos.append(contato)
    print(f"\nO contato {contato["nome"]} foi adicionado com sucesso!")
    return

def visualizar_contatos(lista_contatos):
    for indice, contato in enumerate(lista_contatos):
        status = "★" if contato["favorito"] else "☆"
        nome_contato = contato["nome"]
        telefone_contato = contato["telefone"]
        email_contato = contato["email"]
        print(f"\n{indice}. [ {status} ] - {nome_contato} ({email_contato}) -> {telefone_contato}")
    return

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
    if escolha == "6":
        break