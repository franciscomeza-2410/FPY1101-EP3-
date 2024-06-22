libros_disp = [""]
usuarios = []

def registrar_libro():
     print("Registrar el Libro:")
     nombre = input("Ingrese El Nombre del Libro:")
     autor = input("iIngrese el Nombre Del Autor:")
     ano_publicacion = int(input("Ingrese el ano del Publicacion:"))
     sku = input("Ingrese el SKU:")
     libro = {"nombre", nombre, "autor", autor , "ano_publicacion", ano_publicacion, "sku", sku}
     

     while libro not in libros_disp:
        print("Libro no valido, ingrese uno: ","","".join(libros_disp) )
        Libro = input("Ingrese Un Libro:")
        libro = {
           "Nombre": nombre,
           "autor": autor,
           "ano_publicacion": ano_publicacion,
           "sku": sku
        }
        return libro

def prestar_libro(): 
   print("Lista de Libros:")
   for libro in libros_disp:
       print()