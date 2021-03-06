"""empty message

Revision ID: 897a415e4b18
Revises: 39b59ce10a90
Create Date: 2019-02-01 09:39:02.377746

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '897a415e4b18'
down_revision = '39b59ce10a90'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('izlet_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('izlet_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['izlet_id'], ['izlet.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('User Izleta')
    op.create_foreign_key(None, 'izlet', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'izlet', type_='foreignkey')
    op.create_table('User Izleta',
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.Column('izlet_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['izlet_id'], ['izlet.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    op.drop_table('izlet_user')
    # ### end Alembic commands ###
