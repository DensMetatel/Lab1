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

    def show_tracks(self):
        print(f'Альбом: {self.title}')
        if not self.tracks:
            print("  (пока пуст)")
        for i, track in enumerate(self.tracks, 1):
            print(f"  {i}. {track}")

    def __str__(self):
        return f'Альбом: {self.title} {self.year} (треков: {len(self.tracks)}))'