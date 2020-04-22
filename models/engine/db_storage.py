#!/usr/bin/python3
"""This is the class for DataBasetorage of the project AirBnB"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import environ
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """DBStorage class
    Attributes:
       __engine:
       __session:
    """

    __engine = None
    __session = None

    def __init__(self):
        """Declaration of the DBSstorage class
        """
        user = environ.get('HBNB_MYSQL_USER')
        pwd = environ.get('HBNB_MYSQL_PWD')
        host = environ.get('HBNB_MYSQL_HOST')
        db = environ.get('HBNB_MYSQL_DB')
        env = environ.get('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(user, pwd, host, db),
                                      pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Show all objects of a class
        """
        objects_dict = {}
        session = self.__session
        if not cls:
            clases = [City, State, User, Place, Amenity, Review]
            for clas in clases:
                objects = session.query(clas).all()
                for obj in objects:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    objects_dict[key] = obj
        else:
            objects = session.query(cls).all()
            for obj in objects:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                objects_dict[key] = obj
        return objects_dict

    def new(self, obj):
        """new method
        """
        self.__session.add(obj)

    def save(self):
        """save method
        """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete method
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """reload method
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """This method call the method remove"""
        self.__session.close()
