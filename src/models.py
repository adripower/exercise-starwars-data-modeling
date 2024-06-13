import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    last_name = Column(String(250))
    email = Column(String(250))
    password = Column(String(250))
    created = Column(String(250))
     

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    birth_year = Column(String(80))
    eye_color = Column(String(80))
    gender = Column(String(80))
    favoritos = relationship('FavoritosCharacters', backref='character', lazy=True)

class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    climate = Column(String(80))
    diameter = Column(Integer)
    gravity = Column(Integer)
    favoritos = relationship('FavoritosPlanet', backref='planet', lazy=True)

class Vehicle(Base):
    __tablename__ = 'vehicle'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    passenger = Column(Integer)
    length = Column(Integer)
    weapon = Column(String(250), nullable=False)
    armor = Column(String(250), nullable=False)
    favoritos = relationship('FavoritosVehicle', backref='vehicle', lazy=True)

class FavoritosCharacter(Base):
    __tablename__ = 'favoritos_character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable = False)
    character_id = Column(Integer, ForeignKey('character.id'))


class FavoritosPlanet(Base):
    __tablename__ = 'favoritos_planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable = False)
    planet_id = Column(Integer, ForeignKey('planet.id'))


class FavoritosVehicle(Base):
    __tablename__ = 'favoritos_vehicle'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable = False)
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))


   

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
