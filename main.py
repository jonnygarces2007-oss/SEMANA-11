from servicios.restaurante import Restaurante
from servicios.archivo_servicio import ArchivoServicio
from modelos.producto import Producto
from modelos.usuario import Usuario


# Tupla: opciones fijas del menú
OPCIONES_MENU: tuple = (
    "1. Registrar producto",
    "2. Buscar producto",
    "3. Actualizar producto",
    "4. Eliminar producto",
    "5. Listar productos",
    "6. Registrar usuario",
    "7. Listar usuarios",
    "8. Mostrar categorías",
    "9. Vender producto",
    "10. Consultar ventas de usuario",
    "11. Salir"
)


def mostrar_menu() -> None:
    print("\n========================================")
    print("        SISTEMA DE RESTAURANTE v11")
    print("========================================")
    for linea in OPCIONES_MENU:
        if linea.startswith(("5", "8", "11")):
            print("----------------------------------------")
        print(linea)
    print("========================================")


def guardar_todo(restaurante: Restaurante) -> None:
    """Guarda las 3 colecciones tras cada operación que las modifique"""
    ArchivoServicio.guardar_productos(restaurante.listar_productos())
    ArchivoServicio.guardar_usuarios(restaurante.listar_usuarios())
    ArchivoServicio.guardar_ventas(restaurante.listar_ventas())
    print("💾 Cambios guardados.")


def registrar_producto(restaurante: Restaurante) -> None:
    print("\n--- Registrar Producto ---")
    try:
        codigo = int(input("Código único: "))
        nombre = input("Nombre: ")
        categoria = input("Categoría: ")
        precio = float(input("Precio: $"))
        stock = int(input("Cantidad en stock: "))
        nuevo = Producto(codigo, nombre, categoria, precio, stock)
        if restaurante.registrar_producto(nuevo):
            print("✅ Producto registrado.")
            ArchivoServicio.guardar_productos(restaurante.listar_productos())
        else:
            print("❌ El código ya existe.")
    except ValueError as e:
        print(f"❌ Datos inválidos: {e}")


def buscar_producto(restaurante: Restaurante) -> None:
    print("\n--- Buscar Producto ---")
    try:
        codigo = int(input("Código a buscar: "))
        prod = restaurante.buscar_producto(codigo)
        print(prod if prod else "❌ No encontrado.")
    except ValueError:
        print("❌ El código debe ser un número.")


def actualizar_producto(restaurante: Restaurante) -> None:
    print("\n--- Actualizar Producto ---")
    try:
        codigo = int(input("Código del producto: "))
        nombre = input("Nuevo nombre: ")
        categoria = input("Nueva categoría: ")
        precio = float(input("Nuevo precio: $"))
        stock = int(input("Nuevo stock: "))
        if restaurante.actualizar_producto(codigo, nombre, categoria, precio, stock):
            print("✅ Actualizado.")
            ArchivoServicio.guardar_productos(restaurante.listar_productos())
        else:
            print("❌ No encontrado.")
    except ValueError:
        print("❌ Datos inválidos.")


def eliminar_producto(restaurante: Restaurante) -> None:
    print("\n--- Eliminar Producto ---")
    try:
        codigo = int(input("Código a eliminar: "))
        if restaurante.eliminar_producto(codigo):
            print("✅ Eliminado.")
            ArchivoServicio.guardar_productos(restaurante.listar_productos())
        else:
            print("❌ No encontrado.")
    except ValueError:
        print("❌ El código debe ser un número.")


def listar_productos(restaurante: Restaurante) -> None:
    print("\n--- Lista de Productos ---")
    productos = restaurante.listar_productos()
    if not productos:
        print("Sin productos registrados.")
        return
    for p in productos:
        print(p)


