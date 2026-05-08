

def somar(a, b):
    return (a + b)

def subtrair(a, b):
    return (a - b)

def multiplicar(a, b):
    return (a * b)

def dividir(a, b):
    if b == 0:
        return ("Erro: Não é possível dividir por zero")
    return (a / b)

def potencia(a, b):
    return (a ** b)

def raiz_quadrada(a, b):
    if a < 0:
        return ("Erro: o índice da raiz não pode ser negativo")
    return (a ** 0.5)
