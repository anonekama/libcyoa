from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Uuid
from sqlalchemy.orm import DeclarativeBase, relationship

from libcyoa.db.base_class import Base


class Title(Base):
    """A CYOA title."""
    __tablename__ = "title"

    # Required parameters
    id = Column(Integer, primary_key=True, index=True)
    title_name = Column(String(256), index=True)

    # Relationships
    cyoa_id = Column(Uuid, ForeignKey("cyoa.id"))
    cyoa = relationship("Cyoa")

class TitleReversion(Base):
    """Reversion history of Title."""
    __tablename__ = "titlereversion"

    # Required parameters
    id = Column(Integer, primary_key=True, index=True)
    reversion_type = Column(String(256))  # (e.g. create, update, restore)
    is_current = Column(Boolean)
    timestamp = Column(DateTime)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User")
    title_id = Column(Integer, ForeignKey("title.id"))
    title = relationship("Title")

    # Tracked data
    title_name = Column(String(256), nullable=True)
