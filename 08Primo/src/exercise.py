#escribe tu código abajo de esta línea
def primo(num):
    isPrime = False
    n = num
    divisores = 0
    while n > 0:
        if num % n == 0:
            divisores += 1
        n -= 1
    if divisores == 2:
        isPrime = True
    return isPrime

def main():
    numero = int(input())
    print(primo(numero))

if __name__ == '__main__':
    main()
