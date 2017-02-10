from models import db
from models.custom_types import GUID
import uuid
from sqlalchemy_utils import EmailType

class Donor(db.Model):
    __tablename__ = 'donor'

    uuid        = db.Column(GUID, primary_key=True, default=uuid.uuid4)
    name        = db.Column(db.String(255), nullable=False)
    email       = db.Column(EmailType)
    verified    = db.Column(db.Boolean, nullable=False, default=False)
    donations   = db.relationship("Donation", backref="donor")

