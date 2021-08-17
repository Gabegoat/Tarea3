#escribe tu código abajo de esta línea
def teatro():
    precio = 200
    perdida = 0
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
        perdida = perdida + (precio*porcentaje/100)
        print("Descuento de "+str(porcentaje)+"%")
        edad = int(input("Dame la edad "))
    print("Cantidad total por descuentos: "+str(perdida))


def main():
    teatro()

if __name__ == '__main__':
    main()
