def validar_entrada_numerica(mensagem, tipo=float):
    while True:
        try:
            valor = tipo(input(mensagem))
            if valor < 0:
                print("O valor não pode ser negativo. Tente novamente.")
            else:
                return valor
        except ValueError:
            print(f"Por favor, insira um valor válido ({'número inteiro' if tipo == int else 'número decimal'}).")

def coletar_informacoes_pet():
    print("Por favor, insira as informações sobre seu pet.")

    # Coleta do nome do pet
    while True:
        nome = input("Nome do pet: ").strip()
        if nome:
            break
        else:
            print("O nome do pet não pode estar vazio. Tente novamente.")

    # Coleta da idade do pet
    idade = validar_entrada_numerica("Idade do pet (em anos): ", tipo=int)

    # Coleta do peso do pet
    peso = validar_entrada_numerica("Peso do pet (em kg): ", tipo=float)

    # Exibindo as informações coletadas
    print("\nInformações do pet:")
    print(f"Nome: {nome}")
    print(f"Idade: {idade} anos")
    print(f"Peso: {peso} kg")

# Chama a função para coletar e exibir as informações do pet
coletar_informacoes_pet()
