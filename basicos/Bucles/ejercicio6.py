productos = {"manzana": 1.5, "banana": 0.8, "leche": 2.3}

valores_numericos = {producto: precio for producto, precio in productos.items()}

productosmayores = []
for producto, precio in productos.items():
    if precio > 1:
        productosmayores.append(producto)

print(productosmayores)
