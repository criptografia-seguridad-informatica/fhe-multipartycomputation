from ..database.database import Base
from sqlalchemy import String, Column, DateTime
from sqlalchemy.sql import func, relationship


class MpcSystem(Base):
    __tablename__ = "mpc_systems"
    id = Column(String, primary_key=True, index=True)
    number_owners = Column(Int)
    number_data_received = Column(Int, server_default=0)
    public_key = Column(String)
    relin_key = Column(String)
    rotate_key = Column(String)
    context = Column(String)
    result = Column(String)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

class MpcData(Base):
    __tablename__ = "mpc_data"
    mpc_system_id = Column(String, primary_key=True, ForeignKey("mpc_systems.id"), index=True)
    data_owner_id = Column(String, primary_key=True)
    time_data_sent = Column(DateTime(timezone=True), server_default=func.now())

    mpc_system = relationship("MpcSystem", back_populates="mpc_data")