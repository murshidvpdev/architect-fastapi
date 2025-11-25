# Import Base first
from app.db.base import Base

# Import all models so Alembic sees them
from app.db.models import User