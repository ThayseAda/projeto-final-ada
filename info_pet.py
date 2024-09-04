def coletar_informacoes_pet():
    print("Por favor, insira as informações sobre seu pet.")

    # Coleta do nome do pet
    nome = input("Nome do pet: ")

    # Coleta da idade do pet, garantindo que seja um número inteiro
    while True:
        try:
            idade = int(input("Idade do pet (em anos): "))
            if idade < 0:
                print("A idade não pode ser negativa. Tente novamente.")
            else:
                break
        except ValueError:
            print("Por favor, insira um número válido para a idade.")

    # Coleta do peso do pet, garantindo que seja um número flutuante
    while True:
        try:
            peso = float(input("Peso do pet (em kg): "))
            if peso < 0:
                print("O peso não pode ser negativo. Tente novamente.")
            else:
                break
        except ValueError:
            print("Por favor, insira um número válido para o peso.")

    # Coleta da espécie do pet
    especie = input("Espécie do pet: ")

    # Coleta do porte do pet, com validação para pequeno, médio ou grande
    while True:
        porte = input("Porte do pet (pequeno, médio, grande): ").lower()
        if porte in ["pequeno", "médio", "medio", "grande"]:
            porte = "médio" if porte == "medio" else porte  # Corrige a entrada "medio" para "médio"
            break
        else:
            print("Por favor, insira um porte válido (pequeno, médio, grande).")

    # Exibindo as informações coletadas
    print("\nInformações do pet:")
    print(f"Nome: {nome}")
    print(f"Idade: {idade} anos")
    print(f"Peso: {peso} kg")
    print(f"Espécie: {especie}")
    print(f"Porte: {porte}")

# Chama a função para coletar e exibir as informações do pet
coletar_informacoes_pet()
