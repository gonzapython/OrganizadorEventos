class usuarios():
    def __init__(self, nombre, contraseña)

class comunidades():
    def __init__(self, nombre, direccion, fecha_creacion, creador, organizador)

class eventos():
    def __init__(self, nombre, descripcion, fecha, comunidad)

class miembros_comunidad():
    def __init__(self, nombre, comunidad)

class asistentes_eventos(usuarios, eventos):
    def __init__(self, sistente, comunidad)



