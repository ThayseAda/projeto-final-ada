def test_classificacao():
    # Testes de exemplo
    assert calcular_classificacao(4) == "Verde - Tranquilo"
    assert calcular_classificacao(10) == "Amarelo - Manter sob observação, mas sem risco de mordida"
    assert calcular_classificacao(20) == "Vermelho - Risco de morte"

def calcular_classificacao(peso):
    if peso < 5:
        return "Verde - Tranquilo"
    elif peso < 15:
        return "Amarelo - Manter sob observação, mas sem risco de mordida"
    else:
        return "Vermelho - Risco de morte"

# Executando o teste
test_classificacao()
print("Todos os testes passaram!")