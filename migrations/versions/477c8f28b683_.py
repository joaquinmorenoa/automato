"""empty message

Revision ID: 477c8f28b683
Revises: 
Create Date: 2019-04-11 09:16:56.030526

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '477c8f28b683'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('scrape_task', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'scrape_task', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'scrape_task', type_='foreignkey')
    op.drop_column('scrape_task', 'user_id')
    # ### end Alembic commands ###