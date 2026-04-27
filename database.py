from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Database_Url='postgresql://postgres:admin@localhost:5432/fluttermusicapp'

engine=create_engine(Database_Url)

SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

db=SessionLocal()