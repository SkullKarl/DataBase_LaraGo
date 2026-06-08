from sqlalchemy import (
    create_engine,
    String,
    Integer,
    Date,
    Text,
    ForeignKey,
    Numeric
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import date


# Cambia la contraseña tuya según tu PostgreSQL
engine = create_engine(
    "postgresql+psycopg2://postgres:TU_CONTRASENIA_DEPOSTGRESQL@localhost:5432/larago",
    echo=True
)


class Base(DeclarativeBase):
    pass


class Cliente(Base):
    __tablename__ = "cliente"

    rut_cliente: Mapped[str] = mapped_column(String(12), primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    correo: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    telefono: Mapped[str] = mapped_column(String(20), unique=True)
    direccion: Mapped[str] = mapped_column(String(150))


class Usuario(Base):
    __tablename__ = "usuario"

    id_usuario: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    correo: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    contrasena: Mapped[str] = mapped_column(String(100), nullable=False)


class UsuarioVentas(Base):
    __tablename__ = "usuario_ventas"

    id_usuario: Mapped[int] = mapped_column(
        ForeignKey("usuario.id_usuario"),
        primary_key=True
    )


class UsuarioTaller(Base):
    __tablename__ = "usuario_taller"

    id_usuario: Mapped[int] = mapped_column(
        ForeignKey("usuario.id_usuario"),
        primary_key=True
    )


class UsuarioInventario(Base):
    __tablename__ = "usuario_inventario"

    id_usuario: Mapped[int] = mapped_column(
        ForeignKey("usuario.id_usuario"),
        primary_key=True
    )


class TipoProducto(Base):
    __tablename__ = "tipo_producto"

    nombre_referencial: Mapped[str] = mapped_column(String(100), primary_key=True)
    descripcion: Mapped[str] = mapped_column(Text)
    precio_base: Mapped[int] = mapped_column(Integer)


class Cotizacion(Base):
    __tablename__ = "cotizacion"

    id_cotizacion: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    estado: Mapped[str] = mapped_column(String(30), nullable=False)
    fecha: Mapped[date] = mapped_column(Date, nullable=False)
    descripcion: Mapped[str] = mapped_column(Text)
    precio_anadido: Mapped[int] = mapped_column(Integer, default=0)

    rut_cliente: Mapped[str] = mapped_column(
        ForeignKey("cliente.rut_cliente"),
        nullable=False
    )

    id_usuario: Mapped[int] = mapped_column(
        ForeignKey("usuario_ventas.id_usuario"),
        nullable=False
    )


class Venta(Base):
    __tablename__ = "venta"

    id_venta: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    monto_venta: Mapped[int] = mapped_column(Integer, nullable=False)
    estado_pago: Mapped[str] = mapped_column(String(30), nullable=False)
    fecha_venta: Mapped[date] = mapped_column(Date, nullable=False)
    fecha_entrega: Mapped[date] = mapped_column(Date)
    comentarios: Mapped[str] = mapped_column(Text)

    rut_cliente: Mapped[str] = mapped_column(
        ForeignKey("cliente.rut_cliente"),
        nullable=False
    )

    id_cotizacion: Mapped[int] = mapped_column(
        ForeignKey("cotizacion.id_cotizacion"),
        unique=True,
        nullable=False
    )


class OrdenManufacturacion(Base):
    __tablename__ = "orden_manufacturacion"

    id_orden: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    fecha_inicio: Mapped[date] = mapped_column(Date, nullable=False)
    fecha_termino: Mapped[date] = mapped_column(Date)
    estado: Mapped[str] = mapped_column(String(30), nullable=False)

    id_venta: Mapped[int] = mapped_column(
        ForeignKey("venta.id_venta"),
        nullable=False
    )


class Producto(Base):
    __tablename__ = "producto"

    id_producto: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    stock: Mapped[int] = mapped_column(Integer, default=0)

    nombre_referencial: Mapped[str] = mapped_column(
        ForeignKey("tipo_producto.nombre_referencial"),
        nullable=False
    )

    id_orden: Mapped[int] = mapped_column(
        ForeignKey("orden_manufacturacion.id_orden"),
        nullable=False
    )


class Proveedor(Base):
    __tablename__ = "proveedor"

    id_proveedor: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    direccion: Mapped[str] = mapped_column(String(150))
    telefono: Mapped[str] = mapped_column(String(20))
    correo: Mapped[str] = mapped_column(String(100))
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)


class Material(Base):
    __tablename__ = "material"

    nro_articulo: Mapped[int] = mapped_column(primary_key=True)
    nombre_articulo: Mapped[str] = mapped_column(String(100), nullable=False)
    ubi_existencias: Mapped[str] = mapped_column(String(100))
    descripcion: Mapped[str] = mapped_column(Text)
    cantidad_existencias: Mapped[int] = mapped_column(Integer, nullable=False)
    nivel_reposicion: Mapped[int] = mapped_column(Integer, nullable=False)
    dias_por_pedido: Mapped[int] = mapped_column(Integer)
    notas: Mapped[str] = mapped_column(Text)


class OrdenCompra(Base):
    __tablename__ = "orden_compra"

    id_orden_compra: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    estado: Mapped[str] = mapped_column(String(30), nullable=False)
    fecha_compra: Mapped[date] = mapped_column(Date, nullable=False)

    id_usuario: Mapped[int] = mapped_column(
        ForeignKey("usuario_inventario.id_usuario"),
        nullable=False
    )

    id_proveedor: Mapped[int] = mapped_column(
        ForeignKey("proveedor.id_proveedor"),
        nullable=False
    )


class Contiene(Base):
    __tablename__ = "contiene"

    id_cotizacion: Mapped[int] = mapped_column(
        ForeignKey("cotizacion.id_cotizacion"),
        primary_key=True
    )

    id_producto: Mapped[int] = mapped_column(
        ForeignKey("producto.id_producto"),
        primary_key=True
    )

    cantidad: Mapped[int] = mapped_column(Integer, nullable=False)


class Gestiona(Base):
    __tablename__ = "gestiona"

    id_orden: Mapped[int] = mapped_column(
        ForeignKey("orden_manufacturacion.id_orden"),
        primary_key=True
    )

    id_usuario: Mapped[int] = mapped_column(
        ForeignKey("usuario_taller.id_usuario"),
        primary_key=True
    )


class Abastece(Base):
    __tablename__ = "abastece"

    id_orden_compra: Mapped[int] = mapped_column(
        ForeignKey("orden_compra.id_orden_compra"),
        primary_key=True
    )

    nro_articulo: Mapped[int] = mapped_column(
        ForeignKey("material.nro_articulo"),
        primary_key=True
    )

    cantidad: Mapped[int] = mapped_column(Integer, nullable=False)


class Actualiza(Base):
    __tablename__ = "actualiza"

    nro_articulo: Mapped[int] = mapped_column(
        ForeignKey("material.nro_articulo"),
        primary_key=True
    )

    id_proveedor: Mapped[int] = mapped_column(
        ForeignKey("proveedor.id_proveedor"),
        primary_key=True
    )


class ActualizacionPrecio(Base):
    __tablename__ = "actualizacion_precio"

    nro_articulo: Mapped[int] = mapped_column(
        ForeignKey("material.nro_articulo"),
        primary_key=True
    )

    fecha_actualizacion: Mapped[date] = mapped_column(Date, primary_key=True)

    precio_unitario_material: Mapped[int] = mapped_column(Integer, nullable=False)


class Solicita(Base):
    __tablename__ = "solicita"

    id_orden: Mapped[int] = mapped_column(
        ForeignKey("orden_manufacturacion.id_orden"),
        primary_key=True
    )

    nro_articulo: Mapped[int] = mapped_column(
        ForeignKey("material.nro_articulo"),
        primary_key=True
    )

    cantidad_solicitada: Mapped[int] = mapped_column(Integer, nullable=False)


Base.metadata.create_all(engine)

print("Tablas creadas correctamente.")