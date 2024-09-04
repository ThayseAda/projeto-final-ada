class PetService:
    def coletar_nome(self):
        nome = input("Nome do pet: ")
        return nome

    def coletar_idade(self):
        while True:
            try:
                idade = int(input("Idade do pet (em anos): "))
                if idade < 0:
                    print("A idade não pode ser negativa. Tente novamente.")
                else:
                    break
            except ValueError:
                print("Por favor, insira um número válido para a idade.")
        return idade
    
    def coletar_peso(self):
        while True:
            try:
                peso = float(input("Peso do pet (em kg): "))
                if peso < 0:
                    print("O peso não pode ser negativo. Tente novamente.")
                else:
                    break
            except ValueError:
                print("Por favor, insira um número válido para o peso.")
        return peso