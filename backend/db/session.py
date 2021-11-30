from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.core.config import settings

engine = create_engine(
    'postgresql://tnniqygzwuxlsc:f0677519ca90972524ed8695a26bbcec41e4e878d31111e4ace76240a90c0af5@ec2-3-209-38-221.compute-1.amazonaws.com:5432/d23pv8los6u5ft', pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
