"""
    Ad CRUD utils for the database.
"""

# Libraries.
import secrets
from sqlalchemy.orm import Session

# Services.
from app.database.models.ad import Ad



def get_by_id(db: Session, ad_id: int) -> Ad:
    """Returns ad by it`s ID."""
    return db.query(Ad).filter(Ad.id == ad_id).first()


def get_by_owner_id(db: Session, owner_id: int) -> list[Ad]:
    """Returns ads by it`s owner ID."""
    return db.query(Ad).filter(Ad.owner_id == owner_id).all()


def get_count_by_owner_id(db: Session, owner_id: int) -> int:
    """Returns count of clients by it`s owner ID."""
    return db.query(Ad).filter(Ad.owner_id == owner_id).count()


def create(db: Session, owner_id: int, text: str) -> Ad:
    """Creates Ad"""

    # Create new Ad.
    oauth_client = Ad(
        text=text, owner_id=owner_id
    )

    # Apply OAuth client in database.
    db.add(oauth_client)
    db.commit()
    db.refresh(oauth_client)

    return oauth_client
