#!/usr/bin/python3
"""
python file that contains the class definition of a City
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import State
Base = declarative_base()


class City(Base):
    """
    states table and State class
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))

    def __init__(self, name, state_id):
        self.name = name
        self.state_id = state_id
