class Album:
    def __init__(self, album_id: int, title: str, artist: str, year: int):
        self.album_id = album_id
        self.title = title
        self.artist = artist
        self.year = year
        self.tracks = []

    def add_track(self, track: str):
        self.tracks.append(track)