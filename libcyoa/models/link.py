from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from libcyoa.db.base_class import Base


class Link(Base):
    """A link to a CYOA resource (e.g. imgchest, neocities)."""
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String(256), index=True)
    title = Column(String(256), nullable=True)
    host = Column(String(256), nullable=True)
    # Date published
    # Version
    # Part
    # Status (WIP, complete)
    # Media (image, interactive, text)

    # Images = relationship
    # Page_count
    # Word_count
    # Pixel_count
    # Full_text
    # Keybert_keywords

    # isCurrent
    # isBroken
    # isParsed

    submitter_id = Column(Integer, ForeignKey("user.id"), nullable=True)
    submitter = relationship("User")

class LinkHistory(Base):
    """Reversion history of Link."""
    id = Column(Integer, primary_key=True, index=True)
    link_id = Column(Integer, ForeignKey("link.id"))
