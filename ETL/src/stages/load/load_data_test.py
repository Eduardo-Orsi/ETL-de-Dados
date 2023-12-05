#pylint: disable=broad-exception-caught
from ..contracts.mocks.transform_contract import transform_contract_mock
from ...infra.tests.database_repository import RepositorySpy
from ...errors.load_error import LoadError
from .load_data import LoadData

def test_load():
    db_repo = RepositorySpy()
    load_data = LoadData(db_repo)
    load_data.load(transform_contract_mock)
    assert db_repo.insert_artist_attributes == transform_contract_mock.load_content

def test_load_error():
    db_repo = RepositorySpy()
    load_data = LoadData(db_repo)
    try:
        load_data.load("error")
    except Exception as exception:
        assert isinstance(exception, LoadError)
