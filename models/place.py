#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv
import models
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", cascade='all, delete-orphan',\
                                backref="place")
    else:
        @property
        def reviews(self):
            bulk = models.storage.all()
            elist = []
            result = []
            for i in bulk:
                review = i.replace(".", " ")
                review = shlex.split(review)
                if (review[0] == 'Review'):
                    elist.append(bulk[i])
            for el in elist:
                if (el.place_id == self.id):
                    result.append(el)
            return result
