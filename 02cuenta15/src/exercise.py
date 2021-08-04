#escribe tu código abajo de esta línea
def cuenta15():
    i, j = 0, 0
    negatives = []
    while (i < 15):
        num = float(input("Dame un numero negativo "))
        negatives.append(num)
        i += 1
    while (j < 15):
        print(negatives.pop(0)*-1)
        #print(abs(negatives.pop())) #Valor absoluto -> para evitar errores en caso de que el usuario de un numero positivo
        j += 1

def main():
    cuenta15()


if __name__ == '__main__':
    main()
