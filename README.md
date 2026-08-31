# SEMANA-11

# 📋 Sistema de Gestión de Restaurante - Semana 11

**Asignatura:** Programación Orientada a Objetos
**Estudiante:** [Tu Nombre Completo]
**Fecha:** Agosto 2026

---

##  Objetivo
Incorporar el modelo **Venta** como relación entre Usuario y Producto, controlar **stock disponible**, ampliar la persistencia JSON a **productos, usuarios y ventas**, y demostrar el uso de colecciones para registrar y consultar operaciones.

---

## 📁 Estructura del proyecto
restaurante_app/
├── datos/
│ ├── productos.json ← Productos con stock actualizado
│ ├── usuarios.json ← Usuarios registrados
│ └── ventas.json ← Historial de ventas
├── modelos/
│ ├── producto.py ← Código, nombre, categoría, precio, stock
│ ├── usuario.py ← ID, nombre, correo
│ └── venta.py ← ID usuario, código producto, cantidad
├── servicios/
│ ├── archivo_servicio.py ← Lectura/escritura de los 3 archivos JSON
│ └── restaurante.py ← Lógica: registrar, vender, consultar
├── main.py ← Menú e interacción
└── README.md
plaintext

---

##  ¿Cómo funciona?

###  Stock del producto
Cada producto almacena su cantidad disponible. Al crear un producto se define su stock inicial. El sistema **nunca permite que el stock sea negativo**.

###  Relación Usuario + Producto → Venta
Existe Usuario registrado
Existe Producto disponible
Cantidad > 0 y ≤ stock actual
↓ 
Se crea objeto Venta(usuario_id, producto_codigo, cantidad)
Venta se agrega a la colección
Stock del producto disminuye
Se guardan ventas.json y productos.json
plaintext

###  Consulta de ventas por usuario
El sistema recorre toda la colección de ventas y filtra aquellas que coincidan con la identificación del usuario solicitado. Muestra el nombre del producto y cantidad comprada.

###  Persistencia ampliada
- **productos.json** → conserva código, nombre, categoría, precio y stock actualizado
- **usuarios.json** → conserva identificación, nombre y correo
- **ventas.json** → conserva relación usuario-producto-cantidad

Al iniciar: JSON → diccionarios → objetos Producto/Usuario/Venta
Al guardar: objetos → diccionarios → JSON

---

##  Excepciones controladas
- `FileNotFoundError` → archivos aún no existen → inicia vacío
- `JSONDecodeError` → archivo dañado → inicia vacío con aviso
- `PermissionError` → sin acceso → avisa y continúa en memoria
- `KeyError` → registro incompleto → omite ese registro
- `ValueError` → datos inválidos → rechaza esa operación

---

##  Pruebas realizadas
1. Registrar producto con stock = 10
2. Registrar usuario
3. Vender cantidad = 2 →  Venta ok, stock pasa a 8
4. Verificar ventas.json contiene la operación
5. Consultar ventas del usuario →  Aparece su compra
6. Cerrar y reiniciar el programa → Productos, usuarios y ventas recuperados
7. Intentar vender cantidad = 10 →  Rechazado por stock insuficiente
8. Confirmar que el stock sigue en 8 sin modificarse

---

##  Ejecución
```bash
python main.py
⚠️ Crea la carpeta datos/ antes de ejecutar. Los archivos .json se generan automáticamente al guardar.
💡 Reflexión
Las colecciones permiten almacenar objetos y relacionarlos entre sí. En esta semana, la clase Venta no reemplaza a Producto ni a Usuario, sino que los relaciona mediante sus identificadores. Así, al guardar en JSON se almacenan las claves de relación, y al reconstruir los objetos el sistema puede mostrar información completa recorriendo las colecciones. La persistencia garantiza que el historial de ventas y el stock actualizado se conserven aunque se apague el programa.
