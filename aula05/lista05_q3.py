# Função de processamento do programa
def funcao_processamento():

    print("Diga qual seu tipo de animal favorito: ")
    print("1 - Mamífero \n2 - Réptil")

    opcao = int(input("Qual sua escolha: "))

    if opcao == 1:
        print("Seu animal favorito é um cachorro")
    else:
        print("Seu animal fvorito é uma tartaruga")

    



if __name__ == "__main__":
        
    # Mensagem de inicio do programa
    print("--- --- Iniciando o programa --- ---")

    # Processamento realizado pelo programa
    funcao_processamento()

    # Mensagem de fim de programa
    print("--- --- Fim do Programa --- ---")