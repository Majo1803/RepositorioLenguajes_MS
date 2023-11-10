class Socio:
    def __init__(self, numero_socio, nombre, direccion):
        self.numero_socio = numero_socio
        self.nombre = nombre
        self.direccion = direccion
        self.libros_prestados = []

    def prestar_libro(self, libro, fecha_prestamo):
        if libro.disponible:
            libro.disponible = False
            prestamo = Prestamo(libro, self.numero_socio, fecha_prestamo)
            self.libros_prestados.append(prestamo)
            return True
        else:
            print(f"El libro {libro.titulo} no está disponible para préstamo.")
            return False

    def devolver_libro(self, libro, fecha_devolucion):
        for prestamo in self.libros_prestados:
            if prestamo.libro == libro:
                prestamo.fecha_devolucion = fecha_devolucion
                libro.disponible = True
                self.libros_prestados.remove(prestamo)
                print(f"El libro {libro.titulo} ha sido devuelto.")
                return True
        print(f"El libro {libro.titulo} no está en préstamo por este socio.")
        return False

class Libro:
    def __init__(self, codigo, titulo, autor, disponible=True):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.disponible = disponible

class Prestamo:
    def __init__(self, libro, numero_socio, fecha_prestamo):
        self.libro = libro
        self.numero_socio = numero_socio
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = None

class Biblioteca:
    def __init__(self):
        self.socios = []
        self.libros = []

    def agregar_socio(self, socio):
        self.socios.append(socio)

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def mostrar_estado_libros(self):
        for libro in self.libros:
            estado = "Disponible" if libro.disponible else "No disponible"
            print(f"Código: {libro.codigo}, Título: {libro.titulo}, Autor: {libro.autor}, Estado: {estado}")

    def socios_con_mas_de_3_libros_prestados(self):
        return list(filter(lambda socio: len(socio.libros_prestados) > 3, self.socios))


# Ejemplo de uso
biblioteca = Biblioteca()

socio1 = Socio(1, "Juan", "Calle A")
socio2 = Socio(2, "Maria", "Calle B")
socio3 = Socio(3, "Pedro", "Calle C")
socio4 = Socio(4, "Ana", "Calle D")
socio5 = Socio(5, "Lucas", "Calle E")
libro1 = Libro(101, "Pantalones Cortos", "Lara Rios")
libro2 = Libro(102, "Pantalones Largos", "Lara Rios")
libro3 = Libro(103, "Verano de Colores", "Lara Rios")
libro4 = Libro(104, "Cuentos de mi tía Panchita", "Carmen Lyra")
libro5 = Libro(105, "Paco y Lola", "Emma Gamboa")


biblioteca.agregar_socio(socio1)
biblioteca.agregar_socio(socio2)
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

socio1.prestar_libro(libro1, "2023-11-09")
socio1.prestar_libro(libro2, "2023-11-10")
socio1.prestar_libro(libro5, "2023-11-11")

biblioteca.mostrar_estado_libros()

socio1.devolver_libro(libro1, "2023-11-15")
socio2.devolver_libro(libro3, "2023-11-16")

print("Socios con más de 3 libros prestados:")
socios_con_mas_de_3 = biblioteca.socios_con_mas_de_3_libros_prestados()
for socio in socios_con_mas_de_3:
    print(f"Número de socio: {socio.numero_socio}, Nombre: {socio.nombre}, Libros prestados: {len(socio.libros_prestados)}")
