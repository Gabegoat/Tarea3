#escribe tu código abajo de esta línea
def tablaMultiplicar(num):
    multi = -1
    while (multi < 10):
        multi += 1
        producto = multi * num
        print(num, "x", multi, "=", producto)


def main():
    num1 = int(input())
    tablaMultiplicar(num1)




if __name__ == '__main__':
    main()
