#!/usr/bin/python3
"""
Create State Model
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
class State(Base):
   """
   Represents a state for a MySQL database
   __tablename__ (str): the name of the MySQL database
   id (Integer): The states id.
   name (String): The states name.
   """ 
   __tablename__ = "states"
   id = Column(Integer, primary_key=True)
   name = Column(String(128), nullable=False)