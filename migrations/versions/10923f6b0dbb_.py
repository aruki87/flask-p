"""empty message

Revision ID: 10923f6b0dbb
Revises: 9000b7cd8a52
Create Date: 2019-02-04 09:51:12.403324

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10923f6b0dbb'
down_revision = '9000b7cd8a52'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'izlet', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'izlet', type_='foreignkey')
    # ### end Alembic commands ###
