"""empty message

Revision ID: 6d9513140d15
Revises: ec6e8d189416
Create Date: 2022-10-25 20:21:27.687933

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6d9513140d15'
down_revision = 'ec6e8d189416'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('empresas', sa.Column('tipo', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('empresas', 'tipo')
    # ### end Alembic commands ###
