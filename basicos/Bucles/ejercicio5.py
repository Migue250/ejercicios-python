productos = {"manzana": 1.5, "banana": 0.8, "leche": 2.3}

valores_numericos = {producto: precio for producto, precio in productos.items()}

sumaprecio = 0
for precio in productos.values() :
 sumaprecio += precio 
 print (sumaprecio)


