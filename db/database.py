from sqlmodel import SQLModel, create_engine, Session
from db.emails import Email, User, Company, Status

DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    DATABASE_URL, 
    echo=True, 
    connect_args={"check_same_thread": False}  
)

def create_db_and_tables():
    SQLModel.metadata.drop_all(engine)  
    SQLModel.metadata.create_all(engine)  

def get_session():
    return Session(engine) 
