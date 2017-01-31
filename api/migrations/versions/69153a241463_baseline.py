"""baseline

Revision ID: 69153a241463
Revises: 
Create Date: 2017-01-31 14:13:22.510367

"""
from alembic import op
import sqlalchemy as sa
import models
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '69153a241463'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table('donor',
    sa.Column('uuid', models.custom_types.GUID(), nullable=False),
    sa.Column('email', sqlalchemy_utils.types.email.EmailType(length=255), nullable=True),
    sa.Column('verified', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_table('organization',
    sa.Column('uuid', models.custom_types.GUID(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('country', sa.String(length=100), nullable=True),
    sa.Column('state', sa.String(length=100), nullable=True),
    sa.Column('street_address', sa.Text(), nullable=True),
    sa.Column('logo', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_table('rescuee',
    sa.Column('uuid', models.custom_types.GUID(), nullable=False),
    sa.Column('id', sa.String(length=120), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('kind', sa.String(length=100), nullable=False),
    sa.Column('age', sa.Float(precision=2), nullable=True),
    sa.Column('size', sa.Enum('xs', 's', 'm', 'l', 'xl', name='rescuee_size'), nullable=True),
    sa.Column('weight', sa.Float(precision=2), nullable=True),
    sa.Column('sex', sa.Enum('male', 'female', 'unknown', name='rescuee_sex'), nullable=True),
    sa.Column('sterilized', sa.Boolean(), nullable=True),
    sa.Column('health_status', sa.Text(), nullable=True),
    sa.Column('temperament', sa.String(length=100), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('profile_pic', sa.Text(), nullable=True),
    sa.Column('date_of_rescue', sa.Date(), nullable=True),
    sa.Column('date_of_adoption', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('uuid'),
    sa.UniqueConstraint('id')
    )
    op.create_table('campaign',
    sa.Column('uuid', models.custom_types.GUID(), nullable=False),
    sa.Column('rescuee_uuid', models.custom_types.GUID(), nullable=True),
    sa.Column('type', sa.String(length=100), nullable=False),
    sa.Column('goal', sa.Float(precision=2), nullable=True),
    sa.Column('current_amount', sa.Float(precision=2), nullable=True),
    sa.ForeignKeyConstraint(['rescuee_uuid'], ['rescuee.uuid'], ),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_table('organization_contact_info',
    sa.Column('uuid', models.custom_types.GUID(), nullable=False),
    sa.Column('organization_uuid', models.custom_types.GUID(), nullable=False),
    sa.Column('type', sa.Enum('phone', 'email', 'facebook', 'twitter', 'instagram', 'address', name='organization_contact_info_types'), nullable=False),
    sa.Column('contact_info', sa.Text(), nullable=False),
    sa.Column('details', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['organization_uuid'], ['organization.uuid'], ),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_table('pending_verification',
    sa.Column('uuid', models.custom_types.GUID(), nullable=False),
    sa.Column('donor_uuid', models.custom_types.GUID(), nullable=True),
    sa.Column('expires', sa.TIMESTAMP(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['donor_uuid'], ['donor.uuid'], ),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_table('rescuee_picture',
    sa.Column('uuid', models.custom_types.GUID(), nullable=False),
    sa.Column('rescuee_uuid', models.custom_types.GUID(), nullable=False),
    sa.Column('path', sa.Text(), nullable=False),
    sa.Column('width', sa.Integer(), nullable=True),
    sa.Column('height', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['rescuee_uuid'], ['rescuee.uuid'], ),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_table('donation',
    sa.Column('uuid', models.custom_types.GUID(), nullable=False),
    sa.Column('campaign_uuid', models.custom_types.GUID(), nullable=False),
    sa.Column('donor_uuid', models.custom_types.GUID(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('amount', sa.Float(precision=2), nullable=True),
    sa.ForeignKeyConstraint(['campaign_uuid'], ['campaign.uuid'], ),
    sa.ForeignKeyConstraint(['donor_uuid'], ['donor.uuid'], ),
    sa.PrimaryKeyConstraint('uuid')
    )


def downgrade():
    op.drop_table('donation')
    op.drop_table('rescuee_picture')
    op.drop_table('pending_verification')
    op.drop_table('organization_contact_info')
    op.drop_table('campaign')
    op.drop_table('rescuee')
    op.drop_table('organization')
    op.drop_table('donor')
