import pytest
from ..stages.contracts.mocks.transform_contract import transform_contract_mock
from .database_repository import DatabaseRepository
from .database import DatabaseConnector

@pytest.mark.skip(reason="No need to insert data in data")
def test_insert_artist():
    DatabaseConnector.connect()
    database_repo = DatabaseRepository()
    data = transform_contract_mock.load_content[0]
    database_repo.insert_artist(data)
