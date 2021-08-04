#escribe tu código abajo de esta línea
def menor(numDatos):

    small = numDatos.pop(0)

    while len(numDatos) != 0:
        num = numDatos.pop(0)
        if num < small:
            small = num
        else:
            small = small
    return small


def main():

    userData = input()
    numDatos = list(userData.split(" "))
    print(menor(numDatos))




if __name__ == '__main__':
    main()
