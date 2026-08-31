class Venta:

    def __init__(self, usuario_id: int, producto_codigo: int, cantidad: int):
        if not isinstance(usuario_id, int) or usuario_id <= 0:
            raise ValueError("Identificación de usuario inválida.")
        if not isinstance(producto_codigo, int) or producto_codigo <= 0:
            raise ValueError("Código de producto inválido.")
        if not isinstance(cantidad, int) or cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a cero.")

        self.usuario_id = usuario_id
        self.producto_codigo = producto_codigo
        self.cantidad = cantidad

    def __str__(self) -> str:
        return f"Usuario ID: {self.usuario_id} | Producto Código: {self.producto_codigo} | Cantidad: {self.cantidad}"

    def to_dict(self) -> dict:
        return {
            "usuario_id": self.usuario_id,
            "producto_codigo": self.producto_codigo,
            "cantidad": self.cantidad
        }

    @classmethod
    def from_dict(cls, datos: dict):
        return cls(
            usuario_id=datos["usuario_id"],
            producto_codigo=datos["producto_codigo"],
            cantidad=datos["cantidad"]
        )
