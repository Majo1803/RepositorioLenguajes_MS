class Documento:
    def __init__(self):
        self.hojas = []

    def agregar_hoja(self, hoja):
        self.hojas.append(hoja)

class Hoja:
    def __init__(self):
        self.objetos = []

    def agregar_objeto(self, obj):
        self.objetos.append(obj)

class Grupo:
    def __init__(self):
        self._objetos = []

    def agregar_objeto(self, obj):
        self._objetos.append(obj)

    @property
    def objetos(self):
        return self._objetos

class Rectangulo:
    def __init__(self, x, y, ancho, alto):
        self._x = x
        self._y = y
        self._ancho = ancho
        self._alto = alto

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def ancho(self):
        return self._ancho

    @property
    def alto(self):
        return self._alto

class Circulo:
    def __init__(self, x, y, radio):
        self._x = x
        self._y = y
        self._radio = radio

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def radio(self):
        return self._radio

# Ejemplo de uso del editor gráfico de documentos
if __name__ == "__main__":
    documento = Documento()

    hoja1 = Hoja()
    documento.agregar_hoja(hoja1)

    rectangulo1 = Rectangulo(10, 20, 30, 40)
    hoja1.agregar_objeto(rectangulo1)

    hoja2 = Hoja()
    documento.agregar_hoja(hoja2)

    circulo1 = Circulo(50, 60, 70)
    hoja2.agregar_objeto(circulo1)

    grupo1 = Grupo()
    grupo1.agregar_objeto(rectangulo1)
    grupo1.agregar_objeto(circulo1)

    hoja2.agregar_objeto(grupo1)

    for hoja in documento.hojas:
        for obj in hoja.objetos:
            if isinstance(obj, Grupo):
                print("Grupo:")
                for grupo_obj in obj.objetos:
                    if isinstance(grupo_obj, Rectangulo):
                        print(f"  Rectángulo: x={grupo_obj.x}, y={grupo_obj.y}, ancho={grupo_obj.ancho}, alto={grupo_obj.alto}")
                    elif isinstance(grupo_obj, Circulo):
                        print(f"  Círculo: x={grupo_obj.x}, y={grupo_obj.y}, radio={grupo_obj.radio}")
            elif isinstance(obj, Rectangulo):
                print(f"Rectángulo: x={obj.x}, y={obj.y}, ancho={obj.ancho}, alto={obj.alto}")
            elif isinstance(obj, Circulo):
                print(f"Círculo: x={obj.x}, y={obj.y}, radio={obj.radio}")
