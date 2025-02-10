import pytest
from datetime import datetime
from db.database import get_session, engine, create_db_and_tables  
from db.emails import Email, User, Company, Status
from sqlmodel import SQLModel

@pytest.fixture(scope="function")
def db_session():
    """Creates a fresh database session for each test."""
    create_db_and_tables()

    session = get_session()
    yield session  
    session.close()  

@pytest.fixture
def new_email():
    """Fixture to create a new email instance for testing."""
    return Email(
        email_subject="Test Subject",
        from_email="test@example.com",
        company_id=1,
        received_at=datetime.now(),
        user_id=1,
        status_id=1,
    )

def test_create_email(db_session, new_email):
    """Test inserting and querying an email record."""

    user = User(id=1, name="Test User")
    company = Company(id=1, name="Test Company")
    status = Status(id=1, description="Pending")

    db_session.add_all([user, company, status])  
    db_session.commit()
 
    db_session.add(new_email)
    db_session.commit()

    queried_email = db_session.query(Email).filter_by(email_subject="Test Subject").first()

    assert queried_email is not None, "Email was not found in the database."
    assert queried_email.email_subject == "Test Subject"
    assert queried_email.from_email == "test@example.com"