from typing import Dict
from .interfaces.database_repository import DatabaseRepositoryInterface
from .database import DatabaseConnector


class DatabaseRepository(DatabaseRepositoryInterface):

    def insert_artist(self, data: Dict) -> None:
        query = '''
            INSERT INTO artists
                (first_name, second_name, surname, artist_id, link, extraction_date)
            VALUES
                (%s, %s, %s, %s, %s, %s)
        '''

        cursor = DatabaseConnector.connection.cursor()
        cursor.execute(query, list(data.values()))

        DatabaseConnector.connection.commit()
