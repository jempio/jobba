from sqlmodel import SQLModel, Field
from datetime import datetime

class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str

class Company(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str

class Status(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    description: str

class Email(SQLModel, table=True):
    email_id: int = Field(default=None, primary_key=True)
    email_subject: str
    from_email: str
    company_id: int = Field(foreign_key="company.id")  
    received_at: datetime
    user_id: int = Field(foreign_key="user.id") 
    status_id: int = Field(foreign_key="status.id")  