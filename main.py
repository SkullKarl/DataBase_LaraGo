from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

engine = create_engine("sqlite:///mi_base.db")

class Base(DeclarativeBase):
    pass

class Cliente(Base):
    __tablename__ = "Cliente"

    rut_cliente: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str]
    correo: Mapped[str]
    telefono: Mapped[int]
    direccion: Mapped[str]

class Pide(Base):
    __tablename__ = "Pide"

    id: Mapped[int] = mapped_column(primary_key=True)

class Registra(Base):
    __tablename__ = "Registra"

    id: Mapped[int] = mapped_column(primary_key=True)

class Cotizacion(Base):
    __tablename__ = "Cotizacion"

    id: Mapped[int] = mapped_column(primary_key=True)

class Contiene(Base):
    __tablename__ = "Contiene"

    id: Mapped[int] = mapped_column(primary_key=True)

class Permite(Base):
    __tablename__ = "Permite"

    id: Mapped[int] = mapped_column(primary_key=True)

class Venta(Base):
    __tablename__ = "Venta"

    id: Mapped[int] = mapped_column(primary_key=True)

class Ordena(Base):
    __tablename__ = "Ordena"

    id: Mapped[int] = mapped_column(primary_key=True)

class Orden_de_manufacturacion(Base):
    __tablename__ = "Orden_de_manufacturacion"

    id: Mapped[int] = mapped_column(primary_key=True)

class Produce(Base):
    __tablename__ = "Produce"

    id: Mapped[int] = mapped_column(primary_key=True)

class Producto(Base):
    __tablename__ = "Producto"

    id: Mapped[int] = mapped_column(primary_key=True)

class Solicita(Base):
    __tablename__ = "Solicita"

    id: Mapped[int] = mapped_column(primary_key=True)

class Material(Base):
    __tablename__ = "Material"

    id: Mapped[int] = mapped_column(primary_key=True)

class Abastece(Base):
    __tablename__ = "Abastece"

    id: Mapped[int] = mapped_column(primary_key=True)

class Orden_de_compra(Base):
    __tablename__ = "Orden_de_compra"

    id: Mapped[int] = mapped_column(primary_key=True)

class Actualiza(Base):
    __tablename__ = "Actualiza"

    id: Mapped[int] = mapped_column(primary_key=True)

class Completa(Base):
    __tablename__ = "Completa"

    id: Mapped[int] = mapped_column(primary_key=True)

class Proveedor(Base):
    __tablename__ = "Proveedor"

    id: Mapped[int] = mapped_column(primary_key=True)

class Crea(Base):
    __tablename__ = "Proveedor"

    id: Mapped[int] = mapped_column(primary_key=True)

class Gestiona(Base):
    __tablename__ = "Proveedor"

    id: Mapped[int] = mapped_column(primary_key=True)

class Organiza(Base):
    __tablename__ = "Proveedor"

    id: Mapped[int] = mapped_column(primary_key=True)

Base.metadata.create_all(engine)