import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
from pathlib import Path

def create_db_session():

    BASE_DIR = Path(__file__).resolve().parent
    db_path = os.path.join(BASE_DIR, '..', 'database', 'earthquakes.db')
    engine = create_engine(f"sqlite:///{db_path}")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()

