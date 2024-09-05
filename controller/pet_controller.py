import sys
import os
sys.path.append(os.path.abspath('../'))

from model.pet import Pet # type: ignore
from repository.pet_repository import PetRepository # type: ignore

class PetController:
    def __init__(self, repository):
        self.repository = repository

    def inserir_pet(self, pet):
        self.repository.inserir(pet)

    def listar_pets(self):
        for pet in self.repository.listar_pets()[1:]:
            print(f"Nome: {pet.nome}, Idade: {pet.idade}, Peso: {pet.peso}")