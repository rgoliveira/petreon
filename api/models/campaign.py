from sqlalchemy import *
from sqlalchemy.orm import relationship
from models import Base
from models.custom_types import GUID
import uuid

class Campaign(Base):
    __tablename__ = 'campaign'

    uuid            = Column(GUID, primary_key=True, default=uuid.uuid4)
    rescuee_uuid    = Column(GUID, ForeignKey("rescuee.uuid"))
    type            = Column(String(100), nullable=False)
    goal            = Column(Float(2))
    current_amount  = Column(Float(2))
    donations       = relationship("Donation", backref="campaign")


