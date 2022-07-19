"""
    Ad CRUD utils for the database.
"""

# Libraries.
from sqlalchemy.orm import Session
from sqlalchemy.sql import func

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


def get_random(db: Session) -> Ad:
    return (
        db.query(Ad)
        .filter(Ad.is_active == True)
        .order_by(func.random())
        .limit(1)
        .first()
    )


def create(db: Session, owner_id: int, ad_type: str, ad_data: str, ad_link: str) -> Ad:
    """Creates Ad"""

    # Create new Ad.
    oauth_client = Ad(type=ad_type, data=ad_data, link=ad_link, owner_id=owner_id)

    # Apply OAuth client in database.
    db.add(oauth_client)
    db.commit()
    db.refresh(oauth_client)

    return oauth_client
