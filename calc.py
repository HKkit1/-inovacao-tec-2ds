# Programa para calcular a média de 4 números

# Passo 1: Inicializar uma lista vazia para armazenar os números
numeros = []

# Passo 2: Solicitar os 4 números via input
print("Por favor, digite 4 números:")
for i in range(4):
    # Solicitar cada número individualmente
    # O f-string ajuda a personalizar a mensagem para cada número
    numero = input(f"Digite o {i+1}º número: ")
    
    # Passo 3: Converter os valores para float e adicionar à lista
    try:
        numero_float = float(numero)
        numeros.append(numero_float)
    except ValueError:
        print("Erro: Por favor, digite um número válido.")
        # Se houver erro, pedir o número novamente
        numero = input(f"Digite o {i+1}º número novamente: ")
        numero_float = float(numero)
        numeros.append(numero_float)

# Passo 4: Calcular a média
# A média é a soma de todos os números dividida pela quantidade de números
soma = sum(numeros)
quantidade = len(numeros)
media = soma / quantidade

# Passo 5: Exibir o resultado com duas casas decimais
# O :.2f formata o número para mostrar apenas 2 casas decimais
print(f"\nA média dos números {numeros} é: {media:.2f}")
