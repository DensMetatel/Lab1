class Playlist:
    def __init__(self, playlist_id, name):
        self.playlist_id = playlist_id
        self.name = name
        self.tracks = []

    def add_track(self, track):
        self.tracks.append(track)