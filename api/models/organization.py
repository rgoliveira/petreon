from models import db
from models.custom_types import GUID
import uuid

class Organization(db.Model):
    __tablename__ = 'organization'

    uuid            = db.Column(GUID, primary_key=True, default=uuid.uuid4)
    name            = db.Column(db.String(120), nullable=False)
    country         = db.Column(db.String(100))
    state           = db.Column(db.String(100))
    street_address  = db.Column(db.Text)
    logo            = db.Column(db.Text)
    contact_infos   = db.relationship("OrganizationContactInfo", backref="organization")

