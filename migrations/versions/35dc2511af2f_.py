"""empty message

Revision ID: 35dc2511af2f
Revises: None
Create Date: 2013-11-05 11:13:55.242797

"""

# revision identifiers, used by Alembic.
revision = '35dc2511af2f'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('project',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('url', sa.String(length=64), nullable=True),
    sa.Column('student_points', sa.Integer(), nullable=True),
    sa.Column('info', sa.String(length=5012), nullable=True),
    sa.Column('picture', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('url', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=90), nullable=True),
    sa.Column('passwd', sa.String(length=512), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('project')
    op.drop_table('user')
    ### end Alembic commands ###
