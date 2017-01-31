from models import db
from models.custom_types import GUID
import uuid

class PendingVerification(db.Model):
    __tablename__ = 'pending_verification'

    uuid        = db.Column(GUID, primary_key=True, default=uuid.uuid4)
    donor_uuid  = db.Column(GUID, db.ForeignKey("donor.uuid"))
    expires     = db.Column(db.TIMESTAMP(timezone=True))

