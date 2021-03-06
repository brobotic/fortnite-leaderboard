"""season 4 stats init

Revision ID: c590b7bd7585
Revises: 3510d57f6c18
Create Date: 2018-05-01 12:33:59.582315

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c590b7bd7585'
down_revision = '3510d57f6c18'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('stats', sa.Column('s4_duo_kd', sa.Float(), nullable=True))
    op.add_column('stats', sa.Column('s4_duo_kills', sa.Integer(), nullable=True))
    op.add_column('stats', sa.Column('s4_duo_matches', sa.Integer(), nullable=True))
    op.add_column('stats', sa.Column('s4_duo_wins', sa.Integer(), nullable=True))
    op.add_column('stats', sa.Column('s4_duo_wr', sa.Float(), nullable=True))
    op.add_column('stats', sa.Column('s4_solo_kd', sa.Float(), nullable=True))
    op.add_column('stats', sa.Column('s4_solo_kills', sa.Integer(), nullable=True))
    op.add_column('stats', sa.Column('s4_solo_matches', sa.Integer(), nullable=True))
    op.add_column('stats', sa.Column('s4_solo_wins', sa.Integer(), nullable=True))
    op.add_column('stats', sa.Column('s4_solo_wr', sa.Float(), nullable=True))
    op.add_column('stats', sa.Column('s4_squad_kd', sa.Float(), nullable=True))
    op.add_column('stats', sa.Column('s4_squad_kills', sa.Integer(), nullable=True))
    op.add_column('stats', sa.Column('s4_squad_kpm', sa.Float(), nullable=True))
    op.add_column('stats', sa.Column('s4_squad_matches', sa.Integer(), nullable=True))
    op.add_column('stats', sa.Column('s4_squad_wins', sa.Integer(), nullable=True))
    op.add_column('stats', sa.Column('s4_squad_wr', sa.Float(), nullable=True))
    op.create_index(op.f('ix_stats_s4_duo_kd'), 'stats', ['s4_duo_kd'], unique=False)
    op.create_index(op.f('ix_stats_s4_duo_kills'), 'stats', ['s4_duo_kills'], unique=False)
    op.create_index(op.f('ix_stats_s4_duo_matches'), 'stats', ['s4_duo_matches'], unique=False)
    op.create_index(op.f('ix_stats_s4_duo_wins'), 'stats', ['s4_duo_wins'], unique=False)
    op.create_index(op.f('ix_stats_s4_duo_wr'), 'stats', ['s4_duo_wr'], unique=False)
    op.create_index(op.f('ix_stats_s4_solo_kd'), 'stats', ['s4_solo_kd'], unique=False)
    op.create_index(op.f('ix_stats_s4_solo_kills'), 'stats', ['s4_solo_kills'], unique=False)
    op.create_index(op.f('ix_stats_s4_solo_matches'), 'stats', ['s4_solo_matches'], unique=False)
    op.create_index(op.f('ix_stats_s4_solo_wins'), 'stats', ['s4_solo_wins'], unique=False)
    op.create_index(op.f('ix_stats_s4_solo_wr'), 'stats', ['s4_solo_wr'], unique=False)
    op.create_index(op.f('ix_stats_s4_squad_kd'), 'stats', ['s4_squad_kd'], unique=False)
    op.create_index(op.f('ix_stats_s4_squad_kills'), 'stats', ['s4_squad_kills'], unique=False)
    op.create_index(op.f('ix_stats_s4_squad_kpm'), 'stats', ['s4_squad_kpm'], unique=False)
    op.create_index(op.f('ix_stats_s4_squad_matches'), 'stats', ['s4_squad_matches'], unique=False)
    op.create_index(op.f('ix_stats_s4_squad_wins'), 'stats', ['s4_squad_wins'], unique=False)
    op.create_index(op.f('ix_stats_s4_squad_wr'), 'stats', ['s4_squad_wr'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_stats_s4_squad_wr'), table_name='stats')
    op.drop_index(op.f('ix_stats_s4_squad_wins'), table_name='stats')
    op.drop_index(op.f('ix_stats_s4_squad_matches'), table_name='stats')
    op.drop_index(op.f('ix_stats_s4_squad_kpm'), table_name='stats')
    op.drop_index(op.f('ix_stats_s4_squad_kills'), table_name='stats')
    op.drop_index(op.f('ix_stats_s4_squad_kd'), table_name='stats')
    op.drop_index(op.f('ix_stats_s4_solo_wr'), table_name='stats')
    op.drop_index(op.f('ix_stats_s4_solo_wins'), table_name='stats')
    op.drop_index(op.f('ix_stats_s4_solo_matches'), table_name='stats')
    op.drop_index(op.f('ix_stats_s4_solo_kills'), table_name='stats')
    op.drop_index(op.f('ix_stats_s4_solo_kd'), table_name='stats')
    op.drop_index(op.f('ix_stats_s4_duo_wr'), table_name='stats')
    op.drop_index(op.f('ix_stats_s4_duo_wins'), table_name='stats')
    op.drop_index(op.f('ix_stats_s4_duo_matches'), table_name='stats')
    op.drop_index(op.f('ix_stats_s4_duo_kills'), table_name='stats')
    op.drop_index(op.f('ix_stats_s4_duo_kd'), table_name='stats')
    op.drop_column('stats', 's4_squad_wr')
    op.drop_column('stats', 's4_squad_wins')
    op.drop_column('stats', 's4_squad_matches')
    op.drop_column('stats', 's4_squad_kpm')
    op.drop_column('stats', 's4_squad_kills')
    op.drop_column('stats', 's4_squad_kd')
    op.drop_column('stats', 's4_solo_wr')
    op.drop_column('stats', 's4_solo_wins')
    op.drop_column('stats', 's4_solo_matches')
    op.drop_column('stats', 's4_solo_kills')
    op.drop_column('stats', 's4_solo_kd')
    op.drop_column('stats', 's4_duo_wr')
    op.drop_column('stats', 's4_duo_wins')
    op.drop_column('stats', 's4_duo_matches')
    op.drop_column('stats', 's4_duo_kills')
    op.drop_column('stats', 's4_duo_kd')
    # ### end Alembic commands ###
