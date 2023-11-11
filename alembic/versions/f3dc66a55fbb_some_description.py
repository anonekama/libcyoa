"""Some description

Revision ID: f3dc66a55fbb
Revises: 
Create Date: 2023-11-10 18:25:23.655183

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f3dc66a55fbb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=256), nullable=False),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('is_superuser', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=False)
    op.create_table('link',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(length=256), nullable=True),
    sa.Column('title', sa.String(length=256), nullable=True),
    sa.Column('host', sa.String(length=256), nullable=True),
    sa.Column('submitter_id', sa.String(length=10), nullable=True),
    sa.ForeignKeyConstraint(['submitter_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_link_id'), 'link', ['id'], unique=False)
    op.create_index(op.f('ix_link_url'), 'link', ['url'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_link_url'), table_name='link')
    op.drop_index(op.f('ix_link_id'), table_name='link')
    op.drop_table('link')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###