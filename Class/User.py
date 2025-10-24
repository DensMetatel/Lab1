from Class.Playlist import Playlist


class User:
    def __init__(self, user_id: int, username: str):
        if not username:
            username = 'Неизвестный'
        self.user_id = user_id
        self.username = username
        self.playlists = []

    def create_playlist(self, playlist_id: int, name: str):
        if not name:
            name = 'Без названия'
        playlist = Playlist(playlist_id, name, self)
        self.playlists.append(playlist)
        return playlist

    def show_playlists(self):
        print(f'Плейлисты пользователя {self.username}:')
        if not self.playlists:
            print("  (пока нет плейлистов)")
        for pl in self.playlists:
            print("  ", pl)

    def __str__(self):
        return f'Пользователь: {self.username}'