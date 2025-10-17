# Calcula a média de três notas fornecidas pelo usuário

def solicitar_nota(numero):
    while True:
        try:
            nota = float(input(f"Digite a nota {numero}: "))
            if 0 <= nota <= 10:
                return nota
            else:
                print("A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

nota1 = solicitar_nota(1)
nota2 = solicitar_nota(2)
nota3 = solicitar_nota(3)

media = (nota1 + nota2 + nota3) / 3
print(f"A média das notas é: {media:.2f}")

