from sqlalchemy.orm import Session
from .models import Address
from .schemas import AddressCreate
import math

def create_address(db: Session, address: AddressCreate):
    new_address = Address(**address.dict())
    db.add(new_address)
    db.commit()
    db.refresh(new_address)
    return new_address

def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371  # Earth radius in KM
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)

    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2

    return 2 * R * math.asin(math.sqrt(a))

def get_addresses_within_distance(db: Session, lat, lon, distance):
    addresses = db.query(Address).all()
    result = []

    for addr in addresses:
        dist = calculate_distance(lat, lon, addr.latitude, addr.longitude)
        if dist <= distance:
            result.append(addr)

    return result

def update_address(db: Session, address_id: int, address_data: AddressCreate):
    address = db.query(Address).filter(Address.id == address_id).first()
    if not address:
        return None

    address.name = address_data.name
    address.latitude = address_data.latitude
    address.longitude = address_data.longitude

    db.commit()
    db.refresh(address)
    return address

def delete_address(db: Session, address_id: int):
    address = db.query(Address).filter(Address.id == address_id).first()
    if not address:
        return False

    db.delete(address)
    db.commit()
    return True
