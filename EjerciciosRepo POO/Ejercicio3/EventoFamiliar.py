from Evento import Evento

class EventoFamiliar(Evento):
    def __init__(self, nombre_evento, fecha, cantidad_invitados):
        super().__init__(nombre_evento, fecha)
        self.cantidad = cantidad_invitados

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad_invitados):
        self.cantidad = cantidad_invitados

    def __str__(self):
        return f"Evento Familiar: {self.nombre_evento}, Fecha: {self.fecha}, Atributo Adicional: {self.cantidad}"


class SingletonEventoFamiliar:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SingletonEventoFamiliar, cls).__new__(cls)
            cls._instance.evento_t1 = EventoFamiliar("", "", "") 
        return cls._instance