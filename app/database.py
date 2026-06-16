from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# This creates a local file named 'loonlet_auth.db' in your project
SQLALCHEMY_DATABASE_URL = "sqlite:///./loonlet_auth.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Helper dependency to get a database session for our API routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()