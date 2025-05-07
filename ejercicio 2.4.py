import math

# Clase Círculo
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio

# Clase Rectángulo
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

# Clase Cuadrado 
class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)

# Clase Triángulo
class TrianguloRectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2

    def perimetro(self):
        return self.base + self.altura + self.hipotenusa()

    def hipotenusa(self):
        return math.sqrt(self.base ** 2 + self.altura ** 2)

    def tipo_triangulo(self):
        hipotenusa = self.hipotenusa()
        if self.base == self.altura == hipotenusa:
            return "Es un triangulo Equilátero"
        elif self.base == self.altura or self.base == hipotenusa or self.altura == hipotenusa:
            return "Es un triangulo Isósceles"
        else:
            return "Es un triangulo Escaleno"

# Clase de prueba
def main():
    # Crear un círculo
    circulo = Circulo(2)
    print("Círculo:")
    print(f"Área: {circulo.area():.2f}")
    print(f"Perímetro: {circulo.perimetro():.2f}\n")

    # Crear un rectángulo
    rectangulo = Rectangulo(1, 2)
    print("Rectángulo:")
    print(f"Área: {rectangulo.area():.2f}")
    print(f"Perímetro: {rectangulo.perimetro():.2f}\n")

    # Crear un cuadrado
    cuadrado = Cuadrado(3)
    print("Cuadrado:")
    print(f"Área: {cuadrado.area():.2f}")
    print(f"Perímetro: {cuadrado.perimetro():.2f}\n")

    # Crear un triángulo rectángulo
    triangulo = TrianguloRectangulo(3, 5)
    print("Triángulo Rectángulo:")
    print(f"Área: {triangulo.area():.2f}")
    print(f"Perímetro: {triangulo.perimetro():.2f}")
    print(f"Hipotenusa: {triangulo.hipotenusa():.2f}")
    print(f"Tipo de triángulo: {triangulo.tipo_triangulo()}")

if __name__ == "__main__":
    main()