from Ejercicio3.Contacto import Contacto

class ContactoEmpresa(Contacto):
    def __init__(self, nombre, apellido, puesto):
        super().__init__(nombre, apellido)
        self.puesto = puesto

    def get_puesto(self):
        return self.puesto

    def set_puesto(self, puesto):
        self.puesto = puesto

    def __str__(self):

        return f"Contacto Empresarial: {self.nombre} {self.apellido}, Puesto de Trabajo: {self.puesto}"
