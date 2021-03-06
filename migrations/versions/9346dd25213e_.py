"""empty message

Revision ID: 9346dd25213e
Revises: 
Create Date: 2020-07-15 23:06:20.076839

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9346dd25213e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('order',
    sa.Column('order_id', sa.String(), nullable=False),
    sa.Column('items', sa.String(), nullable=False),
    sa.Column('delivery_note', sa.String(), nullable=True),
    sa.Column('requested_turnaround', sa.String(), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('ordered_by', sa.String(), nullable=False),
    sa.Column('ordered_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('payment_method', sa.String(), nullable=True),
    sa.Column('net_amount', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('order_id'),
    sa.UniqueConstraint('order_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order')
    # ### end Alembic commands ###
