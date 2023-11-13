from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text, UnicodeText, Uuid
from sqlalchemy.orm import DeclarativeBase, relationship

from libcyoa.db.base_class import Base


class Link(Base):
    """A link to a CYOA resource (e.g. imgchest, neocities)."""
    __tablename__ = "link"

    # Required parameters
    id = Column(Uuid, primary_key=True, index=True)
    url = Column(String(2048), index=True)

    # Computed parameters
    title = Column(String(256), nullable=True)  # Link title
    host = Column(String(256), nullable=True)  # (e.g. imgchest, imgur, neocities)
    media = Column(String(256), nullable=True)  # (e.g. image, ICC, text)
    thumbnail = Column(String(256), nullable=True)
    date_published = Column(DateTime, nullable=True)

    # Optional parameters
    subtitle = Column(String(256), nullable=True)  # Abbreviated display title
    version = Column(String(256), nullable=True)
    part = Column(String(256), nullable=True)
    status = Column(String(256), nullable=True)  # (e.g. complete, WIP)
    type = Column(String(256), nullable=True)  # (e.g. OC, mod, DLC)

    # Relationships
    # Cyoa = relationship
    images = relationship(
        "Image",
        cascade="all,delete-orphan",
        back_populates="link",
        uselist=True,
    )
    reversions = relationship(
        "LinkReversion",
        cascade="all,delete-orphan",
        back_populates="link",
        uselist=True,
    )

    # Hidden parameters (do not track reversions)
    page_count = Column(Integer, nullable=True)
    word_count = Column(Integer, nullable=True)
    pixel_count = Column(Integer, nullable=True)
    full_text = Column(UnicodeText, nullable=True)
    keybert_keywords = Column(Text, nullable=True)
    deepdanbooru_keywords = Column(Text, nullable=True)
    parser_log = Column(Text, nullable=True)

    # Flags
    is_broken = Column(Boolean)  # Is it a broken link?
    is_deleted = Column(Boolean)
    is_hidden = Column(Boolean)  # Hide this link entirely?
    is_parsed = Column(Boolean)  # Has the daemon processed/computed this link?
    is_pinned = Column(Boolean)  # Is it considered a main link for a CYOA?


class LinkReversion(Base):
    """Reversion history of Link."""
    __tablename__ = "linkreversion"

    # Required parameters
    id = Column(Uuid, primary_key=True, index=True)
    reversion_type = Column(String(256))  # (e.g. create, update, restore)
    timestamp = Column(DateTime)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User")
    link_id = Column(Uuid, ForeignKey("link.id"))
    link = relationship("Link")
