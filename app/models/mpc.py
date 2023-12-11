from ..database.database import Base
from sqlalchemy import String, Column, DateTime, Integer, ForeignKey, LargeBinary
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

class MpcSystem(Base):
    __tablename__ = "mpc_systems"
    id = Column(String, primary_key=True, index=True)
    number_owners = Column(Integer)
    number_data_received = Column(Integer, server_default="0")
    public_key = Column(LargeBinary)
    relin_key = Column(LargeBinary)
    rotate_key = Column(LargeBinary)
    context = Column(LargeBinary)
    result = Column(LargeBinary)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

class MpcData(Base):
    __tablename__ = "mpc_data"
    mpc_system_id = Column(String, ForeignKey("mpc_systems.id"), primary_key=True, index=True)
    data_owner_id = Column(String, primary_key=True)
    time_data_sent = Column(DateTime(timezone=True), server_default=func.now())

