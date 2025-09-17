import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student


DB_URL = "postgresql://postgres:123@localhost:5432/postgres"


@pytest.fixture(scope="function")
def db_session():
    """Создает сессию для тестов и очищает данные после теста"""
    engine = create_engine(DB_URL)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    yield session

    # Очистка после теста
    session.query(Student).delete()
    session.commit()
    session.close()
    Base.metadata.drop_all(engine)