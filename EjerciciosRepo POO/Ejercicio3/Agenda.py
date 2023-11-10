import Contacto
import Evento

class Agenda:
    def __init__(self):
        self.contactos = []
        self.eventos = []

    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)

    def eliminar_contacto(self, contacto):
        if contacto in self.contactos:
            self.contactos.remove(contacto)

    def agregar_evento(self, evento):
        self.eventos.append(evento)

    def eliminar_evento(self, evento):
        if evento in self.eventos:
            self.eventos.remove(evento)

    def __str__(self):
        contacto_str = "\n".join(str(contacto) for contacto in self.contactos)
        evento_str = "\n".join(str(evento) for evento in self.eventos)
        return f"Agenda de Contactos:\n{contacto_str}\nAgenda de Eventos:\n{evento_str}"

# Implementación de Singleton
class SingletonAgenda:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SingletonAgenda, cls).__new__(cls)
            cls._instance.agenda = Agenda()
        return cls._instance

# Implementación del patrón Abstract Factory
class FactoryAgenda:
    def crear_contacto(self, nombre, apellido):
        return Contacto(nombre, apellido)

    def crear_evento(self, nombre_evento, fecha):
        return Evento(nombre_evento, fecha)


