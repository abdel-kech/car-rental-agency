from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Payment(Base):
    __tablename__ = 'payments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    reservation_id = Column(Integer, ForeignKey('reservations.id'), nullable=False)
    amount = Column(Float, nullable=False)
    payment_date = Column(DateTime, nullable=False)
    payment_method = Column(String(50), nullable=False)
    status = Column(String(20), nullable=False)
    transaction_id = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime, default='2026-02-12 13:01:40')
    updated_at = Column(DateTime, default='2026-02-12 13:01:40', onupdate='2026-02-12 13:01:40')

    reservation = relationship('Reservation', back_populates='payments')