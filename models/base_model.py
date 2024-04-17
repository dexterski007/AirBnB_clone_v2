#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime, Integer


Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""

    id = Column(String(60), nullable=False, primary_key=True, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        elif kwargs:
            for k, v in kwargs.items():
                if k == "updated_at":
                    v = datetime.strptime(kwargs['updated_at'],
                                          '%Y-%m-%dT%H:%M:%S.%f')
                if k == "created_at":
                    v = datetime.strptime(kwargs['created_at'],
                                          '%Y-%m-%dT%H:%M:%S.%f')
                if k != "__class__":
                    setattr(self, k, v)

            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "updated_at" not in kwargs:
                self.updated_at = datetime.today()
            if "created_at" not in kwargs:
                self.created_at = datetime.today()

    def __str__(self):
        """Returns a string representation of the instance"""
        return '[{}] ({}) {}'.format(
            type(self).__name__, self.id, self.__dict__)

    def _repr__(self):
        """ return a string representation of the instance """
        return self.__str__()

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = dict(self.__dict__)
        dictionary["__class__"] = str(type(self).__name__)
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in dictionary.keys():
            del dictionary['_sa_instance_state']
        return dictionary

    def delete(self):
        """ delete object """
        models.storage.delete(self)
