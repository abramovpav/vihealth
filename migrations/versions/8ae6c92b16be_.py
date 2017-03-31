"""empty message

Revision ID: 8ae6c92b16be
Revises: 7b7c2db59561
Create Date: 2017-03-29 13:25:02.182268

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '8ae6c92b16be'
down_revision = '7b7c2db59561'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('vi_state', 'happened_at',
               existing_type=mysql.DATE(),
               nullable=True)
    op.alter_column('vi_state', 'created_at',
               existing_type=mysql.DATETIME(),
               nullable=True)
    op.alter_column('vi_state', 'updated_at',
               existing_type=mysql.DATETIME(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('vi_state', 'updated_at',
               existing_type=mysql.VARCHAR(80),
               nullable=True)
    op.alter_column('vi_state', 'created_at',
               existing_type=mysql.VARCHAR(80),
               nullable=True)
    op.alter_column('vi_state', 'happened_at',
               existing_type=mysql.VARCHAR(80),
               nullable=True)
    # ### end Alembic commands ###