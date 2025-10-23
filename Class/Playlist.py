class Playlist:
    def __init__(self, playlist_id: int, title: str, username):
        self.playlist_id = playlist_id
        self.title = title
        self.username = username
        self.tracks = []

    def add_track(self, track):
        if track not in self.tracks:
            self.tracks.append(track)
        else:
            print('Уже есть в плейлисте')

    def remote_track(self, track):
        if track in self.tracks:
            self.tracks.remove(track)
        else:
            print('Такого трека нет в плейлисте')

    def show_tracks(self):
        print(f'Плейлист: {self.title}')
        if not self.tracks:
            print("  (пока пуст)")
        for i, track in enumerate(self.tracks, 1):
            print(f"  {i}. {track}")

    def __str__(self):
        return f'Плейлист: {self.title} (треков: {len(self.tracks)})'