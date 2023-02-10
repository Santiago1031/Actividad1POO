if __name__ == "__main__":
    import random

    def numeros_aleatorios(n):
        numbers = []
        for i in range(n):
            numbers.append(random.randint(1, 50))
        return numbers

    numbers = numeros_aleatorios(10)
    print(numbers)
