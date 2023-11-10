from Contacto import Contacto
from Evento import Evento
from Agenda import Agenda
from Agenda import SingletonAgenda

if __name__ == "__main__":
    # Crear instancias de contactos y eventos
    contacto1 = Contacto("Juan", "Pérez", "123-456-789")
    contacto2 = Contacto("Maria", "López", "987-654-321")
    evento1 = Evento("Reunión", "2023-11-10")
    evento2 = Evento("Concierto", "2023-12-15")

    # Crear una instancia de la agenda (Singleton)
    singleton_agenda = SingletonAgenda()

    # Agregar contactos y eventos a la agenda
    singleton_agenda.agenda.agregar_contacto(contacto1)
    singleton_agenda.agenda.agregar_contacto(contacto2)
    singleton_agenda.agenda.agregar_evento(evento1)
    singleton_agenda.agenda.agregar_evento(evento2)

    # Mostrar la agenda
    print(singleton_agenda.agenda)
