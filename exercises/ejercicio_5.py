if __name__ == "__main__":
    def fahrenheit_to_celsius(temperature_f):
        temperature_c = (temperature_f - 32) * 5 / 9
        return temperature_c


    temperature_f = float(input("Enter temperature in Fahrenheit: "))
    temperature_c = fahrenheit_to_celsius(temperature_f)
    print(f"Temperature in Celsius: {temperature_c}")
