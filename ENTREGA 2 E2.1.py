import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio


class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)


class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

    def calcular_perimetro(self):
        return 4 * self.lado


class Triangulo_Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

    def calcular_hipotenusa(self):
        return math.sqrt(self.base ** 2 + self.altura ** 2)

    def calcular_perimetro(self):
        return self.base + self.altura + self.calcular_hipotenusa()

    def determinar_tipo_triangulo(self):
        hipotenusa = self.calcular_hipotenusa()
        if self.base == self.altura == hipotenusa:
            print("Es un triángulo equilátero")
        elif self.base != self.altura and self.base != hipotenusa and self.altura != hipotenusa:
            print("Es un triángulo escaleno")
        else:
            print("Es un triángulo isósceles")


def main():
    figura_1 = Circulo(2)
    figura_2 = Rectangulo(1, 2)
    figura_3 = Cuadrado(3)
    figura_4 = Triangulo_Rectangulo(3, 5)

    print("El área del círculo es =", figura_1.calcular_area())
    print("El perímetro del círculo es =", figura_1.calcular_perimetro())
    print()
    print("El área del rectángulo es =", figura_2.calcular_area())
    print("El perímetro del rectángulo es =", figura_2.calcular_perimetro())
    print()
    print("El área del cuadrado es =", figura_3.calcular_area())
    print("El perímetro del cuadrado es =", figura_3.calcular_perimetro())
    print()
    print("El área del triángulo es =", figura_4.calcular_area())
    print("El perímetro del triángulo es =", figura_4.calcular_perimetro())
    figura_4.determinar_tipo_triangulo()


if __name__ == "__main__":
    main()
