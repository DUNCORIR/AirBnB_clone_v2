#!/usr/bin/python3
"""Initializes the storage system for the HBNB project."""
import os
# Import all model classes
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy.ext.declarative import declarative_base

# Create a base class for all model classes
Base = declarative_base()
# Check the storage type from the environment variable
storage_type = os.getenv('HBNB_TYPE_STORAGE')

if storage_type == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()

else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

# Reload the storage to initialize objects
storage.reload()
