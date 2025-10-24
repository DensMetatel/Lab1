from Class.Album import Album
from Class.Track import Track
from Class.Exceptions import CreateError


class Artist:
    def __init__(self, artist_id: int, name: str):
        if not name:
            name = 'Неизвестный'
        self.artist_id = artist_id
        self.name = name
        self.albums = []
        self.tracks = []

    def create_album(self, album_id: int, title: str, year: int):
        if not title:
            title = 'Без названия'
        if year < 0:
            raise CreateError('Год создания не может быть отрицательным')
        album = Album(album_id, title, self, year)
        self.albums.append(album)
        return album

    def create_track(self, track_id: int, title: str, genre: str, duration: int):
        if not title:
            title = 'Без названия'
        if not genre:
            genre = "Неизвестный жанр"
        if duration < 0:
            raise CreateError('Длительность не может быть отрицательной')
        track = Track(track_id, title, genre, duration, self)
        self.tracks.append(track)
        return track

    def show_albums(self):
        print(f"Альбомы артиста {self.name}:")
        if not self.albums:
            print("  (нет альбомов)")
        for album in self.albums:
            print("  ", album)

    def show_tracks(self):
        print(f"Треки артиста {self.name}:")
        if not self.tracks:
            print("  (нет треков)")
        for track in self.tracks:
            print("  ", track)

    def __str__(self):
        return f'Артист: {self.name}'