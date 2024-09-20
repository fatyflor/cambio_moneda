class ConversorMonedas:
    def __init__(self, tasa_cambio):
        self.tasa_cambio = tasa_cambio

    def pesos_a_dolares(self, cantidad_pesos):
        """Convierte pesos a dólares"""
        return cantidad_pesos / self.tasa_cambio

    def dolares_a_pesos(self, cantidad_dolares):
        """Convierte dólares a pesos"""
        return cantidad_dolares * self.tasa_cambio


def main():
    tasa_cambio = float(input("Ingrese la tasa de cambio actual (1 USD = pesos): "))
    conversor = ConversorMonedas(tasa_cambio)

    while True:
        print("\nOpciones:")
        print("1. Convertir pesos a dólares")
        print("2. Convertir dólares a pesos")
        print("3. Salir")

        opcion = input("Ingrese su opción: ")

        if opcion == "1":
            cantidad_pesos = float(input("Ingrese la cantidad de pesos a convertir: "))
            cantidad_dolares = conversor.pesos_a_dolares(cantidad_pesos)
            print(f"{cantidad_pesos} pesos son {cantidad_dolares:.2f} USD")
        elif opcion == "2":
            cantidad_dolares = float(input("Ingrese la cantidad de dólares a convertir: "))
            cantidad_pesos = conversor.dolares_a_pesos(cantidad_dolares)
            print(f"{cantidad_dolares} USD son {cantidad_pesos:.2f} pesos")
        elif opcion == "3":
            print("Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, inténtelo de nuevo.")


if __name__ == "__main__":
    main()
