from sqlalchemy import *
from sqlalchemy.orm import relationship
from models import Base
from models.custom_types import GUID
import uuid

class Organization(Base):
    __tablename__ = 'organization'

    uuid            = Column(GUID, primary_key=True, default=uuid.uuid4)
    name            = Column(String(120), nullable=False)
    country         = Column(String(100))
    state           = Column(String(100))
    street_address  = Column(Text)
    logo            = Column(Text)
    contact_infos   = relationship("OrganizationContactInfo", backref="organization")

