class Artist:
    def __init__(self, artist_id: int, name: str, genre: str):
        self.artist_id = artist_id
        self.name = name
        self.genre = genre
        self.albums = []

    def add_album(self, album):
        self.albums.append(album)