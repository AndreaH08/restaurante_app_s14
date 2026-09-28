class Producto:
    def __init__(self, codigo, nombre, categoria, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio
        }

    @staticmethod
    def from_dict(datos):
        return Producto(
            datos["codigo"],
            datos["nombre"],
            datos["categoria"],
            datos["precio"]
        )

    def __str__(self):
        return f"{self.codigo} - {self.nombre} - ${self.precio}"
    