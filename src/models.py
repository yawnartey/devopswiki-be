from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import ARRAY 
from database import Base

class Resource(Base):
    __tablename__ = "resources"

    id          = Column(Integer, primary_key=True, index=True)
    title       = Column(String, nullable=False)
    url         = Column(String, nullable=False, unique=True)
    description = Column(String)
    source      = Column(String)          
    type        = Column(String)    
    tags        = Column(ARRAY(String))