from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from libcyoa.db.base_class import Base

class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(256), index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    email = Column(String, nullable=True)
    is_superuser = Column(Boolean, default=False)
    links = relationship(
        "Link",
        cascade="all,delete-orphan",
        back_populates="submitter",
        uselist=True,
    )