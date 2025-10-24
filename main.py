from Class.Artist import Artist
from Class.User import User
from Class.Exceptions import CreateError, WrongArtist, TrackExists
from Json.WriteReadJson import save_to_json, load_from_json


def main():
    artist1 = None
    artist2 = None

    try:
        loaded_data = load_from_json()
        if loaded_data:
            print("\nДанные из JSON:")
            for artist in loaded_data:
                print(f"- {artist['name']} ({len(artist['albums'])} альбомов)")

        artist1 = Artist(1, 'Григорий Лепс')
        album1 = artist1.create_album(1, 'Ты чего такой серьёзный', 2017)

        track1 = artist1.create_track(1, 'Аминь', 'Rock', 242)
        track2 = artist1.create_track(2, 'Что ж ты натворила', 'Rock', 215)

        album1.add_track(track1)
        album1.add_track(track2)
        album1.show_tracks()

        user1 = User(1, 'Александр')
        playlist1 = user1.create_playlist(1, 'Песни Лепса')

        playlist1.add_track(track1)
        playlist1.add_track(track2)

        user1.show_playlists()
        playlist1.show_tracks()

        artist2 = Artist(2, 'Любэ')
        wrong_track = artist2.create_track(3, 'Солдат', 'Rock', 306)
        album1.add_track(wrong_track)

    except (CreateError, WrongArtist, TrackExists) as error:
        print(f'\nОшибка: {error}')

    finally:
        artists_to_save = [a for a in (artist1, artist2) if a is not None]
        if artists_to_save:
            save_to_json(artists_to_save)


if __name__ == '__main__':
    main()
