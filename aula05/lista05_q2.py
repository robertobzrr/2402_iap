# Função de processamento do programa
def funcao_processamento():



    qtd_ferro = float(input("Digite a quantidade de ferro: "))
    qtd_ouro = float(input("Digite a quantidade de ouro: "))

    total_liga = qtd_ferro + qtd_ouro
    
    if (qtd_ferro/total_liga) >= 0.7:
        print("A sua armadura será massa!!")
    else:
        print("Sua armadura vai quebrar!!")



if __name__ == "__main__":
    
    # Mensagem de inicio do programa
    print("--- --- Iniciando o programa --- ---")

    # Processamento realizado pelo programa
    funcao_processamento()

    # Mensagem de fim de programa
    print("--- --- Fim do Programa --- ---")