def registrar_usuario(restaurante: Restaurante) -> None:
    print("\n--- Registrar Usuario ---")
    try:
        ide = int(input("Identificación: "))
        nombre = input("Nombre: ")
        correo = input("Correo: ")
        usuario = Usuario(ide, nombre, correo)
        if restaurante.registrar_usuario(usuario):
            print("✅ Usuario registrado.")
            ArchivoServicio.guardar_usuarios(restaurante.listar_usuarios())
        else:
            print("❌ Esa identificación ya existe.")
    except ValueError as e:
        print(f"❌ Datos inválidos: {e}")


def listar_usuarios(restaurante: Restaurante) -> None:
    print("\n--- Lista de Usuarios ---")
    usuarios = restaurante.listar_usuarios()
    if not usuarios:
        print("Sin usuarios registrados.")
        return
    for u in usuarios:
        print(u)


def mostrar_categorias(restaurante: Restaurante) -> None:
    print("\n--- Categorías Únicas ---")
    cats = restaurante.obtener_categorias_unicas()
    if not cats:
        print("Sin categorías.")
        return
    for c in cats:
        print(f"• {c}")


def vender_producto(restaurante: Restaurante) -> None:
    print("\n--- 🛒 Realizar Venta ---")
    try:
        cod_prod = int(input("Código del producto: "))
        id_usuario = int(input("Identificación del usuario: "))
        cantidad = int(input("Cantidad a comprar: "))

        if restaurante.vender_producto(cod_prod, id_usuario, cantidad):
            print("✅ Venta realizada con éxito.")
            # Al vender se actualizan productos y se agregan ventas
            ArchivoServicio.guardar_productos(restaurante.listar_productos())
            ArchivoServicio.guardar_ventas(restaurante.listar_ventas())
        else:
            print("❌ No se pudo realizar la venta. Verifique usuario, producto y stock.")
    except ValueError:
        print("❌ Ingrese valores numéricos válidos.")


def consultar_ventas_usuario(restaurante: Restaurante) -> None:
    print("\n--- 📋 Ventas de Usuario ---")
    try:
        ide = int(input("Identificación del usuario: "))
        ventas = restaurante.consultar_ventas_por_usuario(ide)
        if not ventas:
            print("Este usuario no tiene compras registradas.")
            return
        for venta, prod in ventas:
            nombre_prod = prod.nombre if prod else "(producto no disponible)"
            print(f"• Producto: {nombre_prod} | Código: {venta.producto_codigo} | Cantidad: {venta.cantidad}")
    except ValueError:
        print("❌ Identificación debe ser numérica.")


def salir(restaurante: Restaurante) -> None:
    guardar_todo(restaurante)
    print("👋 Gracias por usar el sistema. ¡Hasta pronto!")


def main():
    # 🔄 Carga de las 3 colecciones al iniciar
    print("🔄 Cargando datos...")
    productos = ArchivoServicio.cargar_productos()
    usuarios = ArchivoServicio.cargar_usuarios()
    ventas = ArchivoServicio.cargar_ventas()

    restaurante = Restaurante("Sabor Andino")
    restaurante.cargar_productos(productos)
    restaurante.cargar_usuarios(usuarios)
    restaurante.cargar_ventas(ventas)

    print(f"✅ {len(productos)} productos | {len(usuarios)} usuarios | {len(ventas)} ventas cargados.")

    # Diccionario: opción → función
    acciones = {
        1: registrar_producto,
        2: buscar_producto,
        3: actualizar_producto,
        4: eliminar_producto,
        5: listar_productos,
        6: registrar_usuario,
        7: listar_usuarios,
        8: mostrar_categorias,
        9: vender_producto,
        10: consultar_ventas_usuario,
        11: salir
    }

    while True:
        mostrar_menu()
        try:
            op = int(input("Seleccione una opción: "))
            if op in acciones:
                acciones[op](restaurante)
                if op == 11:
                    break
            else:
                print("⚠️ Opción no válida.")
        except ValueError:
            print("⚠️ Ingrese un número.")


if __name__ == "__main__":
    main()
