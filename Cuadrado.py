class Cuadrado:
    def __init__(self, dimension):
        self.dimension = dimension

    def dibujar(self):
        # Dibuja la primera fila
        self.dibujar_fila_completa()

        # Dibuja las filas intermedias
        for j in range(self.dimension - 2):
            self.dibujar_fila_intermedia()

        # Dibuja la última fila
        self.dibujar_fila_completa()

    def dibujar_fila_completa(self):
        print("* " * (self.dimension + 1))

    def dibujar_fila_intermedia(self):
        print("* " + "  " * (self.dimension - 2) + "  *")


# Uso de la clase
def main():
    N = int(input("Escribe la dimensión N>=2 del cuadrado a dibujar: "))
    if N >= 2:
        cuadrado = Cuadrado(N)
        cuadrado.dibujar()
    else:
        print("La dimensión debe ser mayor o igual a 2.")


if __name__ == "__main__":
    main()
