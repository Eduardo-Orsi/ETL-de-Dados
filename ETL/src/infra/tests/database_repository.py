

class RepositorySpy:

    def __init__(self) -> None:
        self.insert_artist_attributes = []

    def insert_artist(self, data) -> None:
        self.insert_artist_attributes.append(data)
