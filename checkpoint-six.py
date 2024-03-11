
class Usuario:
    def __init__(self, nombre, password):
        self.nombre = nombre
        self.password = password


objetoUsuario = Usuario("Josu", "pass")
print(objetoUsuario)
print(objetoUsuario.nombre)
print(objetoUsuario.password)
