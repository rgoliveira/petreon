from sqlalchemy import *
from sqlalchemy.orm import relationship
from sqlalchemy_utils import EmailType
from models import Base
from models.custom_types import GUID
import uuid
import enum

class Donor(Base):
    __tablename__ = 'donor'

    uuid        = Column(GUID, primary_key=True, default=uuid.uuid4)
    name        = Column(String(255), nullable=False),
    email       = Column(EmailType)
    verified    = Column(Boolean, nullable=False, default=False)
    donations   = relationship("Donation", backref="donor")


