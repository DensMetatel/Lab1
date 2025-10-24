from Class.Exceptions import WrongArtist, TrackExists, CreateError


class Album:
    def __init__(self, album_id: int, title: str, artist, year: int):
        if not title:
            title = 'Без названия'
        if year < 0:
            raise CreateError('Год создания не может быть отрицательным')
        self.album_id = album_id
        self.title = title
        self.artist = artist
        self.year = year
        self.tracks = []

    def add_track(self, track):
        if track.artist != self.artist:
            raise WrongArtist('Это трек другого артиста')
        if track in self.tracks:
            raise TrackExists("Такой трек уже есть в альбоме")
        self.tracks.append(track)

    def show_tracks(self):
        print(f'Альбом: {self.title}')
        if not self.tracks:
            print("  (пока пуст)")
        for i, track in enumerate(self.tracks, 1):
            print(f"  {i}. {track}")

    def __str__(self):
        return f'Альбом: {self.title} {self.year} (треков: {len(self.tracks)})'