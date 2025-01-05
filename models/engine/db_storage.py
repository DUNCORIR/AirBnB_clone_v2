#!/usr/bin/python3
"""DBStorage Engine SQLAlchemy Object Relational Mapper."""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    def __init__(self):
        """Initialize the DBStorage engine."""
        user = os.getenv("HBNB_MYSQL_USER")
        pwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST", "localhost")
        db = os.getenv("HBNB_MYSQL_DB")
        env = os.getenv("HBNB_ENV")

        # Create the engine
        self.__engine = create_engine(
            f"mysql+mysqldb://{user}:{pwd}@{host}/{db}",
            pool_pre_ping=True
        )
        Session = sessionmaker(bind=self.__engine)
        self.__session = scoped_session(Session)

    def all(self):
        """Return a dictionary of all objects from the database."""
        all_objects = {}
        # Explicitly list the classes you want to query
        classes = [State, City, User, Amenity, Place, Review]
        for cls in classes:
            if hasattr(cls, '__tablename__'):
                objects = self.__session.query(cls).all()
                for obj in objects:
                    all_objects[f"{cls.__name__}.{obj.id}"] = obj
        return all_objects

    def new(self, obj):
        """Add the object to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the current database session."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reloads all tables from the database."""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
