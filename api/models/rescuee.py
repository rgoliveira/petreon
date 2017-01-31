from models import db
from models.custom_types import GUID
import uuid
import enum
from flask.ext.restful import fields, marshal_with

class Rescuee(db.Model):
    __tablename__ = 'rescuee'

    class Rescuee_Size(enum.Enum):
        xs  = "Extra Small"
        s   = "Small"
        m   = "Medium"
        l   = "Large"
        xl  = "Extra Large"

    class Rescuee_Sex(enum.Enum):
        male    = "Male"
        female  = "Female"
        unknown = "Unknown"

    uuid                = db.Column(GUID, primary_key=True, default=uuid.uuid4)
    id                  = db.Column(db.String(120), nullable=False, unique=True)
    name                = db.Column(db.String(120), nullable=False)
    kind                = db.Column(db.String(100), nullable=False)
    age                 = db.Column(db.Float(2))
    size                = db.Column(db.Enum(Rescuee_Size))
    weight              = db.Column(db.Float(2))
    sex                 = db.Column(db.Enum(Rescuee_Sex))
    sterilized          = db.Column(db.Boolean)
    health_status       = db.Column(db.Text)
    temperament         = db.Column(db.String(100))
    description         = db.Column(db.Text)
    profile_pic         = db.Column(db.Text)
    date_of_rescue      = db.Column(db.Date)
    date_of_adoption    = db.Column(db.Date)
    pictures            = db.relationship("RescueePicture", backref="rescuee")
    campaigns           = db.relationship("Campaign", backref="rescuee")

    def __repr__(self):
        return "<Rescuee id=" + self.id + ">"

