from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean
from datetime import datetime

class Vehicle:
    __tablename__ = 'vehicles'

    id = Column(Integer, primary_key=True)
    license_plate = Column(String(20), unique=True, nullable=False)
    brand = Column(String(50), nullable=False)
    model = Column(String(50), nullable=False)
    year = Column(Integer, nullable=False)
    category = Column(String(50), nullable=False)
    daily_rate = Column(Float, nullable=False)
    status = Column(String(20), default='available')
    color = Column(String(30), nullable=False)
    fuel_type = Column(String(20), nullable=False)
    transmission = Column(String(20), nullable=False)
    mileage = Column(Float, nullable=False)
    registration_date = Column(DateTime, default=datetime.utcnow)
    last_maintenance = Column(DateTime)
    is_available = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)