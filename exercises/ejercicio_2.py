if __name__ == "__main__":
    import math


    def Circulo(R):
        A = math.pi * R ** 2
        return A
    Radio = float(input('Ingrese radio para hallar su área: '))
    A = (Circulo(Radio))
    print(f'El área del circulo con radio {Radio} es igual a: {A:.3f}')

