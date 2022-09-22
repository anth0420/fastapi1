"""subir cambios a la db

Revision ID: f85b30bc1c50
Revises: 7055159fb0c0
Create Date: 2022-09-21 12:11:35.040867

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'f85b30bc1c50'
down_revision = '7055159fb0c0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('estudios', 'creacion')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('estudios', sa.Column('creacion', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
