from typing import List, Optional, Set, Tuple
from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class Restaurante:

    def __init__(self, nombre: str):
        self.nombre = nombre
        self._productos: List[Producto] = []
        self._usuarios: List[Usuario] = []
        self._ventas: List[Venta] = []

    # ------------------- Carga inicial -------------------
    def cargar_productos(self, lista: List[Producto]) -> None:
        for p in lista:
            if not self._buscar_producto_indice(p.codigo):
                self._productos.append(p)

    def cargar_usuarios(self, lista: List[Usuario]) -> None:
        for u in lista:
            if not self._buscar_usuario_indice(u.identificacion):
                self._usuarios.append(u)

    def cargar_ventas(self, lista: List[Venta]) -> None:
        self._ventas.extend(lista)

    # ------------------- Validaciones internas -------------------
    def _buscar_producto_indice(self, codigo: int) -> Optional[int]:
        for i, p in enumerate(self._productos):
            if p.codigo == codigo:
                return i
        return None

    def _buscar_usuario_indice(self, identificacion: int) -> Optional[int]:
        for i, u in enumerate(self._usuarios):
            if u.identificacion == identificacion:
                return i
        return None

    # ------------------- Productos -------------------
    def registrar_producto(self, producto: Producto) -> bool:
        if self._buscar_producto_indice(producto.codigo) is not None:
            return False
        self._productos.append(producto)
        return True

    def buscar_producto(self, codigo: int) -> Optional[Producto]:
        idx = self._buscar_producto_indice(codigo)
        return self._productos[idx] if idx is not None else None

    def actualizar_producto(self, codigo: int, nombre: str, categoria: str, precio: float, stock: int) -> bool:
        prod = self.buscar_producto(codigo)
        if not prod:
            return False
        try:
            prod.nombre = nombre.strip().capitalize()
            prod.categoria = categoria.strip().capitalize()
            prod.precio = round(float(precio), 2)
            prod.stock = stock
            return True
        except ValueError:
            return False

    def eliminar_producto(self, codigo: int) -> bool:
        idx = self._buscar_producto_indice(codigo)
        if idx is None:
            return False
        del self._productos[idx]
        return True

    def listar_productos(self) -> List[Producto]:
        return list(self._productos)

    # ------------------- Usuarios -------------------
    def registrar_usuario(self, usuario: Usuario) -> bool:
        if self._buscar_usuario_indice(usuario.identificacion) is not None:
            return False
        self._usuarios.append(usuario)
        return True

    def buscar_usuario(self, identificacion: int) -> Optional[Usuario]:
        idx = self._buscar_usuario_indice(identificacion)
        return self._usuarios[idx] if idx is not None else None

    def listar_usuarios(self) -> List[Usuario]:
        return list(self._usuarios)

    # ------------------- 🆕 VENTAS -------------------
    def vender_producto(self, codigo_producto: int, id_usuario: int, cantidad: int) -> bool:
        """
        Realiza la venta: valida existencia, cantidad y stock;
        registra venta y disminuye stock.
        """
        usuario = self.buscar_usuario(id_usuario)
        producto = self.buscar_producto(codigo_producto)

        if usuario is None or producto is None:
            return False
        if cantidad <= 0 or producto.stock < cantidad:
            return False

        venta = Venta(id_usuario, codigo_producto, cantidad)
        self._ventas.append(venta)
        producto.vender(cantidad)
        return True

    def consultar_ventas_por_usuario(self, id_usuario: int) -> List[Tuple[Venta, Optional[Producto]]]:
        
        resultado: List[Tuple[Venta, Optional[Producto]]] = []
        for venta in self._ventas:
            if venta.usuario_id == id_usuario:
                prod = self.buscar_producto(venta.producto_codigo)
                resultado.append((venta, prod))
        return resultado

    def listar_ventas(self) -> List[Venta]:
        return list(self._ventas)

    # ------------------- Categorías -------------------
    def obtener_categorias_unicas(self) -> Set[str]:
        return {p.categoria for p in self._productos}
