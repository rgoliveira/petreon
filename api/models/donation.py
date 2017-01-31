from models import db
from models.custom_types import GUID
import uuid

class Donation(db.Model):
    __tablename__ = 'donation'

    uuid            = db.Column(GUID, primary_key=True, default=uuid.uuid4)
    campaign_uuid   = db.Column(GUID, db.ForeignKey('campaign.uuid'), nullable=False)
    donor_uuid      = db.Column(GUID, db.ForeignKey('donor.uuid'), nullable=False)
    date            = db.Column(db.Date, nullable=False)
    amount          = db.Column(db.Float(2))

