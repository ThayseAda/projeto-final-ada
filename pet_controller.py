from pet import Pet
from pet_repository import PetRepository

class PetController:
    def __init__(self, repository):
        self.repository = repository

    def inserir_pet(self, pet):
        self.repository.inserir(pet)

    def listar_pets(self):
        for pet in self.repository.listar_pets()[1:]:
            print(f"Nome: {pet.nome}, Idade: {pet.idade}, Peso: {pet.peso}")