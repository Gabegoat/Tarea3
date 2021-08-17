#escribe tu código abajo de esta línea
def mayor(numDatos):
    big = input("Dame un número ")
    while numDatos != 1:
        num = input("Dame un número ")
        if num > big:
            big = num
        else:
            big = big
        numDatos -= 1
    return big


def main():
    #No borrar nada del main
    numDatos = int(input("Dame el número de datos a recibir "))
    print(mayor(numDatos))

if __name__ == '__main__':
    main()
