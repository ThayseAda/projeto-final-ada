from pet import Pet
from pet_service import PetService
from pet_repository import PetRepository
from pet_controller import PetController

def coletar_informacoes_pet():
    print("\nPor favor, insira as informações sobre seu pet.\n")

    pet_service = PetService()
    pet_repository = PetRepository("pets.csv")
    pet_controller = PetController(pet_repository)

    nome = pet_service.coletar_nome()
    idade = pet_service.coletar_idade()
    peso = pet_service.coletar_peso()

    pet = Pet(nome, idade, peso)

    pet_controller.inserir_pet(pet)

    print("\n------------------------\n\nPets\n")
    pet_controller.listar_pets()
    print("\n------------------------\n")

coletar_informacoes_pet()