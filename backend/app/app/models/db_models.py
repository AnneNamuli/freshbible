from sqlalchemy import Boolean, Column, Integer, String, Text, LargeBinary
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
    title = Column(String, index=True)
    book_id = Column(Integer, ForeignKey(Bible_Book.id))
    created_at = Column(DateTime, default=datetime.utcnow())


class Bible_Verse(Base):
    id = Column(Integer, primary_key=True, index=True)
    chapter_id = Column(Integer, ForeignKey(Bible_Chapter.id), index=True)
    chapter = Column(String, ForeignKey(Bible_Chapter.title), index=True)
    verse_number = Column(Integer, index=True)
    text = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow())


class Organization(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow())


class Organization_User(Base):
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(ForeignKey(User.id), index=True)
    organization_id = Column(ForeignKey(Organization.id), index=True)
    created_at = Column(DateTime, default=datetime.utcnow())


class Broadcast(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    subtitle = Column(String)
    thumbnail = Column(LargeBinary(length=(2**32)-1))
    text = Column(Text)
    scheduled_time = Column(DateTime)
    author_id = Column(ForeignKey(User.id), index=True)
    created_at = Column(DateTime, default=datetime.utcnow())


class Asset(Base):
    id = Column(Integer, primary_key=True, index=True)
    broadcast_id = Column(ForeignKey(Broadcast.id), index=True)
    status = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow())


class Broadcasts_Queue(Base):
    id = Column(Integer, primary_key=True, index=True)
    broadcast_id = Column(ForeignKey(Broadcast.id), index=True)
    scheduled_time = Column(DateTime)
    audience = Column(String)
    is_broadcast = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow())


class Broadcast_Stats(Base):
    id = Column(Integer, primary_key=True, index=True)
    broadcast_id = Column(ForeignKey(Broadcast.id), index=True)
    views = Column(Integer)
    likes = Column(Integer)
