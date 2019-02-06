"""empty message

Revision ID: 8a0969446124
Revises: bb37a4bb7137
Create Date: 2019-02-04 09:49:50.691185

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a0969446124'
down_revision = 'bb37a4bb7137'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=140), nullable=True),
    sa.Column('description', sa.String(length=140), nullable=True),
    sa.Column('location', sa.String(length=140), nullable=True),
    sa.Column('picture', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_foreign_key(None, 'izlet', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'izlet', type_='foreignkey')
    op.drop_table('event')
    # ### end Alembic commands ###