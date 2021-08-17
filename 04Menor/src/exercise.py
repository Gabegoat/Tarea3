#escribe tu código abajo de esta línea
def menor(numDatos):
    small = input("Dame un número ")
    while numDatos != 1:
        num = input("Dame un número ")
        if num < small:
            small = num
        else:
            small = small
        numDatos -= 1
    return small


def main():
    #No borrar nada del main
    numDatos = int(input("Dame el número de datos a recibir"))
    print(menor(numDatos))

if __name__ == '__main__':
    main()
