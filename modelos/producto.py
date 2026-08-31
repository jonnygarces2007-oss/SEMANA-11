class Producto:

    def __init__(self, codigo: int, nombre: str, categoria: str, precio: float, stock: int = 0):
        if not isinstance(codigo, int) or codigo <= 0:
            raise ValueError("El código debe ser un número entero positivo.")
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        if not categoria.strip():
            raise ValueError("La categoría no puede estar vacía.")
        if not isinstance(precio, (int, float)) or precio <= 0:
            raise ValueError("El precio debe ser mayor a cero.")
        if not isinstance(stock, int) or stock < 0:
            raise ValueError("El stock debe ser un número entero no negativo.")

        self.codigo = codigo
        self.nombre = nombre.strip().capitalize()
        self.categoria = categoria.strip().capitalize()
        self.precio = round(float(precio), 2)
        self.stock = stock

    def __str__(self) -> str:
        return f"Código: {self.codigo} | Nombre: {self.nombre} | Categoría: {self.categoria} | Precio: ${self.precio:.2f} | Stock: {self.stock}"

    def mostrar_informacion(self) -> str:
        return self.__str__()

    def vender(self, cantidad: int) -> bool:
        if cantidad <= 0 or self.stock < cantidad:
            return False
        self.stock -= cantidad
        return True

    def to_dict(self) -> dict:
       
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "stock": self.stock
        }

    @classmethod
    def from_dict(cls, datos: dict):
      
        return cls(
            codigo=datos["codigo"],
            nombre=datos["nombre"],
            categoria=datos["categoria"],
            precio=datos["precio"],
            stock=datos.get("stock", 0)
        )
