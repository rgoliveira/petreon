from sqlalchemy.ext.declarative import declarative_base

# expore a Base to be used by our models
Base = declarative_base()

################################
# !!! LOAD EVERY MODEL HERE !!!#
################################
# This is needed to register them in Base.metadade,
# which is used by Alembic to read the database
# structure.

from models import campaign
from models import donation
from models import donor
from models import organization
from models import organization_contact_info
from models import pending_verification
from models import rescuee
from models import rescuee_picture

