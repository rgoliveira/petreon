from sqlalchemy import *
from sqlalchemy.orm import relationship
from models import Base
from models.custom_types import GUID
import uuid

class RescueePicture(Base):
    __tablename__ = 'rescuee_picture'

    uuid            = Column(GUID, primary_key=True, default=uuid.uuid4)
    rescuee_uuid    = Column(GUID, ForeignKey("rescuee.uuid"), nullable=False)
    path            = Column(Text, nullable=False)
    width           = Column(Integer)
    height          = Column(Integer)

