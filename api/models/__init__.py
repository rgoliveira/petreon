from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

################################
# !!! LOAD EVERY MODEL HERE !!!#
################################
# This is needed to register them in Base.metadata, which is used by Alembic to
# read the database structure.

from models.campaign                  import Campaign
from models.donation                  import Donation
from models.donor                     import Donor
from models.organization              import Organization
from models.organization_contact_info import OrganizationContactInfo
from models.pending_verification      import PendingVerification
from models.rescuee                   import Rescuee
from models.rescuee_picture           import RescueePicture

