#escribe tu código abajo de esta línea
def relojDigital():
    h = 0
    m = 0
    s = 0
    full = ""
    ans = ""
    while h < 24:
        print(str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2))
        s += 1
        if s == 60:
            s = 0
            m += 1
        if m == 60:
            m = 0
            h += 1


def main():
    relojDigital()

if __name__ == '__main__':
    main()
