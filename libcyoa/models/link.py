from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from libcyoa.db.base_class import Base


class Link(Base):
    id = Column(Integer, primary_key=True, index=True)  # 2
    url = Column(String(256), index=True)
    title = Column(String(256), nullable=True)
    host = Column(String(256), nullable=True)
    submitter_id = Column(String(10), ForeignKey("user.id"), nullable=True)
    submitter = relationship("User", back_populates="links")