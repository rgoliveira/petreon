from sqlalchemy import *
from sqlalchemy.orm import relationship
from models import Base
from models.custom_types import GUID
import uuid

class PendingVerification(Base):
    __tablename__ = 'pending_verification'

    uuid        = Column(GUID, primary_key=True, default=uuid.uuid4)
    donor_uuid  = Column(GUID, ForeignKey("donor.uuid"))
    expires     = Column(TIMESTAMP(timezone=True))


