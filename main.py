from datetime import date
from decimal import Decimal
from config import engine_config
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import create_engine, Integer, Numeric, String, Enum, Date, ForeignKey

engine = create_engine(engine_config)

class Base(DeclarativeBase):
    pass

class cliente(Base):
    __tablename__ = "Cliente"

    RUT_Cliente: Mapped[str] = mapped_column(String(12), primary_key=True)
    Nombre: Mapped[str] = mapped_column(String(50))
    Correo: Mapped[str] = mapped_column(String(50))
    Teléfono: Mapped[str] = mapped_column(String(15))
    Dirección: Mapped[str] = mapped_column(String(50))

class cotizacion(Base):
    __tablename__ = "Cotización"

    id_Cotización: Mapped[int] = mapped_column(primary_key=True)
    Estado: Mapped[str] = mapped_column(Enum("Pendiente", "Aprobada", "Rechazada", name ="estado_cotizacion"))
    Fecha: Mapped[date] = mapped_column(Date)
    Descripcion: Mapped[str] = mapped_column(String(250))
    Precio_Añadido: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    RUT_Cliente: Mapped[str] = mapped_column(String(12), ForeignKey("Cliente.RUT_Cliente"))
    id_Usuario: Mapped[int] = mapped_column(Integer, ForeignKey("Usuario_Ventas.id_Usuario"))

class contiene(Base):
    __tablename__ = "Contiene"

    id_Cotización: Mapped[int] = mapped_column(Integer, ForeignKey("Cotización.id_Cotización"), primary_key=True)
    id_Producto: Mapped[int] = mapped_column(Integer, ForeignKey("Producto.id_Producto"))
    cantidad: Mapped[int] = mapped_column(Integer)

class producto(Base):
    __tablename__ = "Producto"

    id_Producto: Mapped[int] = mapped_column(Integer, primary_key=True)
    Nombre_Referencial: Mapped[str] = mapped_column(String(30), ForeignKey("Tipo_Producto.Nombre_Referencial"))
    Stock: Mapped[int] = mapped_column(Integer)
    id_Orden: Mapped[int] = mapped_column(Integer, ForeignKey("Orden_de_manufacturación.id_Orden"))

class tipo_producto(Base):
    __tablename__ = "Tipo_Producto"

    Nombre_Referencial: Mapped[str] = mapped_column(String(30), primary_key=True)
    Descripción: Mapped[str] = mapped_column(String(100))
    Precio_base: Mapped[Decimal] = mapped_column(Numeric(10, 2))

class produce(Base):
    __tablename__ = "Produce"

    id_Producto: Mapped[int] = mapped_column(Integer, ForeignKey("Producto.id_Producto"), primary_key=True)
    id_Orden: Mapped[int] = mapped_column(Integer, ForeignKey("Orden_de_manufacturación.id_Orden"), primary_key=True)
    descripción: Mapped[str] = mapped_column(String(100))

class venta(Base):
    __tablename__ = "Venta"

    id_Venta: Mapped[int] = mapped_column(Integer, primary_key=True)
    Monto_Venta: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    Estado_Pago: Mapped[str] = mapped_column(Enum("Pendiente", "Aprobado", "Rechazado", name ="estado_venta"))
    Fecha_Venta: Mapped[date] = mapped_column(Date)
    Fecha_Entrega: Mapped[date] = mapped_column(Date)
    Comentarios: Mapped[str] = mapped_column(String(100))
    RUT_Cliente: Mapped[str] = mapped_column(String(12), ForeignKey("Cliente.RUT_Cliente"))
    id_Cotizacion: Mapped[int] = mapped_column(Integer, ForeignKey("Cotización.id_Cotización"))

class orden_de_manufacturacion(Base):
    __tablename__ = "Orden_de_manufacturación"

    id_Orden: Mapped[int] = mapped_column(Integer, primary_key=True)
    Fecha_Inicio: Mapped[date] = mapped_column(Date)
    Fecha_Termino: Mapped[date] = mapped_column(Date)
    Estado: Mapped[str] = mapped_column(Enum("No iniciada", "En proceso", "Terminada", name ="estado_orden_de_manufacturacion"))
    id_Venta: Mapped[int] = mapped_column(Integer, ForeignKey("Venta.id_Venta"))

class gestiona(Base):
    __tablename__ = "Gestiona"

    id_Orden: Mapped[int] = mapped_column(Integer, ForeignKey("Orden_de_manufacturación.id_Orden"), primary_key=True)
    id_Usuario: Mapped[int] = mapped_column(Integer, ForeignKey("Usuario_Taller.id_Usuario"), primary_key=True)

class Usuario(Base):
    __tablename__ = "Usuario"

    id_Usuario: Mapped[int] = mapped_column(Integer, primary_key=True)
    Nombre: Mapped[str] = mapped_column(String(25))
    Correo: Mapped[str] = mapped_column(String(25))
    Contraseña: Mapped[str] = mapped_column(String(25))

class Usuario_Ventas(Base):
    __tablename__ = "Usuario_Ventas"

    id_Usuario: Mapped[int] = mapped_column(Integer, ForeignKey("Usuario.id_Usuario"), primary_key=True)

class Usuario_Taller(Base):
    __tablename__ = "Usuario_Taller"

    id_Usuario: Mapped[int] = mapped_column(Integer, ForeignKey("Usuario.id_Usuario"), primary_key=True)

class Usuario_Inventario(Base):
    __tablename__ = "Usuario_Inventario"

    id_Usuario: Mapped[int] = mapped_column(Integer, ForeignKey("Usuario.id_Usuario"), primary_key=True)

