from Ejercicio3.Contacto import Contacto

class ContactoFamiliar(Contacto):
    def __init__(self, nombre, apellido, parentesco):
        super().__init__(nombre, apellido)
        self.parentesco = parentesco

    def get_parentesco(self):
        return self.parentesco

    def set_parentesco(self, parentesco):
        self.parentesco = parentesco

    def __str__(self):
        return f"Contacto Familiar: {self.nombre} {self.apellido}, Parentesco: {self.parentesco}"

# Implementación del patrón Singleton para ContactoFamiliar
class SingletonContactoFamiliar:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SingletonContactoFamiliar, cls).__new__(cls)
            cls._instance.contacto_familiar = ContactoFamiliar("", "", "")  # Puedes proporcionar valores predeterminados aquí.
        return cls._instance
