#escribe tu código abajo de esta línea
def sumaFibonacci():
    fibonacci = [1,2]
    n = 0
    suma = 0
    nextFibo = 0
    while nextFibo < 4000001:
        nextFibo = fibonacci[n]+fibonacci[n+1]
        fibonacci.append(nextFibo)
        if nextFibo%2 == 0:
            suma += nextFibo
        n += 1
    return suma



def main():
    sumaFibonacci()


if __name__ == '__main__':
    main()
