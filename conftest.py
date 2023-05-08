import pytest
from app import app

@pytest.fixture(scope='session')
def client():
    """
    Fixture que cria um cliente de teste para o Flask
    """
    with app.test_client() as client:
        yield client
  