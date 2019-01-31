"""Izlet

Revision ID: bef34016c8d0
Revises: ada2d655fd63
Create Date: 2019-01-30 18:23:33.860298

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bef34016c8d0'
down_revision = 'ada2d655fd63'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('izlet', sa.Column('picture', sa.String(length=200), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('izlet', 'picture')
    # ### end Alembic commands ###
