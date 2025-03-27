import sys
import math

def calcular_factorial(n):
    return math.factorial(n)

def main():
    if len(sys.argv) > 1:
        entrada = sys.argv[1]
    else:
        entrada = input("Ingrese un número o un rango (ejemplo: 5, 4-8, -10, 6-): ")

    if '-' in entrada:
        partes = entrada.split('-')
        if entrada.startswith('-'):
            min_num = 1
            max_num = int(partes[1])
        elif entrada.endswith('-'):
            min_num = int(partes[0])
            max_num = 60
        else:
            min_num, max_num = map(int, partes)

        for i in range(min_num, max_num + 1):
            print(f"{i}! = {calcular_factorial(i)}")

    else:
        num = int(entrada)
        print(f"{num}! = {calcular_factorial(num)}")

if __name__ == "__main__":
    main()


