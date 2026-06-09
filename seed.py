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
    pide,
    registra,
    permite,
    ordena,
    crea,
    organiza,
    completa,
)

with Session(engine) as session:

    # CLIENTES
    session.add_all([
        cliente(RUT_Cliente="6043909-5", Nombre="Alexis Santos Acuña", Correo="alexis@email.com", Teléfono="987654321", Dirección="Yumbel"),
        cliente(RUT_Cliente="12345678-9", Nombre="Benjamín Rebolledo", Correo="benjamin@email.com", Teléfono="912345678", Dirección="Concepción"),
        cliente(RUT_Cliente="77654321-0", Nombre="Comercial El Buen Sabor SpA", Correo="contacto@buensabor.cl", Teléfono="934567890", Dirección="Los Ángeles"),
        cliente(RUT_Cliente="11111111-1", Nombre="Food Express SpA", Correo="foodexpress@email.cl", Teléfono="911111111", Dirección="Chillán"),
        cliente(RUT_Cliente="22222222-2", Nombre="Municipalidad de Yumbel", Correo="compras@yumbel.cl", Teléfono="922222222", Dirección="Yumbel"),
        cliente(RUT_Cliente="33333333-3", Nombre="Café Ruta 5", Correo="cafe.ruta5@email.cl", Teléfono="933333333", Dirección="Cabrero"),
        cliente(RUT_Cliente="44444444-4", Nombre="Eventos del Sur SpA", Correo="eventos.sur@email.cl", Teléfono="944444444", Dirección="Temuco"),
        cliente(RUT_Cliente="55555555-5", Nombre="La Picada Móvil", Correo="picadamovil@email.cl", Teléfono="955555555", Dirección="Concepción"),
    ])

    # USUARIOS
    session.add_all([
        Usuario(id_Usuario=1, Nombre="Juan Fernández", Correo="juan@larago.cl", Contraseña="1234"),
        Usuario(id_Usuario=2, Nombre="Pedro Muñoz", Correo="pedro@larago.cl", Contraseña="1234"),
        Usuario(id_Usuario=3, Nombre="Ana Rojas", Correo="ana@larago.cl", Contraseña="1234"),
        Usuario(id_Usuario=4, Nombre="Carla Soto", Correo="carla@larago.cl", Contraseña="1234"),
        Usuario(id_Usuario=5, Nombre="Mario Díaz", Correo="mario@larago.cl", Contraseña="1234"),
        Usuario(id_Usuario=6, Nombre="Luis Pérez", Correo="luis@larago.cl", Contraseña="1234"),
    ])
    session.commit()

    session.add_all([
        Usuario_Ventas(id_Usuario=1),
        Usuario_Ventas(id_Usuario=4),
        Usuario_Taller(id_Usuario=2),
        Usuario_Taller(id_Usuario=5),
        Usuario_Inventario(id_Usuario=3),
        Usuario_Inventario(id_Usuario=6),
    ])

    # TIPO PRODUCTO
    session.add_all([
        tipo_producto(Nombre_Referencial="Foodtruck Premium", Descripción="Foodtruck 3.5 x 2 premium", Precio_base=Decimal("13990000.00")),
        tipo_producto(Nombre_Referencial="Trailer Baño", Descripción="Trailer baño 3.5 x 2 equipado", Precio_base=Decimal("13990000.00")),
        tipo_producto(Nombre_Referencial="Tiny Home", Descripción="Implementación personalizada Tiny Home", Precio_base=Decimal("3500000.00")),
        tipo_producto(Nombre_Referencial="Foodtruck Basico", Descripción="Foodtruck estándar sin equipamiento premium", Precio_base=Decimal("9990000.00")),
        tipo_producto(Nombre_Referencial="Trailer Logistico", Descripción="Trailer logístico para instituciones", Precio_base=Decimal("15990000.00")),
    ])

    # PROVEEDORES
    session.add_all([
        proveedor(id_Proveedor=1, Dirección="Av Industrial 1200", Teléfono="412223344", Correo="ventas@aceros.cl", Nombre="Aceros BioBio"),
        proveedor(id_Proveedor=2, Dirección="Ruta 5 Sur Km 480", Teléfono="432221111", Correo="electricasur@mail.cl", Nombre="Electrica Sur"),
        proveedor(id_Proveedor=3, Dirección="Las Industrias 900", Teléfono="412555666", Correo="sanitarios@mail.cl", Nombre="Sanitarios Pro"),
        proveedor(id_Proveedor=4, Dirección="Camino Norte 450", Teléfono="412777888", Correo="ruedas@mail.cl", Nombre="Ruedas y Ejes Ltda"),
        proveedor(id_Proveedor=5, Dirección="Av Bodega 300", Teléfono="413333444", Correo="pinturas@mail.cl", Nombre="Pinturas Industrial"),
    ])

    # MATERIALES
    session.add_all([
        material(Nro_Artículo=1001, Nombre_Artículo="Acero galvanizado", Ubi_Existencias="Bodega A", Descripción="Láminas acero estructura", Cantidad_Existencias=20, Nivel_Reposición="10", Días_Por_Pedido=5, Notas="Material crítico"),
        material(Nro_Artículo=1002, Nombre_Artículo="Eje torsión AL-KO", Ubi_Existencias="Bodega B", Descripción="Ejes torsión trailer", Cantidad_Existencias=4, Nivel_Reposición="6", Días_Por_Pedido=10, Notas="Stock bajo"),
        material(Nro_Artículo=1003, Nombre_Artículo="Cable eléctrico SEC", Ubi_Existencias="Bodega C", Descripción="Cableado eléctrico", Cantidad_Existencias=100, Nivel_Reposición="40", Días_Por_Pedido=3, Notas="Uso frecuente"),
        material(Nro_Artículo=1004, Nombre_Artículo="Lavamanos acero", Ubi_Existencias="Bodega B", Descripción="Lavamanos acero", Cantidad_Existencias=5, Nivel_Reposición="4", Días_Por_Pedido=7, Notas="Sanitario"),
        material(Nro_Artículo=1005, Nombre_Artículo="Neumático aro 15", Ubi_Existencias="Bodega D", Descripción="Neumático trailer", Cantidad_Existencias=8, Nivel_Reposición="8", Días_Por_Pedido=6, Notas="Reponer pronto"),
        material(Nro_Artículo=1006, Nombre_Artículo="Piso vinílico SPC", Ubi_Existencias="Bodega A", Descripción="Piso lavable", Cantidad_Existencias=30, Nivel_Reposición="15", Días_Por_Pedido=4, Notas="Terminaciones"),
        material(Nro_Artículo=1007, Nombre_Artículo="Bomba de agua", Ubi_Existencias="Bodega C", Descripción="Bomba sistema agua", Cantidad_Existencias=3, Nivel_Reposición="5", Días_Por_Pedido=8, Notas="Stock bajo"),
        material(Nro_Artículo=1008, Nombre_Artículo="Pintura anticorrosiva", Ubi_Existencias="Bodega E", Descripción="Pintura base estructura", Cantidad_Existencias=12, Nivel_Reposición="10", Días_Por_Pedido=4, Notas="Pintura"),
    ])

    session.commit()

    # COTIZACIONES
    session.add_all([
        cotizacion(id_Cotización=1, Estado="Aprobada", Fecha=date(2026, 5, 10), Descripcion="Foodtruck 3.5x2 premium", Precio_Añadido=Decimal("500000.00"), RUT_Cliente="6043909-5", id_Usuario=1),
        cotizacion(id_Cotización=2, Estado="Pendiente", Fecha=date(2026, 5, 15), Descripcion="Implementación Tiny Home", Precio_Añadido=Decimal("350000.00"), RUT_Cliente="12345678-9", id_Usuario=1),
        cotizacion(id_Cotización=3, Estado="Aprobada", Fecha=date(2026, 5, 20), Descripcion="Trailer baño equipado", Precio_Añadido=Decimal("0.00"), RUT_Cliente="77654321-0", id_Usuario=1),
        cotizacion(id_Cotización=4, Estado="Aprobada", Fecha=date(2026, 6, 1), Descripcion="Foodtruck hamburguesas", Precio_Añadido=Decimal("750000.00"), RUT_Cliente="11111111-1", id_Usuario=4),
        cotizacion(id_Cotización=5, Estado="Rechazada", Fecha=date(2026, 6, 3), Descripcion="Trailer baño evento", Precio_Añadido=Decimal("0.00"), RUT_Cliente="22222222-2", id_Usuario=4),
        cotizacion(id_Cotización=6, Estado="Aprobada", Fecha=date(2026, 6, 5), Descripcion="Foodtruck cafetería", Precio_Añadido=Decimal("400000.00"), RUT_Cliente="33333333-3", id_Usuario=1),
        cotizacion(id_Cotización=7, Estado="Pendiente", Fecha=date(2026, 6, 8), Descripcion="Trailer logístico", Precio_Añadido=Decimal("1000000.00"), RUT_Cliente="44444444-4", id_Usuario=4),
        cotizacion(id_Cotización=8, Estado="Aprobada", Fecha=date(2026, 6, 10), Descripcion="Foodtruck básico", Precio_Añadido=Decimal("200000.00"), RUT_Cliente="55555555-5", id_Usuario=1),
    ])

    session.commit()

    # VENTAS
    session.add_all([
        venta(id_Venta=1, Monto_Venta=Decimal("14490000.00"), Estado_Pago="Aprobado", Fecha_Venta=date(2026, 5, 12), Fecha_Entrega=date(2026, 6, 15), Comentarios="Pago inicial recibido", RUT_Cliente="6043909-5", id_Cotizacion=1),
        venta(id_Venta=2, Monto_Venta=Decimal("13990000.00"), Estado_Pago="Pendiente", Fecha_Venta=date(2026, 5, 22), Fecha_Entrega=date(2026, 6, 25), Comentarios="Pendiente saldo", RUT_Cliente="77654321-0", id_Cotizacion=3),
        venta(id_Venta=3, Monto_Venta=Decimal("14740000.00"), Estado_Pago="Aprobado", Fecha_Venta=date(2026, 6, 2), Fecha_Entrega=date(2026, 7, 10), Comentarios="Abono inicial", RUT_Cliente="11111111-1", id_Cotizacion=4),
        venta(id_Venta=4, Monto_Venta=Decimal("14390000.00"), Estado_Pago="Aprobado", Fecha_Venta=date(2026, 6, 7), Fecha_Entrega=date(2026, 7, 18), Comentarios="Cliente cafetería", RUT_Cliente="33333333-3", id_Cotizacion=6),
        venta(id_Venta=5, Monto_Venta=Decimal("10190000.00"), Estado_Pago="Pendiente", Fecha_Venta=date(2026, 6, 12), Fecha_Entrega=date(2026, 7, 25), Comentarios="Foodtruck básico", RUT_Cliente="55555555-5", id_Cotizacion=8),
    ])

    session.commit()

    # ORDENES MANUFACTURACION
    session.add_all([
        orden_de_manufacturacion(id_Orden=1, Fecha_Inicio=date(2026, 5, 13), Fecha_Termino=date(2026, 6, 10), Estado="En proceso", id_Venta=1),
        orden_de_manufacturacion(id_Orden=2, Fecha_Inicio=date(2026, 5, 23), Fecha_Termino=date(2026, 6, 20), Estado="No iniciada", id_Venta=2),
        orden_de_manufacturacion(id_Orden=3, Fecha_Inicio=date(2026, 6, 4), Fecha_Termino=date(2026, 7, 5), Estado="En proceso", id_Venta=3),
        orden_de_manufacturacion(id_Orden=4, Fecha_Inicio=date(2026, 6, 8), Fecha_Termino=date(2026, 7, 12), Estado="En proceso", id_Venta=4),
        orden_de_manufacturacion(id_Orden=5, Fecha_Inicio=date(2026, 6, 13), Fecha_Termino=date(2026, 7, 20), Estado="No iniciada", id_Venta=5),
    ])

    session.commit()

    # PRODUCTOS
    session.add_all([
        producto(id_Producto=1, Nombre_Referencial="Foodtruck Premium", Stock=1, id_Orden=1),
        producto(id_Producto=2, Nombre_Referencial="Trailer Baño", Stock=1, id_Orden=2),
        producto(id_Producto=3, Nombre_Referencial="Foodtruck Premium", Stock=1, id_Orden=3),
        producto(id_Producto=4, Nombre_Referencial="Foodtruck Premium", Stock=1, id_Orden=4),
        producto(id_Producto=5, Nombre_Referencial="Foodtruck Basico", Stock=1, id_Orden=5),
    ])

    session.commit()

    # ORDENES COMPRA
    session.add_all([
        orden_de_compra(id_Orden=1, Estado="Por pagar", Fecha_Compra=date(2026, 5, 25), id_Usuario=3, id_Proveedor=1),
        orden_de_compra(id_Orden=2, Estado="Pagada", Fecha_Compra=date(2026, 5, 26), id_Usuario=3, id_Proveedor=3),
        orden_de_compra(id_Orden=3, Estado="Procesando pago", Fecha_Compra=date(2026, 6, 5), id_Usuario=6, id_Proveedor=2),
        orden_de_compra(id_Orden=4, Estado="Por pagar", Fecha_Compra=date(2026, 6, 6), id_Usuario=3, id_Proveedor=1),
        orden_de_compra(id_Orden=5, Estado="Pagada", Fecha_Compra=date(2026, 6, 9), id_Usuario=6, id_Proveedor=4),
    ])

    session.commit()

    # RELACIONES PRINCIPALES
    session.add_all([
        contiene(id_Cotización=1, id_Producto=1, cantidad=1),
        contiene(id_Cotización=3, id_Producto=2, cantidad=1),
        contiene(id_Cotización=4, id_Producto=3, cantidad=1),
        contiene(id_Cotización=6, id_Producto=4, cantidad=1),
        contiene(id_Cotización=8, id_Producto=5, cantidad=1),

        pide(RUT_Cliente="6043909-5", id_Cotización=1),
        pide(RUT_Cliente="12345678-9", id_Cotización=2),
        pide(RUT_Cliente="77654321-0", id_Cotización=3),
        pide(RUT_Cliente="11111111-1", id_Cotización=4),
        pide(RUT_Cliente="22222222-2", id_Cotización=5),
        pide(RUT_Cliente="33333333-3", id_Cotización=6),
        pide(RUT_Cliente="44444444-4", id_Cotización=7),
        pide(RUT_Cliente="55555555-5", id_Cotización=8),

        registra(RUT_Cliente="6043909-5", id_Venta=1),
        registra(RUT_Cliente="77654321-0", id_Venta=2),
        registra(RUT_Cliente="11111111-1", id_Venta=3),
        registra(RUT_Cliente="33333333-3", id_Venta=4),
        registra(RUT_Cliente="55555555-5", id_Venta=5),

        permite(id_Cotización=1, id_Venta=1),
        permite(id_Cotización=3, id_Venta=2),
        permite(id_Cotización=4, id_Venta=3),
        permite(id_Cotización=6, id_Venta=4),
        permite(id_Cotización=8, id_Venta=5),

        ordena(id_Venta=1, id_Orden=1),
        ordena(id_Venta=2, id_Orden=2),
        ordena(id_Venta=3, id_Orden=3),
        ordena(id_Venta=4, id_Orden=4),
        ordena(id_Venta=5, id_Orden=5),

        crea(id_Cotización=1, id_Usuario=1),
        crea(id_Cotización=2, id_Usuario=1),
        crea(id_Cotización=3, id_Usuario=1),
        crea(id_Cotización=4, id_Usuario=4),
        crea(id_Cotización=5, id_Usuario=4),
        crea(id_Cotización=6, id_Usuario=1),
        crea(id_Cotización=7, id_Usuario=4),
        crea(id_Cotización=8, id_Usuario=1),

        gestiona(id_Orden=1, id_Usuario=2),
        gestiona(id_Orden=2, id_Usuario=2),
        gestiona(id_Orden=3, id_Usuario=5),
        gestiona(id_Orden=4, id_Usuario=2),
        gestiona(id_Orden=5, id_Usuario=5),
    ])

    session.commit()

    # MATERIALES SOLICITADOS
    session.add_all([
        solicita(id_Orden=1, Nro_Artículo=1001, Cantidad_Solicitada=12),
        solicita(id_Orden=1, Nro_Artículo=1002, Cantidad_Solicitada=6),
        solicita(id_Orden=1, Nro_Artículo=1003, Cantidad_Solicitada=30),
        solicita(id_Orden=2, Nro_Artículo=1003, Cantidad_Solicitada=30),
        solicita(id_Orden=2, Nro_Artículo=1004, Cantidad_Solicitada=6),
        solicita(id_Orden=3, Nro_Artículo=1001, Cantidad_Solicitada=15),
        solicita(id_Orden=3, Nro_Artículo=1002, Cantidad_Solicitada=8),
        solicita(id_Orden=3, Nro_Artículo=1005, Cantidad_Solicitada=10),
        solicita(id_Orden=4, Nro_Artículo=1006, Cantidad_Solicitada=20),
        solicita(id_Orden=4, Nro_Artículo=1007, Cantidad_Solicitada=4),
        solicita(id_Orden=5, Nro_Artículo=1001, Cantidad_Solicitada=8),
        solicita(id_Orden=5, Nro_Artículo=1008, Cantidad_Solicitada=5),
    ])

    session.commit()

    # PROVEEDORES Y COMPRAS
    session.add_all([
        actualiza(Nro_Artículo=1001, id_Proveedor=1),
        actualiza(Nro_Artículo=1002, id_Proveedor=4),
        actualiza(Nro_Artículo=1003, id_Proveedor=2),
        actualiza(Nro_Artículo=1004, id_Proveedor=3),
        actualiza(Nro_Artículo=1005, id_Proveedor=4),
        actualiza(Nro_Artículo=1006, id_Proveedor=5),
        actualiza(Nro_Artículo=1007, id_Proveedor=3),
        actualiza(Nro_Artículo=1008, id_Proveedor=5),

        abastece(id_Orden=1, Nro_Artículo=1002, Cantidad=4),
        abastece(id_Orden=2, Nro_Artículo=1004, Cantidad=3),
        abastece(id_Orden=3, Nro_Artículo=1003, Cantidad=40),
        abastece(id_Orden=4, Nro_Artículo=1001, Cantidad=20),
        abastece(id_Orden=4, Nro_Artículo=1002, Cantidad=6),
        abastece(id_Orden=5, Nro_Artículo=1005, Cantidad=10),

        organiza(id_Usuario=3, id_Orden=1),
        organiza(id_Usuario=3, id_Orden=2),
        organiza(id_Usuario=6, id_Orden=3),
        organiza(id_Usuario=3, id_Orden=4),
        organiza(id_Usuario=6, id_Orden=5),

        completa(id_Orden=1, id_Proveedor=1),
        completa(id_Orden=2, id_Proveedor=3),
        completa(id_Orden=3, id_Proveedor=2),
        completa(id_Orden=4, id_Proveedor=1),
        completa(id_Orden=5, id_Proveedor=4),
    ])

    session.commit()

    # HISTORIAL DE PRECIOS
    session.add_all([
        actualizacion_precio(Nro_Artículo=1001, Fecha_Actualización=date(2026, 5, 1), Precio_Unitario_Material=Decimal("25000.00")),
        actualizacion_precio(Nro_Artículo=1002, Fecha_Actualización=date(2026, 5, 1), Precio_Unitario_Material=Decimal("180000.00")),
        actualizacion_precio(Nro_Artículo=1003, Fecha_Actualización=date(2026, 5, 1), Precio_Unitario_Material=Decimal("2500.00")),
        actualizacion_precio(Nro_Artículo=1004, Fecha_Actualización=date(2026, 5, 1), Precio_Unitario_Material=Decimal("45000.00")),
        actualizacion_precio(Nro_Artículo=1005, Fecha_Actualización=date(2026, 5, 1), Precio_Unitario_Material=Decimal("65000.00")),
        actualizacion_precio(Nro_Artículo=1006, Fecha_Actualización=date(2026, 5, 1), Precio_Unitario_Material=Decimal("12000.00")),
        actualizacion_precio(Nro_Artículo=1007, Fecha_Actualización=date(2026, 5, 1), Precio_Unitario_Material=Decimal("85000.00")),
        actualizacion_precio(Nro_Artículo=1008, Fecha_Actualización=date(2026, 5, 1), Precio_Unitario_Material=Decimal("18000.00")),
    ])

    session.commit()

print("Datos insertados correctamente.")