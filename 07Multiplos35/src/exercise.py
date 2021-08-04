#escribe tu código abajo de esta línea
def multipli3o5():
    suma = 0
    n = 0
    while n < 1000:
        if n % 3 == 0:
            suma += n
        elif n % 5 == 0:
            suma += n
        n += 1
    return suma

def main():

    print(multipli3o5())





if __name__ == '__main__':
    main()
