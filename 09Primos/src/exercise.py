#escribe tu código abajo de esta línea
def primos(num):
    listaprimos = []
    while num > 0:

        n = num
        divisores = 0

        while n > 0:
            if num % n == 0:
                divisores += 1
            n -= 1
        if divisores == 2:
            listaprimos.append(num)
        num -= 1
    return listaprimos[0]          #Se obtienen todos los numeros primos pero solo se regresa el mas cercano a la entrada del usuario

def main():
    numero = int(input())
    print(primos(numero))

if __name__ == '__main__':
    main()
