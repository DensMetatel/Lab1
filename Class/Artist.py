from Class.Album import Album
from Class.Track import Track


class Artist:
    def __init__(self, artist_id: int, name: str):
        self.artist_id = artist_id
        self.name = name
        self.albums = []
        self.tracks = []

    def create_album(self, album_id: int, title: str, year: int):
        album = Album(album_id, title, self, year)
        self.albums.append(album)
        return album

    def create_track(self, track_id: int, title: str, genre: str, duration: int):
        track = Track(track_id, title, genre, duration, self)
        self.tracks.append(track)
        return track

    def __str__(self):
        return f'Артист: {self.name}'