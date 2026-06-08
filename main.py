from config import engine_config
from sqlalchemy import create_engine, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

engine = create_engine(engine_config)

class Base(DeclarativeBase):
    pass

class cliente(Base):
    __tablename__ = "Cliente"

    Rut_Cliente: Mapped[int] = mapped_column(primary_key=True)
    Nombre: Mapped[str] = mapped_column()
    Correo: Mapped[str] = mapped_column()
    telefono: Mapped[int] = mapped_column(Integer)
    direccion: Mapped[str] = mapped_column()

class cotizacion(Base):
    __tablename__ = "Cotización"

    id: Mapped[int] = mapped_column(primary_key=True)

class contiene(Base):
    __tablename__ = "Contiene"

    id: Mapped[int] = mapped_column(primary_key=True)

class producto(Base):
    __tablename__ = "Producto"

    id: Mapped[int] = mapped_column(primary_key=True)

class tipo_producto(Base):
    __tablename__ = "Tipo_Producto"

    id: Mapped[int] = mapped_column(primary_key=True)

class produce(Base):
    __tablename__ = "Produce"

    id: Mapped[int] = mapped_column(primary_key=True)

class venta(Base):
    __tablename__ = "Venta"

    id: Mapped[int] = mapped_column(primary_key=True)

class orden_de_manufacturacion(Base):
    __tablename__ = "Orden_de_manufacturación"

    id: Mapped[int] = mapped_column(primary_key=True)

class gestiona(Base):
    __tablename__ = "Gestiona"

    id: Mapped[int] = mapped_column(primary_key=True)



class orden_de_compra(Base):
    __tablename__ = "Orden_de_Compra"

    id: Mapped[int] = mapped_column(primary_key=True)

class abastece(Base):
    __tablename__ = "Abastece"

    id: Mapped[int] = mapped_column(primary_key=True)

class proveedor(Base):
    __tablename__ = "Proveedor"

    id: Mapped[int] = mapped_column(primary_key=True)

class actualiza(Base):
    __tablename__ = "Actualiza"

    id: Mapped[int] = mapped_column(primary_key=True)

class material(Base):
    __tablename__ = "Material"

    id: Mapped[int] = mapped_column(primary_key=True)

class solicita(Base):
    __tablename__ = "Solicita"

    id: Mapped[int] = mapped_column(primary_key=True)

class pide(Base):
    __tablename__ = "Pide"

    id: Mapped[int] = mapped_column(primary_key=True)

class registra(Base):
    __tablename__ = "Registra"

    id: Mapped[int] = mapped_column(primary_key=True)

class permite(Base):
    __tablename__ = "Permite"

    id: Mapped[int] = mapped_column(primary_key=True)

class ordena(Base):
    __tablename__ = "Ordena"

    id: Mapped[int] = mapped_column(primary_key=True)

class crea(Base):
    __tablename__ = "Crea"

    id: Mapped[int] = mapped_column(primary_key=True)

class organiza(Base):
    __tablename__ = "Organiza"

    id: Mapped[int] = mapped_column(primary_key=True)

class completa(Base):
    __tablename__ = "Completa"

    id: Mapped[int] = mapped_column(primary_key=True)

Base.metadata.create_all(engine)