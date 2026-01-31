from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from .database import Base, engine, SessionLocal
from .schemas import AddressCreate, AddressResponse
from .crud import (
    create_address,
    get_addresses_within_distance,
    update_address,
    delete_address
)


# Create database tables
Base.metadata.create_all(bind=engine)

#starts FASTAPI
app = FastAPI(title="Address Book API")

# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create Address API
@app.post("/addresses", response_model=AddressResponse)
def add_address(address: AddressCreate, db: Session = Depends(get_db)):
    return create_address(db, address)

# Get Nearby Addresses API
@app.get("/addresses/nearby")
def nearby_addresses(
    lat: float,
    lon: float,
    distance: float,
    db: Session = Depends(get_db)
):
    return get_addresses_within_distance(db, lat, lon, distance)

#updating addresses
@app.put("/addresses/{address_id}", response_model=AddressResponse)
def update_address_api(
    address_id: int,
    address: AddressCreate,
    db: Session = Depends(get_db)
):
    updated = update_address(db, address_id, address)
    if not updated:
        return {"error": "Address not found"}
    return updated

#deleting addresses
@app.delete("/addresses/{address_id}")
def delete_address_api(address_id: int, db: Session = Depends(get_db)):
    deleted = delete_address(db, address_id)
    if not deleted:
        return {"error": "Address not found"}
    return {"message": "Address deleted successfully"}


