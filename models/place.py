#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
import models


# Define the 'place_amenity' table for the many-to-many relationship
place_amenity = Table(
    'place_amenity', 
    Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False)
)

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    # Relationship with Review (DBStorage)
    reviews = relationship("Review", backref="place", cascade="all, delete-orphan")

    # Relationship with Amenity (DBStorage)
    amenities = relationship(
        "Amenity", secondary=place_amenity, backref="places", viewonly=False
    )

    # Getter for reviews (FileStorage)
    @property
    def reviews(self):
        """Return list of Review instances with place_id equal to current Place.id"""
        from models.review import Review
        return [review for review in models.storage.all(Review).values()
                if review.place_id == self.id]

    # Getter for amenities (FileStorage)
    @property
    def amenities(self):
        """Getter for amenities in FileStorage"""
        return [amenity for amenity in models.storage.all(Amenity).values()
                if amenity.id in self.amenity_ids]

    # Setter for amenities (FileStorage)
    @amenities.setter
    def amenities(self, obj):
        """Setter for amenities in FileStorage"""
        if isinstance(obj, Amenity):
            self.amenity_ids.append(obj.id)