import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    subscription_date = Column(Date)
    favs = relationship('Favorite', backref="User")

class Favorite(Base):
    __tablename__ = 'favorites'

    id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    planet_id = Column(Integer, ForeignKey('planets.id'))
    character_id = Column(Integer, ForeignKey('characters.id'))

class Character(Base):
    __tablename__ = 'characters'

    id = Column(Integer, primary_key=True)
    character_name = Column(String, nullable=False)
    character_img = Column(String, nullable=False)
    birth_year = Column(Date)
    species = Column(String, nullable=False)
    height = Column(String, nullable=False)
    mass = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    hair_color = Column(String, nullable=False)
    skin_color = Column(String, nullable=False)
    # homeworld_id =

class Planet(Base):
    __tablename__ = 'planets'

    id = Column(Integer, primary_key=True)
    planet_name = Column(String, nullable=False)
    planet_img = Column(String, nullable=False)
    population = Column(Integer, nullable=False)
    rotation = Column(String, nullable=False)
    orbital = Column(String, nullable=False)
    diameter = Column(String, nullable=False)
    gravity = Column(String, nullable=False)
    terrain = Column(String, nullable=False)
    surface = Column(String, nullable=False)
    climate = Column(String, nullable=False)



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
