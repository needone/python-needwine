"""empty message

Revision ID: b068c9c70016
Revises: 
Create Date: 2020-11-13 15:18:54.687443

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b068c9c70016'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('role',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('label', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('wine_type',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('label', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('firstname', sa.String(), nullable=True),
    sa.Column('lastname', sa.String(), nullable=True),
    sa.Column('password_hash', sa.String(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('wine',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('year', sa.String(), nullable=True),
    sa.Column('type_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['type_id'], ['wine_type.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('notice',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('wine_id', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['wine_id'], ['wine.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('notice')
    op.drop_table('wine')
    op.drop_table('user')
    op.drop_table('wine_type')
    op.drop_table('role')
    # ### end Alembic commands ###
