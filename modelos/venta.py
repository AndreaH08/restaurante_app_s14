class Venta:
    def __init__(self, codigo, producto, cantidad, total):
        self.codigo = codigo
        self.producto = producto
        self.cantidad = cantidad
        self.total = total

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "producto": self.producto,
            "cantidad": self.cantidad,
            "total": self.total
        }

    @staticmethod
    def from_dict(datos):
        return Venta(
            datos["codigo"],
            datos["producto"],
            datos["cantidad"],
            datos["total"]
        )

    def __str__(self):
        return f"Venta {self.codigo}: {self.producto} x {self.cantidad} = ${self.total}"
    