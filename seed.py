from datetime import date
from decimal import Decimal
from sqlalchemy.orm import Session

from main import (
    engine,
    cliente,
    Usuario,
    Usuario_Ventas,
    Usuario_Taller,
    Usuario_Inventario,
    tipo_producto,
    proveedor,
    material,
    cotizacion,
    venta,
    orden_de_manufacturacion,
    producto,
    orden_de_compra,
    contiene,
    gestiona,
    abastece,
    actualiza,
    actualizacion_precio,
    solicita,
)

with Session(engine) as session:

    # CLIENTES
    session.add_all([
        cliente(
            RUT_Cliente="6043909-5",
            Nombre="Alexis Santos Acuña",
            Correo="alexis@email.com",
            Teléfono="987654321",
            Dirección="Yumbel"
        ),
        cliente(
            RUT_Cliente="12345678-9",
            Nombre="Benjamín Rebolledo",
            Correo="benjamin@email.com",
            Teléfono="912345678",
            Dirección="Concepción"
        ),
        cliente(
            RUT_Cliente="77654321-0",
            Nombre="Comercial El Buen Sabor SpA",
            Correo="contacto@buensabor.cl",
            Teléfono="934567890",
            Dirección="Los Ángeles"
        )
    ])

    # USUARIOS
    session.add_all([
        Usuario(id_Usuario=1, Nombre="Juan Carlos Fernández", Correo="juan@larago.cl", Contraseña="1234"),
        Usuario(id_Usuario=2, Nombre="Pedro Muñoz", Correo="pedro@larago.cl", Contraseña="1234"),
        Usuario(id_Usuario=3, Nombre="Ana Rojas", Correo="ana@larago.cl", Contraseña="1234"),
    ])
    session.commit()

    session.add_all([
        Usuario_Ventas(id_Usuario=1),
        Usuario_Taller(id_Usuario=2),
        Usuario_Inventario(id_Usuario=3),
    ])

    # TIPO PRODUCTO
    session.add_all([
        tipo_producto(
            Nombre_Referencial="Foodtruck Premium",
            Descripción="Foodtruck 3.5 x 2 metros con implementación premium",
            Precio_base=Decimal("13990000.00")
        ),
        tipo_producto(
            Nombre_Referencial="Trailer Baño",
            Descripción="Tráiler baño 3.5 x 2 metros equipado",
            Precio_base=Decimal("13990000.00")
        ),
        tipo_producto(
            Nombre_Referencial="Tiny Home",
            Descripción="Implementación personalizada para Tiny Home",
            Precio_base=Decimal("3500000.00")
        )
    ])

    # PROVEEDORES
    session.add_all([
        proveedor(id_Proveedor=1, Dirección="Av. Industrial 1200", Teléfono="412223344", Correo="ventas@aceros.cl", Nombre="Aceros BioBio"),
        proveedor(id_Proveedor=2, Dirección="Ruta 5 Sur Km 480", Teléfono="432221111", Correo="contacto@electrica.cl", Nombre="Eléctrica Sur"),
        proveedor(id_Proveedor=3, Dirección="Av. Las Industrias 900", Teléfono="412555666", Correo="ventas@sanitarios.cl", Nombre="Sanitarios Pro"),
    ])

    # MATERIALES
    session.add_all([
        material(
            Nro_Artículo=1001,
            Nombre_Artículo="Acero galvanizado",
            Ubi_Existencias="Bodega A",
            Descripción="Láminas de acero para estructura",
            Cantidad_Existencias=20,
            Nivel_Reposición="10",
            Días_Por_Pedido=5,
            Notas="Material crítico"
        ),
        material(
            Nro_Artículo=1002,
            Nombre_Artículo="Eje torsión AL-KO",
            Ubi_Existencias="Bodega B",
            Descripción="Ejes de torsión para tráiler",
            Cantidad_Existencias=4,
            Nivel_Reposición="6",
            Días_Por_Pedido=10,
            Notas="Stock bajo"
        ),
        material(
            Nro_Artículo=1003,
            Nombre_Artículo="Cable eléctrico SEC",
            Ubi_Existencias="Bodega C",
            Descripción="Cableado para instalación eléctrica",
            Cantidad_Existencias=100,
            Nivel_Reposición="40",
            Días_Por_Pedido=3,
            Notas="Uso frecuente"
        ),
        material(
            Nro_Artículo=1004,
            Nombre_Artículo="Lavamanos acero",
            Ubi_Existencias="Bodega B",
            Descripción="Lavamanos para foodtruck o baño",
            Cantidad_Existencias=5,
            Nivel_Reposición="4",
            Días_Por_Pedido=7,
            Notas="Proveedor sanitario"
        ),
    ])

    session.commit()

    # COTIZACIONES
    session.add_all([
        cotizacion(
            id_Cotización=1,
            Estado="Aprobada",
            Fecha=date(2026, 5, 10),
            Descripcion="Foodtruck 3.5x2 modelo premium",
            Precio_Añadido=Decimal("500000.00"),
            RUT_Cliente="6043909-5",
            id_Usuario=1
        ),
        cotizacion(
            id_Cotización=2,
            Estado="Pendiente",
            Fecha=date(2026, 5, 15),
            Descripcion="Implementación Tiny Home personalizada",
            Precio_Añadido=Decimal("350000.00"),
            RUT_Cliente="12345678-9",
            id_Usuario=1
        ),
        cotizacion(
            id_Cotización=3,
            Estado="Aprobada",
            Fecha=date(2026, 5, 20),
            Descripcion="Trailer baño equipado",
            Precio_Añadido=Decimal("0.00"),
            RUT_Cliente="77654321-0",
            id_Usuario=1
        ),
    ])

    session.commit()

    # VENTAS
    session.add_all([
        venta(
            id_Venta=1,
            Monto_Venta=Decimal("14490000.00"),
            Estado_Pago="Aprobado",
            Fecha_Venta=date(2026, 5, 12),
            Fecha_Entrega=date(2026, 6, 15),
            Comentarios="Pago inicial recibido",
            RUT_Cliente="6043909-5",
            id_Cotizacion=1
        ),
        venta(
            id_Venta=2,
            Monto_Venta=Decimal("13990000.00"),
            Estado_Pago="Pendiente",
            Fecha_Venta=date(2026, 5, 22),
            Fecha_Entrega=date(2026, 6, 25),
            Comentarios="Cliente pendiente de saldo",
            RUT_Cliente="77654321-0",
            id_Cotizacion=3
        ),
    ])

    session.commit()

    # ORDENES MANUFACTURACION
    session.add_all([
        orden_de_manufacturacion(
            id_Orden=1,
            Fecha_Inicio=date(2026, 5, 13),
            Fecha_Termino=date(2026, 6, 10),
            Estado="En proceso",
            id_Venta=1
        ),
        orden_de_manufacturacion(
            id_Orden=2,
            Fecha_Inicio=date(2026, 5, 23),
            Fecha_Termino=date(2026, 6, 20),
            Estado="No iniciada",
            id_Venta=2
        ),
    ])

    session.commit()

    # PRODUCTOS
    session.add_all([
        producto(id_Producto=1, Nombre_Referencial="Foodtruck Premium", Stock=1, id_Orden=1),
        producto(id_Producto=2, Nombre_Referencial="Trailer Baño", Stock=1, id_Orden=2),
    ])

    session.commit()

    # RELACIONES
    session.add_all([
        contiene(id_Cotización=1, id_Producto=1, cantidad=1),
        contiene(id_Cotización=3, id_Producto=2, cantidad=1),

        gestiona(id_Orden=1, id_Usuario=2),
        gestiona(id_Orden=2, id_Usuario=2),

        solicita(id_Orden=1, Nro_Artículo=1001, Cantidad_Solicitada=12),
        solicita(id_Orden=1, Nro_Artículo=1002, Cantidad_Solicitada=6),
        solicita(id_Orden=2, Nro_Artículo=1003, Cantidad_Solicitada=30),
        solicita(id_Orden=2, Nro_Artículo=1004, Cantidad_Solicitada=6),

        actualiza(Nro_Artículo=1001, id_Proveedor=1),
        actualiza(Nro_Artículo=1002, id_Proveedor=1),
        actualiza(Nro_Artículo=1003, id_Proveedor=2),
        actualiza(Nro_Artículo=1004, id_Proveedor=3),
    ])

    session.commit()

    # ORDENES COMPRA
    session.add_all([
        orden_de_compra(
            id_Orden=1,
            Estado="Por pagar",
            Fecha_Compra=date(2026, 5, 25),
            id_Usuario=3,
            id_Proveedor=1
        ),
        orden_de_compra(
            id_Orden=2,
            Estado="Pagada",
            Fecha_Compra=date(2026, 5, 26),
            id_Usuario=3,
            id_Proveedor=3
        ),
    ])

    session.commit()

    session.add_all([
        abastece(id_Orden=1, Nro_Artículo=1002, Cantidad=4),
        abastece(id_Orden=2, Nro_Artículo=1004, Cantidad=3),

        actualizacion_precio(
            Nro_Artículo=1001,
            Fecha_Actualización=date(2026, 5, 1),
            Precio_Unitario_Material=Decimal("25000.00")
        ),
        actualizacion_precio(
            Nro_Artículo=1002,
            Fecha_Actualización=date(2026, 5, 1),
            Precio_Unitario_Material=Decimal("180000.00")
        ),
        actualizacion_precio(
            Nro_Artículo=1003,
            Fecha_Actualización=date(2026, 5, 1),
            Precio_Unitario_Material=Decimal("2500.00")
        ),
        actualizacion_precio(
            Nro_Artículo=1004,
            Fecha_Actualización=date(2026, 5, 1),
            Precio_Unitario_Material=Decimal("45000.00")
        ),
    ])

    session.commit()

print("Datos insertados correctamente.")