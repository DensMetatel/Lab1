class Album:
    def __init__(self, album_id: int, title: str, artist, year: int):
        self.album_id = album_id
        self.title = title
        self.artist = artist
        self.year = year
        self.tracks = []

    def add_track(self, track):
        if track.artist == self.artist:
            self.tracks.append(track)
        else:
            print('Это трек другого артиста!')

    def __str__(self):
        return f'Альбом: {self.title} ({self.year})'