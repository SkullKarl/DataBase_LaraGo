from sqlalchemy import text

def generar_vistas(engine):
    vistas = [
        """
        CREATE OR REPLACE VIEW Vista_Cotizaciones_Cliente AS
        SELECT 
            c."Nombre" AS cliente, 
            co."id_Cotización" AS id_cotizacion, 
            co."Estado" AS estado, 
            co."Fecha" AS fecha, 
            co."Descripcion" AS descripcion, 
            co."Precio_Añadido" AS precio_anadido
        FROM "Cliente" c
        JOIN "Cotización" co ON c."RUT_Cliente" = co."RUT_Cliente"
        ORDER BY c."Nombre", co."Fecha";
        """,
        """
        CCREATE OR REPLACE VIEW Vista_Ventas_Periodo AS
        SELECT 
            v."id_Venta" AS id_venta, 
            c."Nombre" AS cliente, 
            v."Monto_Venta" AS monto_venta, 
            v."Estado_Pago" AS estado_pago, 
            v."Fecha_Venta" AS fecha_venta, 
            v."Fecha_Entrega" AS fecha_entrega, 
            co."Descripcion" AS descripcion_cotizacion
        FROM "Venta" v
        JOIN "Cliente" c ON v."RUT_Cliente" = c."RUT_Cliente"
        JOIN "Cotización" co ON v."id_Cotizacion" = co."id_Cotización"
        ORDER BY v."Fecha_Venta";
        """,
        """
        CREATE OR REPLACE VIEW Vista_Ordenes_Manufacturacion_Ventas_Especificas AS
        SELECT 
            v."id_Venta" AS id_venta, 
            c."Nombre" AS cliente, 
            om."id_Orden" AS id_orden_manufacturacion, 
            om."Fecha_Inicio" AS fecha_inicio, 
            om."Fecha_Termino" AS fecha_termino, 
            om."Estado" AS estado_orden
        FROM "Venta" v
        JOIN "Cliente" c ON v."RUT_Cliente" = c."RUT_Cliente"
        JOIN "Orden_de_manufacturación" om ON v."id_Venta" = om."id_Venta"
        ORDER BY v."id_Venta";
        """,
        """
        CREATE OR REPLACE VIEW Vista_Estado_Orden_Manufacturacion AS
        SELECT 
            om."id_Orden" AS id_orden_manufacturacion, 
            om."Estado" AS estado_actual, 
            om."Fecha_Inicio" AS fecha_inicio, 
            om."Fecha_Termino" AS fecha_termino, 
            v."id_Venta" AS id_venta, 
            c."Nombre" AS cliente
        FROM "Orden_de_manufacturación" om
        JOIN "Venta" v ON om."id_Venta" = v."id_Venta"
        JOIN "Cliente" c ON v."RUT_Cliente" = c."RUT_Cliente"
        ORDER BY om."id_Orden";
        """,
        """
        CREATE OR REPLACE VIEW Vista_Materiales_Reposicion AS
        SELECT 
            m."Nro_Artículo", 
            m."Nombre_Artículo", 
            m."Cantidad_Existencias", 
            m."Nivel_Reposición", 
            m."Ubi_Existencias"
        FROM "Material" m
        WHERE m."Cantidad_Existencias" <= CAST(m."Nivel_Reposición" AS INTEGER)
        ORDER BY m."Cantidad_Existencias";
        """,
        """
        CREATE OR REPLACE VIEW Vista_Ordenes_Compra_Proveedor AS
        SELECT 
            p."Nombre" AS proveedor, 
            oc."id_Orden" AS id_orden_compra, 
            oc."Estado" AS estado_orden, 
            oc."Fecha_Compra" AS fecha_compra, 
            m."Nombre_Artículo" AS material, 
            a."Cantidad" AS cantidad_comprada
        FROM "Proveedor" p
        JOIN "Orden_de_Compra" oc ON p."id_Proveedor" = oc."id_Proveedor"
        JOIN "Abastece" a ON oc."id_Orden" = a."id_Orden"
        JOIN "Material" m ON a."Nro_Artículo" = m."Nro_Artículo"
        ORDER BY p."Nombre", oc."Fecha_Compra";
        """,
        """
        CREATE OR REPLACE VIEW Vista_Proveedores_Insumos AS
        SELECT 
            m."Nro_Artículo", 
            m."Nombre_Artículo", 
            p."id_Proveedor", 
            p."Nombre" AS proveedor, 
            p."Correo", 
            p."Teléfono"
        FROM "Material" m
        JOIN "Actualiza" a ON m."Nro_Artículo" = a."Nro_Artículo"
        JOIN "Proveedor" p ON a."id_Proveedor" = p."id_Proveedor"
        ORDER BY m."Nombre_Artículo";
        """
    ]

    with engine.begin() as conn:
        for i, vista in enumerate(vistas):
            try:
                conn.execute(text(vista))
                print(f" Vista {i + 1} creada/actualizada con éxito.")
            except Exception as e:
                print(f" Error en la vista {i + 1}: {e}")