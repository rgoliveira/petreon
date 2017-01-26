from sqlalchemy import *
from sqlalchemy.orm import relationship
from models import Base
from models.custom_types import GUID
import uuid

class Donation(Base):
    __tablename__ = 'donation'

    uuid            = Column(GUID, primary_key=True, default=uuid.uuid4)
    campaign_uuid   = Column(GUID, ForeignKey('campaign.uuid'), nullable=False)
    donor_uuid      = Column(GUID, ForeignKey('donor.uuid'), nullable=False)
    date            = Column(Date, nullable=False)
    amount          = Column(Float(2))


