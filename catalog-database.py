import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
Base = declarative_base()

class Category(Base):

      __tablename__ = 'Category'

      name = Column(String(250), nullable=False)
      id = Column(Integer, primary_key=True)
  
  class Item(Base):

      __tablename__ = 'item'

      name = Column(String(250), nullable=False)
      id = Column(Integer, primary_key=True)
      description=Column (String(250) )
      #Relatioship
      Category_id=Column(Integer,ForeignKey(Category.id))
      Category=relatioship (Category)
      





engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine)
