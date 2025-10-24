from Class.Artist import Artist
from Class.User import User
from Class.Exceptions import CreateError, WrongArtist, TrackExists
from Json.WriteReadJson import save_to_json, load_from_json


def main():
    try:
        artists = load_from_json()
        print("Артисты, загруженные из JSON:")
        if not artists:
            print("(Файл пуст или отсутствует)")
        else:
            for artist in artists:
                print(f"- {artist.name} ({len(artist.albums)} альбомов), ({len(artist.tracks)} треков)")

        artist1 = Artist(2, 'Григорий Лепс')
        album1 = artist1.create_album(1, 'Ты чего такой серьёзный', 2017)

        track1 = artist1.create_track(1, 'Аминь', 'Rock', 242, 2017)
        track2 = artist1.create_track(2, 'Что ж ты натворила', 'Rock', 215, 2017)

        album1.add_track(track1)
        album1.add_track(track2)
        album1.show_tracks()

        user1 = User(1, 'Александр')
        playlist1 = user1.create_playlist(1, 'Песни Лепса')

        playlist1.add_track(track1)
        playlist1.add_track(track2)

        user1.show_playlists()
        playlist1.show_tracks()

        artist2 = Artist(3, 'Любэ')
        artist2.create_track(1, 'Солдат', 'Русская эстрада',306,2012)
        artists.append(artist1)
        artists.append(artist2)

        save_to_json(artists)

    except (CreateError, WrongArtist, TrackExists) as error:
        print(f'Ошибка: {error}')


if __name__ == '__main__':
    main()
