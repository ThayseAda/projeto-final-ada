from pet import Pet
import csv

class PetRepository:
    def __init__(self, arquivo_csv):
        self.arquivo_csv = arquivo_csv

    def inserir(self, pet):
        with open(self.arquivo_csv, 'a', newline='') as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow([pet.nome, pet.idade, pet.peso])

    def listar_pets(self):
        pets = []
        with open(self.arquivo_csv, 'r') as arquivo:
            leitor = csv.reader(arquivo)
            for linha in leitor:
                nome, idade, peso = linha
                pets.append(Pet(nome, idade, peso))
        return pets