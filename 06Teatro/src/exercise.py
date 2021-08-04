#escribe tu código abajo de esta línea
def teatro():
    edad = int(input("Dame la edad "))
    while edad != 0:
        if edad < 5:
            porcentaje = 0
        elif edad < 15:
            porcentaje = 35
        elif edad < 20:
            porcentaje = 25
        elif edad < 46:
            porcentaje = 10
        elif edad < 66:
            porcentaje = 25
        else:
            porcentaje = 35
        print("Descuento de ", porcentaje, "%")
        edad = int(input("Dame la edad "))
    print("Cantidad total por descuentos: X")


def main():

    teatro()




if __name__ == '__main__':
    main()
