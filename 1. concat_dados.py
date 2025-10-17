def concat_dados(*args):
    """Concatena todos os argumentos em uma única string."""
    return ''.join(str(arg) for arg in args)

if __name__ == "__main__":
    print(concat_dados("Olá, ", "mundo!", 123))  # Exemplo de uso

# Vamos receber dois dados diferentes do usuário e concatena-los em uma única string?!