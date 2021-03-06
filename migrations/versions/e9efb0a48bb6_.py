"""empty message

Revision ID: e9efb0a48bb6
Revises: 6fe23e548cfc
Create Date: 2021-05-29 01:30:48.849206

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e9efb0a48bb6'
down_revision = '6fe23e548cfc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('medical_record', sa.Column('disease', sa.String(), nullable=False))
    op.add_column('medical_record', sa.Column('bangalorean', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('medical_record', 'bangalorean')
    op.drop_column('medical_record', 'disease')
    # ### end Alembic commands ###
