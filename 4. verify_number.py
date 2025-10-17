# Verifica se um número inteiro é par ou ímpar

def solicitar_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

numero = solicitar_inteiro("Digite um número inteiro: ")

if numero % 2 == 0:
    print(f"{numero} é par.")
else:
    print(f"{numero} é ímpar.")
