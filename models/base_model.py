#!/usr/bin/python3
"""This module defines a base class for
all models in hbnb clone with SQLAlchemy."""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
import models
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        if kwargs:
            for key, value in kwargs.items():
                if key in (
                    "created_at", "updated_at"
                ) and isinstance(value, str):
                    value = datetime.fromisoformat(value)
                if key != "__class__":
                    setattr(self, key, value)

            # id id not provided, generate
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.utcnow()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.utcnow()

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return f"[{cls}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.utcnow()
        # Pass self to storage.new
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance to dictionary, exclude non-serializable fields"""
        dict_rep = self.__dict__.copy()  # Copy the dictionary
        dict_rep["id"] = str(self.id)  # Ensure 'id' is a string
        # Convert datetime to string
        dict_rep["created_at"] = self.created_at.isoformat()
        dict_rep["updated_at"] = self.updated_at.isoformat()

        # Remove SQLAlchemy instance state (not serializable)
        if "_sa_instance_state" in dict_rep:
            del dict_rep["_sa_instance_state"]

        return dict_rep

    def delete(self):
        """Delete the current instance from storage."""
        models.storage.delete(self)

    def __init__(self, *args, **kwargs):
        """Initialize Place instance"""
        super().__init__(*args, **kwargs)
        self.amenity_ids = []