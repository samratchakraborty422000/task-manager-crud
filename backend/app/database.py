from sqlalchemy import create_engine
from sqlalchemy import sessionmaker, DeclarativeBase

DATABASE_URL = "sqlite:///./tasks.db"

connect_args = {
    "check_same_thread": False
}

engine = create_engine(
    DATABASE_URL,
    connect_args=connect_args
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for database models
class Base(DeclarativeBase):
    pass

# Database dependency
def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


