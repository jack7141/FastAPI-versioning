from datetime import datetime

from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class HeaderBannerModel(Base):
    __tablename__ = "header_banners"

    id = Column(String, primary_key=True)
    display_start = Column(DateTime)
    display_end = Column(DateTime)
    banner_name = Column(String)
    banner_description = Column(String)
    background_color = Column(String)
    text_color = Column(String)
    redirection_path = Column(String)
    created_at = Column(DateTime(timezone=True), nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime(timezone=True), nullable=False, default=datetime.utcnow())
