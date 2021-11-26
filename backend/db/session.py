from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.core.config import settings

engine = create_engine(
    'postgres://ajwxdwkkfxevyz:bb8cce02280090a8f1ad70d0f84447be1624eed4d109a5b3d78461deb3b12f62@ec2-50-16-241-192.compute-1.amazonaws.com:5432/dd3l6uitsvdd3t', pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
