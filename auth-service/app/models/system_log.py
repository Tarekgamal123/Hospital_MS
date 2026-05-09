from sqlalchemy import Column, String, Integer, BigInteger, Boolean, Text, DateTime, func
from app.core.database import Base

class SystemLog(Base):
    __tablename__ = "system_logs"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    service_name = Column(String(255), nullable=False)
    user_id = Column(Integer, nullable=True)
    user_role = Column(String(50), nullable=True)
    action = Column(String(255), nullable=False)
    resource_type = Column(String(255), nullable=True)
    resource_id = Column(String(255), nullable=True)
    method = Column(String(10), nullable=False)
    endpoint = Column(Text, nullable=False)
    ip_address = Column(String(50), nullable=True)
    user_agent = Column(Text, nullable=True)
    status_code = Column(Integer, nullable=False)
    details = Column(Text, nullable=True)
    success = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())