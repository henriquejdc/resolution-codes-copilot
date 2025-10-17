# Verifica se uma palavra é um palíndromo

palavra = input("Digite uma palavra para verificar se é um palíndromo: ")

# Remove espaços e converte para minúsculas
palavra_formatada = palavra.replace(" ", "").lower()

# Inverte a palavra
palavra_invertida = palavra_formatada[::-1]

if palavra_formatada == palavra_invertida:
    print(f'"{palavra}" é um palíndromo!')
else:
    print(f'"{palavra}" não é um palíndromo.')

