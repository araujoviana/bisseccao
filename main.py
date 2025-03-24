# Matheus Gabriel Viana Araujo - 10420444
# Guilherme Araújo Castro - 10427775
# Diogo Fassina Garcia - 10417030

import math

def bisseccao(f, a: float, b: float, epsilon: float, max_iteracoes: int) -> float:
    while abs(f((b + a) / 2)) > epsilon or max_iteracoes > 0:
        meio = (b + a) / 2
        if f(meio) == 0: return meio
        if f(meio) * f(a) > 0:
            a = meio
        else:
            b = meio

        max_iteracoes -= 1

    return (a + b) / 2


def main():

    # Exercício 2

    print(f"A raiz de x^3 + 4x^2 - 10 é: {bisseccao(lambda x: x**3 + 4*x**2 - 10, 1, 2, 0.1, 1000)}")

    # Exercício 3

    print("\nExercício 3:", end="\n\n")

    epsilon: float = 0.001
    max_iteracoes = 1000

    # A
    print("A:")
    print(f"A raiz de x - 2^(-x) é: {bisseccao(lambda x: x - 2**(-x), 0, 1, epsilon, max_iteracoes)}")

    # B
    print("B:")
    print(f"A raiz de e^x - x^2 + 3x - 2 é: {bisseccao(lambda x: math.e**x - x**2 + 3*x - 2, 0, 1, epsilon, max_iteracoes)}")

    # C1
    print("C1:")
    print(f"A primeira raiz de 2x * cos(2x) - (x+1)^2 é: {bisseccao(lambda x: 2*x*math.cos(2*x)-(x+1)**2, -3, -2, epsilon, max_iteracoes)}")
    # C2
    print("C2:")
    print(f"A segunda raiz de 2x * cos(2x) - (x+1)^2 é: {bisseccao(lambda x: 2*x*math.cos(2*x)-(x+1)**2, -1, 0, epsilon, max_iteracoes)}")

    # D1
    print("D1:")
    print(f"A primeira raiz de x cos x - 2x^2 + 3x - 1 é: {bisseccao(lambda x: x*math.cos(x)-(2*x**2)+3*x-1, 0.2, 0.3, epsilon, max_iteracoes)}")
    # D2
    print("D2:")
    print(f"A segunda raiz de x cos x - 2x^2 + 3x - 1 é: {bisseccao(lambda x: x*math.cos(x)-(2*x**2)+3*x-1, 1.2, 1.3, epsilon, max_iteracoes)}")

if __name__ == "__main__":
    main()
