from sqlalchemy import *
from sqlalchemy.orm import relationship
from models import Base
from models.custom_types import GUID
import uuid
import enum

class Rescuee(Base):
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

    uuid                = Column(GUID, primary_key=True, default=uuid.uuid4)
    id                  = Column(String(120), nullable=False, unique=True)
    name                = Column(String(120), nullable=False)
    kind                = Column(String(100), nullable=False)
    age                 = Column(Float(2))
    size                = Column(Enum(Rescuee_Size))
    weight              = Column(Float(2))
    sex                 = Column(Enum(Rescuee_Sex))
    sterilized          = Column(Boolean)
    health_status       = Column(Text)
    temperament         = Column(String(100))
    description         = Column(Text)
    profile_pic         = Column(Text)
    date_of_rescue      = Column(Date)
    date_of_adoption    = Column(Date)
    pictures            = relationship("RescueePicture", backref="rescuee")
    campaigns           = relationship("Campaign", backref="rescuee")

    def __repr__(self):
        return "<Rescuee id=" + self.id + ">"

