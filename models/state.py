#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
import os

storage_type = os.getenv('HBNB_TYPE_STORAGE')


class State(BaseModel, Base):
    """
    State class representing a state in
    the database or file storage
    """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    if models.storage_type == "db":
        # Relationship for DBStorage
        cities = relationship(
            "City", backref="state", cascade="all, delete, delete-orphan"
        )
    else:
        # Getter attribute for Filestorage
        @property
        def cities(self):
            """
            Returns a list of City instances where
            state_id equals the current State.id.
            """
            return [
                city for city in models.storage.all(City).values()
                if city.state_id == self.id
            ]
