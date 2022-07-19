"""
    Ad database model.
"""

# ORM.
from sqlalchemy.sql import func
from sqlalchemy import Integer, Column, Boolean, DateTime, String, Union

# Core model base.
from app.database.core import Base


class Ad(Base):
    """Ad model"""

    __tablename__ = "ads"

    # Database.
    id = Column(Integer, primary_key=True, index=True, nullable=False)

    # Owner id.
    owner_id = Column(Integer, nullable=False)

    # States.
    is_active = Column(Boolean, nullable=False, default=True)
    is_verified = Column(Boolean, nullable=False, default=False)

    # Ad.
    type = Column(String(length=16), nullable=False)
    data = Column(String, nullable=False)

    # Times.
    time_created = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
    time_verified = Column(DateTime(timezone=True), nullable=True)
