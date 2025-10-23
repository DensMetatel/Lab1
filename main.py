from Class.Artist import Artist
from Class.Track import Track
from Class.User import User

# создаём артиста и треки
artist = Artist(1, "Григорий Лепс")
track1 = artist.create_track(1, "Аминь", "Rock", 242)
track2 = artist.create_track(2, "Что ж ты натворила",  "Rock", 215)

# создаём пользователя и плейлист
user = User(1, "Denil")
playlist = user.create_playlist(1, "Лепс")

playlist.add_track(track1)
playlist.add_track(track2)
playlist.show_tracks()

user.show_playlists()

