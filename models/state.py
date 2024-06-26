#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, DateTime, Integer
import models
from models.city import City
import shlex


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        bulk = models.storage.all()
        elist = []
        result = []
        for k in bulk:
            city = k.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                elist.append(bulk[k])
        for el in elist:
            if (el.state_id == self.id):
                result.append(el)
        return (result)
