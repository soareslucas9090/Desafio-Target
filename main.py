def q1_fibonacci(n: int) -> bool:
    fib = [0, 1]

    aux = 0

    while aux < n:
        aux = fib[-1] + fib[-2]
        fib.append(aux)

    return n in fib


def q2_string_search_a(str: str) -> int:
    a = ["a", "A"]
    repsA = 0

    for c in str:
        if c in a:
            repsA += 1

    return repsA


def q3_pseudocodigo() -> int:
    indice = 12
    soma = 0
    k = 1

    while k < indice:
        k += 1
        soma = soma + k

    return soma


###### q1 ######
print("Executando o código da função 1...\n")
n = input("Digite o número que você deseja verificar se está em fibonacci: ")

if q1_fibonacci(int(n)):
    print(f"\nO número {n} está em fibonacci\n")
else:
    print(f"\nO número {n} não está em fibonacci\n")

###### q2 ######

print("Executando o código da função 2...\n")
str = input("Digite a string que quer passar para a função: ")

repsA = q2_string_search_a(str)
print(f"\nA string passada: {str} contém {repsA} 'a's ou 'A's\n")

###### q3 ######

print("Executando o código da função 3...\n")

print(f"A soma dada no pseudo código é {q3_pseudocodigo()}")
