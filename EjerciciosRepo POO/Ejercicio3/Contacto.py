class Contacto:
    _instance = None  

    def __new__(cls, nombre, apellido, telefono):
        if cls._instance is None:
            cls._instance = super(Contacto, cls).__new__(cls)
            cls._instance.nombre = nombre
            cls._instance.apellido = apellido
            cls._instance.telefono = telefono
        return cls._instance

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_apellido(self):
        return self.apellido

    def set_apellido(self, apellido):
        self.apellido = apellido

    def get_telefono(self):
        return self.telefono

    def set_telefono(self, telefono):
        self.telefono = telefono

    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Telefono: {self.telefono}"
