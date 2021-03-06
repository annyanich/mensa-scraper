"""Create table 'menu_entries' to store scraped menu data

Revision ID: e106ab7b8607
Revises: a94bc6277195
Create Date: 2016-05-30 20:22:42.661503

"""

# revision identifiers, used by Alembic.
revision = 'e106ab7b8607'
down_revision = 'a94bc6277195'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('menu_entries',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('time_scraped', sa.DateTime(), nullable=False),
    sa.Column('date_valid', sa.Date(), nullable=False),
    sa.Column('mensa', sa.String(length=64), nullable=False),
    sa.Column('category', sa.String(length=64), nullable=False),
    sa.Column('description', sa.String(length=500), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('menu_entries')
    ### end Alembic commands ###
