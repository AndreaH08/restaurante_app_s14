import json
import os
from modelos.venta import Venta

class VentaServicio:
    def __init__(self):
        self.archivo = 'datos/ventas.json'

    def guardar(self, venta):
        ventas = self.listar()
        ventas.append(venta.to_dict())
        os.makedirs('datos', exist_ok=True)
        with open(self.archivo, 'w', encoding='utf-8') as archivo:
            json.dump(ventas, archivo, indent=4)

    def listar(self):
        if not os.path.exists(self.archivo):
            return []
        with open(self.archivo, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
