from .database import DatabaseConnector


def test_connection():
    assert DatabaseConnector.connection is None
    DatabaseConnector.connect()
    assert DatabaseConnector.connection is not None
