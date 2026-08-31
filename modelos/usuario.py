class Usuario:

    def __init__(self, identificacion: int, nombre: str, correo: str):
        if not isinstance(identificacion, int) or identificacion <= 0:
            raise ValueError("La identificación debe ser un número entero positivo.")
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        if "@" not in correo:
            raise ValueError("El correo no tiene formato válido.")

        self.identificacion = identificacion
        self.nombre = nombre.strip().capitalize()
        self.correo = correo.strip().lower()

    def __str__(self) -> str:
        return f"ID: {self.identificacion} | Nombre: {self.nombre} | Correo: {self.correo}"

    def mostrar_informacion(self) -> str:
        return self.__str__()

    def to_dict(self) -> dict:
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "correo": self.correo
        }

    @classmethod
    def from_dict(cls, datos: dict):
        return cls(
            identificacion=datos["identificacion"],
            nombre=datos["nombre"],
            correo=datos["correo"]
        )
