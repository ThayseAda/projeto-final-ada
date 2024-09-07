import tkinter as tk
from tkinter import messagebox

# Função para coletar as informações do pet
def coletar_informacoes_pet():
    nome = entry_nome.get()
    
    # Validando a idade
    try:
        idade = int(entry_idade.get())
        if idade < 0:
            raise ValueError("Idade não pode ser negativa.")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira uma idade válida (número inteiro).")
        return

    # Validando o peso
    try:
        peso = float(entry_peso.get())
        if peso < 0:
            raise ValueError("Peso não pode ser negativo.")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um peso válido (número decimal).")
        return

    # Exibindo as informações coletadas
    resultado = f"Nome: {nome}\nIdade: {idade} anos\nPeso: {peso} kg"
    messagebox.showinfo("Informações do Pet", resultado)

# Criando a janela principal
janela = tk.Tk()
janela.title("Coletar Informações do Pet")

# Rótulos e campos de entrada para nome, idade e peso
label_nome = tk.Label(janela, text="Nome do pet:")
label_nome.grid(row=0, column=0, padx=10, pady=10)
entry_nome = tk.Entry(janela)
entry_nome.grid(row=0, column=1, padx=10, pady=10)

label_idade = tk.Label(janela, text="Idade do pet (em anos):")
label_idade.grid(row=1, column=0, padx=10, pady=10)
entry_idade = tk.Entry(janela)
entry_idade.grid(row=1, column=1, padx=10, pady=10)

label_peso = tk.Label(janela, text="Peso do pet (em kg):")
label_peso.grid(row=2, column=0, padx=10, pady=10)
entry_peso = tk.Entry(janela)
entry_peso.grid(row=2, column=1, padx=10, pady=10)

# Botão para coletar as informações
botao_coletar = tk.Button(janela, text="Coletar Informações", command=coletar_informacoes_pet)
botao_coletar.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Executando o loop da janela
janela.mainloop()
