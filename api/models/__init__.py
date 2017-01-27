from sqlalchemy.ext.declarative import declarative_base

# expore a Base to be used by our models
Base = declarative_base()

################################
# !!! LOAD EVERY MODEL HERE !!!#
################################
# This is needed to register them in Base.metadade,
# which is used by Alembic to read the database
# structure.

from models.campaign                  import Campaign
from models.donation                  import Donation
from models.donor                     import Donor
from models.organization              import Organization
from models.organization_contact_info import OrganizationContactInfo
from models.pending_verification      import PendingVerification
from models.rescuee                   import Rescuee
from models.rescuee_picture           import RescueePicture

