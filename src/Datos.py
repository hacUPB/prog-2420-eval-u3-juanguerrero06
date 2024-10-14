def main():
    peliculas = [
    {"nombre": "Película 1", "asientos": [["O" for _ in range(5)] for _ in range(5)]},
    {"nombre": "Película 2", "asientos": [["O" for _ in range(5)] for _ in range(5)]},
    {"nombre": "Película 3", "asientos": [["O" for _ in range(5)] for _ in range(5)]}
]

    reservas = []

    def mostrar_peliculas():
        print("Películas en cartelera:")
        for i, pelicula in enumerate(peliculas, 1):
            print(f"{i}. {pelicula['nombre']}")

    def mostrar_asientos(seleccion):
        pelicula = peliculas[seleccion]
        print(f"Asientos para {pelicula['nombre']} (O = Disponible, X = Reservado):")
        for fila in pelicula["asientos"]:
            print(" ".join(fila))

    def realizar_reserva():
        mostrar_peliculas()
        seleccion = int(input("Seleccione la película (por favor solo ingrese el número): ")) - 1

        if 0 <= seleccion < len(peliculas):
            mostrar_asientos(seleccion)
            fila = int(input("Seleccione la fila (1-5): ")) - 1
            asiento = int(input("Seleccione su asiento (1-5): ")) - 1
            pelicula = peliculas[seleccion]
            
            if pelicula["asientos"][fila][asiento] == "O":
                nombre = input("Introduzca su nombre: ")
                pelicula["asientos"][fila][asiento] = "X"
                reservas.append({
                    "nombre": nombre, 
                    "pelicula": pelicula["nombre"], 
                    "fila": fila + 1, 
                    "asiento": asiento + 1
                })
                print("Reserva realizada con éxito.")
            else:
                print("El asiento ya está reservado.")
        else:
            print("Selección de película no válida.")

    def menu():
        while True:
            print("\n--- Sistema de Reservas ---")
            print("1. Ver películas")
            print("2. Ver asientos")
            print("3. Realizar reserva")
            print("4. Salir")
            opcion = input("Elija una opción: ")
            if opcion == "1":
                mostrar_peliculas()
            elif opcion == "2":
                seleccion = int(input("Seleccione la película (por favor solo ingrese el número): ")) - 1
                if 0 <= seleccion < len(peliculas):
                    mostrar_asientos(seleccion)
                else:
                    print("Selección de película no válida.")
            elif opcion == "3":
                realizar_reserva()
            elif opcion == "4":
                break
            else:
                print("Opción no válida")

    if __name__ == "__main__":
        menu()
if __name__ == "__main__":
    main()
