#!/usr/bin/python3
"""Defines the State class."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
import os
import models
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    if os.getenv('HBNB_TYPE_STORAGE') == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete")

    else:
        name = ""

        @property
        def cities(self):
            """Return City list"""
            state_list = []
            obj_dict = models.storage.all(City)
            for key, value in obj_dict.items():
                if value.state_id == self.id:
                    state_list.append(obj_dict[key])
            return state_list
