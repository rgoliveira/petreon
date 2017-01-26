from sqlalchemy import *
from sqlalchemy.orm import relationship
from models import Base
from models.custom_types import GUID
import uuid
import enum

class OrganizationContactInfo(Base):
    __tablename__ = 'organization_contact_info'

    class Organization_Contact_Info_Types(enum.Enum):
        phone     = "Phone"
        email     = "Email"
        facebook  = "Facebook"
        twitter   = "Twitter"
        instagram = "Instagram"
        address   = "Address"

    uuid                = Column(GUID, primary_key=True, default=uuid.uuid4)
    organization_uuid   = Column(GUID, ForeignKey('organization.uuid'), nullable=False)
    type                = Column(Enum(Organization_Contact_Info_Types), nullable=False)
    contact_info        = Column(Text, nullable=False)
    details             = Column(Text)

