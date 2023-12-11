"""Empty Init

Revision ID: 4cd9aa90c8fb
Revises: 
Create Date: 2023-12-11 05:12:48.563495

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4cd9aa90c8fb'
down_revision = None
branch_labels = None
depends_on = None

# includes the code that would be needed to perform changes to the database based on this migration
def upgrade() -> None:
    pass

# includes any code that would be needed to undo this migration and return to the previous state.
def downgrade() -> None:
    pass
