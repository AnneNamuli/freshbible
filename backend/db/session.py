from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine(
    'postgresql://kchjyvdochyvpm:7ee4d5c0c2c38c8d81736130750edf32f335e47e3f8c467ffe982f093a45f738@ec2-107-23-213-65.compute-1.amazonaws.com:5432/d4019b51ju20a2'
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
