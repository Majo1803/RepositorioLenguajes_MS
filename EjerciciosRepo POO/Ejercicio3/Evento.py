class Evento:
    _instance = None  

    def __new__(cls, nombre_evento, fecha):
        if cls._instance is None:
            cls._instance = super(Evento, cls).__new__(cls)
            cls._instance.nombre_evento = nombre_evento
            cls._instance.fecha = fecha
        return cls._instance

    def get_nombre_evento(self):
        return self.nombre_evento

    def set_nombre_evento(self, nombre_evento):
        self.nombre_evento = nombre_evento

    def get_fecha(self):
        return self.fecha

    def set_fecha(self, fecha):
        self.fecha = fecha

    def __str__(self):
        return f"Evento: {self.nombre_evento}, Fecha: {self.fecha}"



