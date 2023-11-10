from Evento import Evento

class EventoReunion(Evento):
    def __init__(self, nombre_evento, fecha, cantidad):
        super().__init__(nombre_evento, fecha)
        self.cant_invitados = cantidad

    def get_cant_invitados(self):
        return self.cant_invitados

    def set_cant_invitados(self, cant_invitados):
        self.cant_invitados = cant_invitados

    def __str__(self):
        return f"EventoT1: {self.nombre_evento}, Fecha: {self.fecha}, Atributo Adicional: {self.cant_invitados}"


class SingletonEventoReunion:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SingletonEventoReunion, cls).__new__(cls)
            cls._instance.evento_t1 = EventoReunion("", "", "")  
        return cls._instance