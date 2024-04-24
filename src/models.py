import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    apellido = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    favoritos = relationship("Favoritos")
   


    





class Vehiculos(Base):
    __tablename__ = 'vehiculos'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    tipo = Column(String(250))
    pasajeros = Column(String(250))
    velocidad = Column(String(250), nullable=False)

class Planetas(Base):
    __tablename__ = 'planetas'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    tipo = Column(String(250))
    clima = Column(String(250))
    gravedad = Column(String(250), nullable=False)
    

class Personajes(Base):
    __tablename__ = 'personajes'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    raza = Column(String(250))
    altura = Column(String(250))
    peso = Column(String(250), nullable=False)



class Favoritos(Base):
    __tablename__ = 'Favoritos'
    id = Column(Integer, primary_key=True)
    personajes_id = Column(Integer, ForeignKey('personajes.id'))
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    planetas_id = Column(Integer, ForeignKey('planetas.id'))
    vehiculos_id = Column(Integer, ForeignKey("vehiculos"))
    personajes = relationship(Personajes)
    usuario = relationship(Usuario)
    planetas = relationship(Planetas)
    vehiculos = relationship(Vehiculos)


    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
