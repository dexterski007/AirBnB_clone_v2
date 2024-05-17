#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""
from os import getenv
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """This class manages storage of hbnb models using SQLalchemy"""
    __engine = None
    __session = None

    def __init__(self):
        """ init method for db storage """
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        dbname = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(user, password, host, dbname),
                                      pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        new_dic = {}
        if cls is None:
            clslist = [User, State, City, Amenity, Place, Review]
            for cl in clslist:
                command = self.__session.query(cl)
                for i in command:
                    k = "{}.{}".format(type(i).__name__, i.id)
                    new_dic[k] = i
        else:
            if type(cls) is str:
                cls = eval(cls)
            command = self.__session.query(cls)
            for i in command:
                k = "{}.{}".format(type(i).__name__, i.id)
                new_dic[k] = i
        return (new_dic)

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__session.add(obj)

    def save(self):
        """Saves storage dictionary to file"""
        self.__session.commit()

    def reload(self):
        """ create tables and create current session"""
        Base.metadata.create_all(self.__engine)
        sess = sessionmaker(expire_on_commit=False, bind=self.__engine)
        self.__session = scoped_session(sess)()

    def delete(self, obj=None):
        """ delete object """
        if obj:
            self.__session.delete(obj)

    def close(self):
        """ calls reload """
        self.__session.close()
