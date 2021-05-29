"""empty message

Revision ID: a70bf60724e3
Revises: 45453df2d83e
Create Date: 2021-05-29 00:57:37.534082

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a70bf60724e3'
down_revision = '45453df2d83e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('medical_category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category_name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('medical_record',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=False),
    sa.Column('last_name', sa.String(), nullable=False),
    sa.Column('phone_no', sa.String(length=10), nullable=False),
    sa.Column('medical_category_id', sa.Integer(), nullable=True),
    sa.Column('record_owner_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['medical_category_id'], ['medical_category.id'], ),
    sa.ForeignKeyConstraint(['record_owner_id'], ['account.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_index('ix_account_email', table_name='account')
    op.create_index(op.f('ix_account_email'), 'account', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_account_email'), table_name='account')
    op.create_index('ix_account_email', 'account', ['email'], unique=False)
    op.drop_table('medical_record')
    op.drop_table('medical_category')
    # ### end Alembic commands ###
