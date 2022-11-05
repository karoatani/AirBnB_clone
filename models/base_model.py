#!/usr/bin/python3
from models import storage
import uuid
import datetime


class BaseModel(object):
    def __init__(self, *args, **kwargs):
        """
        Initialize base model attributes
        """
        if kwargs is None or kwargs == {}:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
        else:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.datetime.strptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f')
                setattr(self, key, value)
        storage.new(self)

    def __str__(self):
        """Return string representation of the object"""

        return f'[{type(self).__name__}({self.id}){self.__dict__}]'

    def save(self):
        """Save object to json"""
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """Convert object to dictionary"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = type(self).__name__
        new_dict["created_at"] = new_dict["created_at"].isoformat()
        new_dict["updated_at"] = new_dict["updated_at"].isoformat()

        return new_dict
