import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(250), nullable=False)
    surname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    favoritos = relationship("Favoritos")
    subscripcion_date = Column(DateTime(), default=datetime.now())
   


    





class Vehicles(Base):
    __tablename__ = 'vehicles'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    tipo = Column(String(250))
    pasajeros = Column(String(250))
    velocidad = Column(String(250), nullable=False)
    favorites = relationship('Favorites', backref='vehicles', lazy=True)

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    tipo = Column(String(250))
    clima = Column(String(250))
    gravedad = Column(String(250), nullable=False)
    favorites = relationship('Favorites', backref='planets', lazy=True)
    

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    age = Column(String(250))
    heigh  = Column(String(250))
    peso = Column(String(250), nullable=False)
    favorites = relationship('Favorites', backref='person', lazy=True)

class FavoritesVehicles(Base):
    __tablename__ = 'favorites_vehicles'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'))
    vehicles = relationship(Vehicles)

class FavoritesPlanets(Base):
    __tablename__ = 'favorites_planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    planets_id = Column(Integer, ForeignKey('planets.id'))
    planets = relationship(Planets)

# class Favoritos(Base):
#     __tablename__ = 'Favoritos'
#     id = Column(Integer, primary_key=True)
#     personajes_id = Column(Integer, ForeignKey('personajes.id'))
#     usuario_id = Column(Integer, ForeignKey('usuario.id'))
#     planetas_id = Column(Integer, ForeignKey('planetas.id'))
#     vehiculos_id = Column(Integer, ForeignKey("vehiculos"))
#     personajes = relationship(Personajes)
#     usuario = relationship(Usuario)
#     planetas = relationship(Planetas)
#     vehiculos = relationship(Vehiculos)


    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
