from sqlalchemy import Column, ForeignKey, Integer, String, Uuid
from sqlalchemy.orm import DeclarativeBase, relationship

from libcyoa.db.base_class import Base


class Hash(Base):
    """A hash of an image."""
    __tablename__ = "hash"

    # Required parameters
    id = Column(Integer, primary_key=True, index=True)
    hash = Column(String(256), index=True)

    # Relationships
    images = relationship(
        "Image",
        cascade="all,delete-orphan",
        back_populates="hash",
        uselist=True,
    )
