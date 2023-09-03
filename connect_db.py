from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from config import get_connection_string

engine = create_engine(get_connection_string())
Session = sessionmaker(bind=engine)
session = Session()