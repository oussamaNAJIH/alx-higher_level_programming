#!/usr/bin/python3
"""
python file that contains the class definition of a State
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class State(Base):
    """
    states table and State class
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)

    def __init__(self, name):
        self.name = name
