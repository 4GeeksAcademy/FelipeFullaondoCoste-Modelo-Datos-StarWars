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
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    subscription_date = Column(Date)
    favorites = relationship('Favorite', back_populates='user')

class Favorite(Base):
    __tablename__ = 'favorites'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='favorites')
    planet_id = Column(Integer, ForeignKey('planets.id'))
    character_id = Column(Integer, ForeignKey('characters.id'))

class Character(Base):
    __tablename__ = 'characters'

    id = Column(Integer, primary_key=True)
    character_name = Column(String, nullable=False)
    species = Column(String)
    gender = Column(String)
    homeworld_id = Column(String, ForeignKey('planets.id'))
    planet = relationship('Planet', back_populates='character') 

class Planet(Base):
    __tablename__ = 'planets'

    id = Column(Integer, primary_key=True)
    characters = relationship('Character', back_populates='planet')
    planet_img = Column(String)
    population = Column(Integer)
    climate = Column(String)



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
