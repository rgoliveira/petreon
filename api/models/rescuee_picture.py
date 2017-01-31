from models import db
from models.custom_types import GUID
import uuid

class RescueePicture(db.Model):
    __tablename__ = 'rescuee_picture'

    uuid            = db.Column(GUID, primary_key=True, default=uuid.uuid4)
    rescuee_uuid    = db.Column(GUID, db.ForeignKey("rescuee.uuid"), nullable=False)
    path            = db.Column(db.Text, nullable=False)
    width           = db.Column(db.Integer)
    height          = db.Column(db.Integer)

