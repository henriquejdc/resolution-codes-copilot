# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

def solicitar_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Entrada inválida. Digite um número.")

num1 = solicitar_numero("Digite o primeiro número: ")
num2 = solicitar_numero("Digite o segundo número: ")

print("Escolha a operação:")
print("+ para adição")
print("- para subtração")
print("* para multiplicação")
print("/ para divisão")
operacao = input("Operação: ")

resultado = None
if operacao == '+':
    resultado = num1 + num2
elif operacao == '-':
    resultado = num1 - num2
elif operacao == '*':
    resultado = num1 * num2
elif operacao == '/':
    if num2 == 0:
        print("Erro: divisão por zero.")
    else:
        resultado = num1 / num2
else:
    print("Operação inválida.")

if resultado is not None:
    print(f"Resultado: {resultado}")