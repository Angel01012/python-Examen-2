"""empty message

Revision ID: 0145b6ee5aee
Revises: 
Create Date: 2023-11-06 11:01:05.153333

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0145b6ee5aee'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('equipo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=250), nullable=True),
    sa.Column('cantidadjugadores', sa.Numeric(precision=10, scale=0), nullable=True),
    sa.Column('precioactual', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('liga', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('jugador',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=250), nullable=True),
    sa.Column('apellido', sa.String(length=250), nullable=True),
    sa.Column('edad', sa.Integer(), nullable=True),
    sa.Column('valormercado', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('mercancia',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=250), nullable=True),
    sa.Column('tipomercancia', sa.String(length=250), nullable=True),
    sa.Column('precio', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('edicion', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('partido',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('equipovisitante', sa.String(length=250), nullable=True),
    sa.Column('equipolocal', sa.String(length=250), nullable=True),
    sa.Column('arbitro', sa.String(length=250), nullable=True),
    sa.Column('balon', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('patrocinador',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=250), nullable=True),
    sa.Column('presupuesto', sa.Numeric(precision=8, scale=4), nullable=True),
    sa.Column('añoscontratado', sa.Integer(), nullable=True),
    sa.Column('pais', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('patrocinador')
    op.drop_table('partido')
    op.drop_table('mercancia')
    op.drop_table('jugador')
    op.drop_table('equipo')
    # ### end Alembic commands ###
