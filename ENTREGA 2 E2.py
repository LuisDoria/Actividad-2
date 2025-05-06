from enum import Enum

class TipoPlaneta(Enum):
    GASEOSO = "GASEOSO"
    TERRESTRE = "TERRESTRE"
    ENANO = "ENANO"

class Planeta:
    def __init__(self, nombre, cantidad_satelites, masa, volumen, diametro, distancia_sol, tipo, es_observable):
        self.nombre = nombre
        self.cantidad_satelites = cantidad_satelites
        self.masa = masa
        self.volumen = volumen
        self.diametro = diametro
        self.distancia_sol = distancia_sol
        self.tipo = tipo
        self.es_observable = es_observable

    def imprimir(self):
        print(f"Nombre del planeta = {self.nombre}")
        print(f"Cantidad de satélites = {self.cantidad_satelites}")
        print(f"Masa del planeta = %.6E" % self.masa)
        print(f"Volumen del planeta = %.6E" % self.volumen)
        print(f"Diámetro del planeta = {self.diametro}")
        print(f"Distancia al sol = {self.distancia_sol}")
        print(f"Tipo de planeta = {self.tipo.name}")
        print(f"Es observable = {str(self.es_observable).lower()}")

    def calcular_densidad(self):
        return self.masa / self.volumen

    def es_planeta_exterior(self):
        UA = 149597870  # Unidad Astronómica en km
        limite = 3.4 * UA
        return self.distancia_sol > limite

# --- Método principal ---
def main():
    p1 = Planeta(
        nombre="Tierra",
        cantidad_satelites=1,
        masa=5.9736E24,
        volumen=1.0832E12,
        diametro=12742,
        distancia_sol=150000000,
        tipo=TipoPlaneta.TERRESTRE,
        es_observable=True
    )

    p1.imprimir()
    print("Densidad del planeta = %.15E" % p1.calcular_densidad())
    print("Es planeta exterior = " + str(p1.es_planeta_exterior()).lower())
    print()

    p2 = Planeta(
        nombre="Júpiter",
        cantidad_satelites=79,
        masa=1.899E27,
        volumen=1.431E15,
        diametro=139820,
        distancia_sol=750000000,
        tipo=TipoPlaneta.GASEOSO,
        es_observable=True
    )

    p2.imprimir()
    print("Densidad del planeta = %.15E" % p2.calcular_densidad())
    print("Es planeta exterior = " + str(p2.es_planeta_exterior()).lower())

if __name__ == "__main__":
    main()


    
    