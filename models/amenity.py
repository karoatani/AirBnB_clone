#!/usr/bin/python3

"""
Amenity class that inherits from BaseModel
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Class that defines attributes for an amenity """
    name = ''
