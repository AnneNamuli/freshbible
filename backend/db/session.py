from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#from backend.core.config import settings

engine = create_engine(
    'postgresql://sxjzpybxpehuuy:218e99589d70810d3c3063781cf2763fae04c1b8e15535e277e4229a7a448964@ec2-34-204-127-36.compute-1.amazonaws.com:5432/d4pq8cteal1me7', pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
