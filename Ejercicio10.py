import datetime
class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

    def UnirseSala(self, salachat):
        self.salachat = salachat
        salachat.AgregarUsuario(self)

    def EnviarMensaje(self, contenido):
        mensaje = Mensaje(contenido, self)
        self.salachat.EnviarMensaje(mensaje)

    def RecibirMensaje(self, mensaje):
            print(f"[{datetime.datetime.now().time().strftime('%H:%M:%S')}] : {mensaje.emisor.nombre}: {mensaje.contenido}")


class Mensaje:
    def __init__(self, contenido, emisor):
        self.contenido = contenido
        self.emisor = emisor

class SalaChat:
    def __init__(self):
        self.usuarios =set()

    def AgregarUsuario(self, usuario):
            self.usuarios.add(usuario)

    def EnviarMensaje(self, mensaje):
        for usuario in self.usuarios:
            if usuario == mensaje.emisor:
                usuario.RecibirMensaje(mensaje)

usuario1 = Usuario("Sebastian")
usuario2 = Usuario("Nicolas")
usuario3 = Usuario("Valentina")
usuario4 = Usuario("Mateo")

sala = SalaChat()

usuario1.UnirseSala(sala)
usuario2.UnirseSala(sala)
usuario3.UnirseSala(sala)
usuario4.UnirseSala(sala)

usuario1.EnviarMensaje("Hola gente como van")
usuario2.EnviarMensaje("Hola Sebastian")
usuario3.EnviarMensaje("Hola estrellitas")
usuario4.EnviarMensaje("Hola chicos")