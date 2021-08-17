#escribe tu código abajo de esta línea
def tablaMultiplicar(num):
    multi = -1
    while (multi < 10):
        multi += 1
        producto = multi * num
        print(num, "x", multi, "=", producto)


def main():
    #No borrar nada del main
    num1 = int(input("Dime el multiplicando "))
    tablaMultiplicar(num1)

if __name__ == '__main__':
    main()
