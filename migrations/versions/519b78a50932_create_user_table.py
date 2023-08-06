"""Create user table

Revision ID: 519b78a50932
Revises: 
Create Date: 2023-08-05 20:49:59.120554

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '519b78a50932'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=256), nullable=False),
    sa.Column('user_role', sa.String(), nullable=True),
    sa.Column('blocked', sa.Boolean(), nullable=True),
    sa.Column('activity', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
