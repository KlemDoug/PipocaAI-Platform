'''
Menu Interativo do Chatbot
Pipoca.AI
'''

def exibir_menu_chatbot(nickname):
    '''
    Exibe menu principal do chatbot.
    Argumentos:
        nickname (str): Nome escolhido pelo usuário (Já validado).
    Retorna:
        int: Opção entre 0 e 9.
    Retorna: -1 em caso de erro.
    '''

    print("\n" + "=" * 55)
    print(f"🤖 Olá 👋, @{nickname}! Como posso lhe ajudar hoje?")
    print("\n🍿 Bem-vindo ao menu de opções 🍿:")
    print("=" * 55)

    print("[1] Filmes")
    print("[2] Séries")
    print("[3] Recomendações")
    print("[4] Lançamentos")
    print("[5] Favoritos")
    print("[6] Buscar Título")
    print("[7] Notícias")
    print("[8] Avaliações")
    print("[9] Configurações")
    print("[0] Sair")

    try:
        opcao = int(input("Escolha uma opção: "))

        if 0 <= opcao:
            return opcao
        else:
            print("Opção não encontrada, tente novamente.")
            return -1   
    
    except ValueError:
        print("Digite apenas números.")
        return -1