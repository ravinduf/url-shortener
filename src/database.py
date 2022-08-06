from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import get_settings

# check same thread false allows more than one request at a time to
# communicate with database
engine = create_engine(
    get_settings().db_url, connect_args={"check_same_thread": False}
)


SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)

Base = declarative_base() # connects database engine to SQLAlchemy functionality
                        # of the models
                        

