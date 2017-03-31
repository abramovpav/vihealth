"""empty message

Revision ID: b1aab5cf0866
Revises: 8ae6c92b16be
Create Date: 2017-03-31 14:26:16.928320

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b1aab5cf0866'
down_revision = '8ae6c92b16be'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('vi_state', 'happened_at',
               existing_type=sa.DATE(),
               nullable=False)
    op.drop_column('vi_state', 'pressure')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('vi_state', sa.Column('pressure', mysql.VARCHAR(collation=u'utf8_unicode_ci', length=100), nullable=False))
    op.alter_column('vi_state', 'happened_at',
               existing_type=sa.DATE(),
               nullable=True)
    # ### end Alembic commands ###
