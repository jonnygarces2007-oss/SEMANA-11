import json
from typing import List
from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


RUTA_PRODUCTOS = "datos/productos.json"
RUTA_USUARIOS = "datos/usuarios.json"
RUTA_VENTAS = "datos/ventas.json"


class ArchivoServicio:
    """Servicio encargado de leer y escribir productos, usuarios y ventas en JSON"""

    # ------------------- PRODUCTOS -------------------
    @staticmethod
    def cargar_productos() -> List[Producto]:
        productos: List[Producto] = []
        try:
            with open(RUTA_PRODUCTOS, mode="r", encoding="utf-8") as archivo:
                registros = json.load(archivo)
            for registro in registros:
                try:
                    productos.append(Producto.from_dict(registro))
                except KeyError as e:
                    print(f"⚠️ Registro producto incompleto, falta campo: {e} — se omite.")
                except ValueError as e:
                    print(f"⚠️ Registro producto inválido: {e} — se omite.")
        except FileNotFoundError:
            print("ℹ️ productos.json no existe. Se inicia con lista vacía.")
        except json.JSONDecodeError:
            print("⚠️ productos.json tiene formato dañado. Se inicia vacío.")
        except PermissionError:
            print(f"❌ Sin permiso para leer {RUTA_PRODUCTOS}.")
        except Exception as e:
            print(f"⚠️ Error leyendo productos: {e}")
        return productos

    @staticmethod
    def guardar_productos(productos: List[Producto]) -> bool:
        try:
            registros = [p.to_dict() for p in productos]
            with open(RUTA_PRODUCTOS, mode="w", encoding="utf-8") as archivo:
                json.dump(registros, archivo, indent=4, ensure_ascii=False)
            return True
        except PermissionError:
            print(f"❌ Sin permiso para escribir {RUTA_PRODUCTOS}.")
        except Exception as e:
            print(f"⚠️ Error guardando productos: {e}")
        return False

    # ------------------- USUARIOS -------------------
    @staticmethod
    def cargar_usuarios() -> List[Usuario]:
        usuarios: List[Usuario] = []
        try:
            with open(RUTA_USUARIOS, mode="r", encoding="utf-8") as archivo:
                registros = json.load(archivo)
            for registro in registros:
                try:
                    usuarios.append(Usuario.from_dict(registro))
                except KeyError as e:
                    print(f"⚠️ Registro usuario incompleto, falta: {e} — se omite.")
                except ValueError as e:
                    print(f"⚠️ Registro usuario inválido: {e} — se omite.")
        except FileNotFoundError:
            print("ℹ️ usuarios.json no existe. Se inicia con lista vacía.")
        except json.JSONDecodeError:
            print("⚠️ usuarios.json tiene formato dañado. Se inicia vacío.")
        except PermissionError:
            print(f"❌ Sin permiso para leer {RUTA_USUARIOS}.")
        except Exception as e:
            print(f"⚠️ Error leyendo usuarios: {e}")
        return usuarios

    @staticmethod
    def guardar_usuarios(usuarios: List[Usuario]) -> bool:
        try:
            registros = [u.to_dict() for u in usuarios]
            with open(RUTA_USUARIOS, mode="w", encoding="utf-8") as archivo:
                json.dump(registros, archivo, indent=4, ensure_ascii=False)
            return True
        except PermissionError:
            print(f"❌ Sin permiso para escribir {RUTA_USUARIOS}.")
        except Exception as e:
            print(f"⚠️ Error guardando usuarios: {e}")
        return False

    # ------------------- VENTAS -------------------
    @staticmethod
    def cargar_ventas() -> List[Venta]:
        ventas: List[Venta] = []
        try:
            with open(RUTA_VENTAS, mode="r", encoding="utf-8") as archivo:
                registros = json.load(archivo)
            for registro in registros:
                try:
                    ventas.append(Venta.from_dict(registro))
                except KeyError as e:
                    print(f"⚠️ Registro venta incompleto, falta: {e} — se omite.")
                except ValueError as e:
                    print(f"⚠️ Registro venta inválido: {e} — se omite.")
        except FileNotFoundError:
            print("ℹ️ ventas.json no existe. Se inicia con lista vacía.")
        except json.JSONDecodeError:
            print("⚠️ ventas.json tiene formato dañado. Se inicia vacío.")
        except PermissionError:
            print(f"❌ Sin permiso para leer {RUTA_VENTAS}.")
        except Exception as e:
            print(f"⚠️ Error leyendo ventas: {e}")
        return ventas

    @staticmethod
    def guardar_ventas(ventas: List[Venta]) -> bool:
        try:
            registros = [v.to_dict() for v in ventas]
            with open(RUTA_VENTAS, mode="w", encoding="utf-8") as archivo:
                json.dump(registros, archivo, indent=4, ensure_ascii=False)
            return True
        except PermissionError:
            print(f"❌ Sin permiso para escribir {RUTA_VENTAS}.")
        except Exception as e:
            print(f"⚠️ Error guardando ventas: {e}")
        return False
