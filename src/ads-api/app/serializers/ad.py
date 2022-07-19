import time

from app.database.models.ad import Ad


def serialize(ad: Ad, in_list: bool = False) -> dict:
    """Returns dict object for API response with serialized Ad data."""

    serialized_ad = {
        "id": ad.id,
        "states": {
            "is_active": ad.is_active,
            "is_verified": ad.is_verified,
        },
        "display": {"type": "text", "data": ad.text},
        "created_at": time.mktime(ad.time_created.timetuple()),
    }

    if in_list:
        return serialized_ad

    return {"ad": serialized_ad}


serialize_ad = serialize
