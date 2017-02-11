"""Fixing error from comma

Revision ID: 10862037de5f
Revises: 69153a241463
Create Date: 2017-02-10 20:51:10.184907

"""
from alembic import op
import sqlalchemy as sa
import models
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '10862037de5f'
down_revision = '69153a241463'
branch_labels = None
depends_on = None


"""

Adds a missing name column to the donor table.

"""
def upgrade():
    op.add_column('donor',
    sa.Column('name', sa.String(length=120), nullable=False)
    )

"""

Removes a missing name column to the donor table.

"""
def downgrade():
    op.drop_column('donor','name')
