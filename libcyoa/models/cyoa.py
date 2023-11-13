from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text, UnicodeText, Uuid
from sqlalchemy.orm import DeclarativeBase, relationship

from libcyoa.db.base_class import Base


class Cyoa(Base):
    """A CYOA entry."""
    __tablename__ = "cyoa"

    # Required parameters
    id = Column(Uuid, primary_key=True, index=True)
    primary_title = Column(String(256), index=True)
    primary_author = Column(String(256))


    # Optional parameters
    summary = Column(Text, nullable=True)

    # Relationship
    titles = relationship(
        "Title",
        cascade="all,delete-orphan",
        back_populates="link",
        uselist=True,
    )
    # author (multiple)
    # tag (multiple)