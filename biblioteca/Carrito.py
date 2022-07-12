from this import s

from django.shortcuts import redirect, render

from biblioteca.models import Producto
from rest_taller.models import Libro


class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito
    

    def agregar(self, producto):
        id = str(producto.sku)
        if id not in self.carrito.keys():
            self.carrito[id]={
                "producto_id": producto.sku,
                "nombre": producto.nombreLibro,
                "dias": producto.dias,
            }
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, producto):
        id = str(producto.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, producto):
        id = str(producto.id)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["acumulado"] -= producto.precio
            if self.carrito[id]["cantidad"] <= 0: self.eliminar(producto)

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True


