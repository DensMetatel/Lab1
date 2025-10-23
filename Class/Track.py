class Track:
    def __init__(self, track_id: int, title: str, genre: str, duration: int, artist):
        self.track_id = track_id
        self.title = title
        self.genre = genre
        self.duration = duration
        self.artist = artist

    def __str__(self):
        mi = self.duration // 60
        se = self.duration % 60
        return f'{self.title} — {self.artist.name} ({self.genre}, {mi}:{se:02d})'