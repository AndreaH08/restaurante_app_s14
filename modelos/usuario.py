class Usuario:
    def __init__(self, usuario, clave, rol):
        self.usuario = usuario
        self.clave = clave
        self.rol = rol

    def to_dict(self):
        return {
            "usuario": self.usuario,
            "clave": self.clave,
            "rol": self.rol
        }

    @staticmethod
    def from_dict(datos):
        return Usuario(
            datos["usuario"],
            datos["clave"],
            datos["rol"]
        )

    def validar_clave(self, clave):
        return self.clave == clave

    def __str__(self):
        return f"{self.usuario} - {self.rol}"
    