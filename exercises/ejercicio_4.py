if __name__ == "__main__":
    def par_impar(number):
        if number % 2 == 0:
            return True
        else:
            return False

    numero = int(input("Ingrese un numero: "))

    if par_impar(numero):
        print(f"{numero} es par")
    else:
        print(f"{numero} es impar")