class orden_de_compra(Base):
    __tablename__ = "Orden_de_Compra"

    id_Orden: Mapped[int] = mapped_column(Integer, primary_key=True)
    Estado: Mapped[str] = mapped_column(Enum("Por pagar", "Procesando pago", "Pagada", name ="estado_orden_de_compra"))
    Fecha_Compra: Mapped[date] = mapped_column(Date)
    id_Usuario: Mapped[int] = mapped_column(Integer, ForeignKey("Usuario_Inventario.id_Usuario"))
    id_Proveedor: Mapped[int] = mapped_column(Integer, ForeignKey("Proveedor.id_Proveedor"))

class abastece(Base):
    __tablename__ = "Abastece"

    id_Orden: Mapped[int] = mapped_column(Integer, ForeignKey("Orden_de_Compra.id_Orden"), primary_key=True)
    Nro_Artículo: Mapped[int] = mapped_column(Integer, ForeignKey("Material.Nro_Artículo"), primary_key=True)
    Cantidad: Mapped[int] = mapped_column(Integer)

class proveedor(Base):
    __tablename__ = "Proveedor"

    id_Proveedor: Mapped[int] = mapped_column(Integer, primary_key=True)
    Dirección: Mapped[str] = mapped_column(String(30))
    Teléfono: Mapped[str] = mapped_column(String(15))
    Correo: Mapped[str] = mapped_column(String(20))
    Nombre: Mapped[str] = mapped_column(String(30))

class actualiza(Base):
    __tablename__ = "Actualiza"

    Nro_Artículo: Mapped[int] = mapped_column(Integer, ForeignKey("Material.Nro_Artículo"), primary_key=True)
    id_Proveedor: Mapped[int] = mapped_column(Integer, ForeignKey("Proveedor.id_Proveedor"))

class actualizacion_precio(Base):
    __tablename__ = "Actualización_Precio"

    Nro_Artículo: Mapped[int] = mapped_column(Integer, ForeignKey("Material.Nro_Artículo"), primary_key=True)
    Fecha_Actualización: Mapped[date] = mapped_column(Date)
    Precio_Unitario_Material: Mapped[Decimal] = mapped_column(Numeric(10, 2))

class material(Base):
    __tablename__ = "Material"

    Nro_Artículo: Mapped[int] = mapped_column(Integer, primary_key=True)
    Nombre_Artículo: Mapped[str] = mapped_column(String(30))
    Ubi_Existencias: Mapped[str] = mapped_column(String(50))
    Descripción: Mapped[str] = mapped_column(String(100))
    Cantidad_Existencias: Mapped[int] = mapped_column(Integer)
    Nivel_Reposición: Mapped[str] = mapped_column(String(50))
    Días_Por_Pedido: Mapped[int] = mapped_column(Integer)
    Notas: Mapped[str] = mapped_column(String(100))

class solicita(Base):
    __tablename__ = "Solicita"

    id_Orden: Mapped[int] = mapped_column(Integer, ForeignKey("Orden_de_manufacturación.id_Orden"), primary_key=True)
    Nro_Artículo: Mapped[int] = mapped_column(Integer, ForeignKey("Material.Nro_Artículo"), primary_key=True)
    Cantidad_Solicitada: Mapped[int] = mapped_column(Integer)

class pide(Base):
    __tablename__ = "Pide"

    RUT_Cliente: Mapped[str] = mapped_column(String(12), ForeignKey("Cliente.RUT_Cliente"), primary_key=True)
    id_Cotización: Mapped[int] = mapped_column(Integer, ForeignKey("Cotización.id_Cotización"), primary_key=True)

class registra(Base):
    __tablename__ = "Registra"

    RUT_Cliente: Mapped[str] = mapped_column(String(12), ForeignKey("Cliente.RUT_Cliente"), primary_key=True)
    id_Venta: Mapped[int] = mapped_column(Integer, ForeignKey("Venta.id_Venta"), primary_key=True)

class permite(Base):
    __tablename__ = "Permite"

    id_Cotización: Mapped[int] = mapped_column(Integer, ForeignKey("Cotización.id_Cotización"), primary_key=True)
    id_Venta: Mapped[int] = mapped_column(Integer, ForeignKey("Venta.id_Venta"), primary_key=True)

class ordena(Base):
    __tablename__ = "Ordena"

    id_Venta: Mapped[int] = mapped_column(Integer, ForeignKey("Venta.id_Venta"), primary_key=True)
    id_Orden: Mapped[int] = mapped_column(Integer, ForeignKey("Orden_de_manufacturación.id_Orden"), primary_key=True)

class crea(Base):
    __tablename__ = "Crea"

    id_Cotización: Mapped[int] = mapped_column(Integer, ForeignKey("Cotización.id_Cotización"), primary_key=True)
    id_Usuario: Mapped[int] = mapped_column(Integer, ForeignKey("Usuario_Ventas.id_Usuario"), primary_key=True)

class organiza(Base):
    __tablename__ = "Organiza"

    id_Usuario: Mapped[int] = mapped_column(Integer, ForeignKey("Usuario_Inventario.id_Usuario"), primary_key=True)
    id_Orden: Mapped[int] = mapped_column(Integer, ForeignKey("Orden_de_Compra.id_Orden"), primary_key=True)

class completa(Base):
    __tablename__ = "Completa"

    id_Orden: Mapped[int] = mapped_column(Integer, ForeignKey("Orden_de_Compra.id_Orden"), primary_key=True)
    id_Proveedor: Mapped[int] = mapped_column(Integer, ForeignKey("Proveedor.id_Proveedor"), primary_key=True)

Base.metadata.create_all(engine)

print("Listooo")