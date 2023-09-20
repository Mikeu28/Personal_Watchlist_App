"""changed table named and added columns to UserShows

Revision ID: 00181841787f
Revises: 11bf3e0015c3
Create Date: 2023-09-20 16:23:24.471894

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00181841787f'
down_revision = '11bf3e0015c3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shows',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('image', sa.String(), nullable=True),
    sa.Column('platform', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('_password_hash', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_shows',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('show_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['show_id'], ['shows.id'], name=op.f('fk_user_shows_show_id_shows')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_user_shows_user_id_users')),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('show')
    op.drop_table('user')
    op.drop_table('user_show')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_show',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('rating', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.Column('show_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['show_id'], ['show.id'], name='fk_user_show_show_id_show'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='fk_user_show_user_id_user'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(), nullable=False),
    sa.Column('_password_hash', sa.VARCHAR(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('show',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=False),
    sa.Column('image', sa.VARCHAR(), nullable=True),
    sa.Column('platform', sa.VARCHAR(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('user_shows')
    op.drop_table('users')
    op.drop_table('shows')
    # ### end Alembic commands ###
