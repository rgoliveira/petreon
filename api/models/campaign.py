from models import db
from models.custom_types import GUID
import uuid

class Campaign(db.Model):
    __tablename__ = 'campaign'

    uuid            = db.Column(GUID, primary_key=True, default=uuid.uuid4)
    rescuee_uuid    = db.Column(GUID, db.ForeignKey("rescuee.uuid"))
    type            = db.Column(db.String(100), nullable=False)
    goal            = db.Column(db.Float(2))
    current_amount  = db.Column(db.Float(2))
    donations       = db.relationship("Donation", backref="campaign")

