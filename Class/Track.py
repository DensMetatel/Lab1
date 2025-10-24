from Class.Exceptions import CreateError


class Track:
    def __init__(self, track_id: int, title: str, genre: str, duration: int, year: int, artist):
        if not title:
            title = "Без названия"
        if not year:
            year = 'Год выпуска неизвестен'
        if not genre:
            genre = "Неизвестный жанр"
        if not duration:
            duration = "Длительность не распознана"
        if duration < 0:
            raise CreateError('Длительность трека не может быть отрицательной')
        if year < 0:
            raise CreateError('Год выпуска трека не может быть отрицательной')
        if not artist:
            raise CreateError('Трек никому не принадлежит')
        self.track_id = track_id
        self.title = title
        self.genre = genre
        self.duration = duration
        self.year = year
        self.artist = artist

    def __str__(self):
        mi = self.duration // 60
        se = self.duration % 60
        return f'{self.title} — {self.artist.name} ({self.genre}, {mi}:{se:02d}) {self.year}'