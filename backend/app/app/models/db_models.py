from sqlalchemy import Boolean, Column, Integer, String, Text
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Date, DateTime
from datetime import datetime
from app.db.base_class import Base


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    phone_number = Column(String, unique=True, index=True, nullable=False)
    date_of_birth = Column(Date)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    created_at = Column(DateTime, default=datetime.utcnow())
    modified_at = Column(DateTime, default=datetime.utcnow(),
                         onupdate=datetime.utcnow())


class Bible_Book(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True)
    slug = Column(String, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow())


class Bible_Chapter(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    book_id = Column(Integer, ForeignKey(Bible_Book.id))
    created_at = Column(DateTime, default=datetime.utcnow())


class Bible_Verse(Base):
    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey(Bible_Book.id), index=True)
    chapter_id = Column(Integer, ForeignKey(Bible_Chapter.id), index=True)
    verse_number = Column(Integer, index=True)
    text = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow())
