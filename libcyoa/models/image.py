from sqlalchemy import Column, ForeignKey, Integer, String, Uuid
from sqlalchemy.orm import DeclarativeBase, relationship


class Image(DeclarativeBase):
    """An image in a CYOA link."""
    __tablename__ = "image"

    # Required parameters
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String(2048), index=True)
    index = Column(Integer)

    # Computed parameters
    width = Column(Integer, nullable=True)
    height = Column(Integer, nullable=True)

    # Relationships
    link_id = Column(Uuid, ForeignKey("link.id"))
    link = relationship("Link")
    hash_id = Column(Integer, ForeignKey("hash.id"))
    hash = relationship("Hash")
