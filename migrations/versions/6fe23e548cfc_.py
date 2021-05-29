"""empty message

Revision ID: 6fe23e548cfc
Revises: a70bf60724e3
Create Date: 2021-05-29 01:07:51.927623

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6fe23e548cfc'
down_revision = 'a70bf60724e3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'medical_category', ['category_name'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'medical_category', type_='unique')
    # ### end Alembic commands ###