from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

ENGINE = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SESSION = sessionmaker(autocommit=False, autoflush=False, bind=ENGINE)

Base = declarative_base()

def get_db():
    db = SESSION()
    try:
        yield db
    finally:
        db.close()