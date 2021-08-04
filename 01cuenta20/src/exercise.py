#escribe tu código abajo de esta línea
def cuenta20():
    i = 0
    positive, negative, zeros = 0, 0, 0
    while (i < 20):
        num = float(input("Dame un numero "))
        if num == 0:
            zeros += 1
        elif num > 0:
            positive += 1
        else:
            negative += 1

        i += 1
    print("Positivos: ", positive)
    print("Negativos: ", negative)
    print("Ceros: ", zeros)

def main():
    cuenta20()


if __name__ == '__main__':
    main()
