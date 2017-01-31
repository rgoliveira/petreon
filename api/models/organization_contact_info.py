from models import db
from models.custom_types import GUID
import uuid
import enum

class OrganizationContactInfo(db.Model):
    __tablename__ = 'organization_contact_info'

    class Organization_Contact_Info_Types(enum.Enum):
        phone     = "Phone"
        email     = "Email"
        facebook  = "Facebook"
        twitter   = "Twitter"
        instagram = "Instagram"
        address   = "Address"

    uuid                = db.Column(GUID, primary_key=True, default=uuid.uuid4)
    organization_uuid   = db.Column(GUID, db.ForeignKey('organization.uuid'), nullable=False)
    type                = db.Column(db.Enum(Organization_Contact_Info_Types), nullable=False)
    contact_info        = db.Column(db.Text, nullable=False)
    details             = db.Column(db.Text)

