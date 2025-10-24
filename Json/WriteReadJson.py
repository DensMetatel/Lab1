import json
from Class.Artist import Artist


def save_to_json(artists: list[Artist], filename: str = "information_artist.json"):
    data = []
    for artist in artists:
        artist_data = {
            "artist_id": artist.artist_id,
            "name": artist.name,
            "albums": [
                {
                    "album_id": album.album_id,
                    "title": album.title,
                    "year": album.year,
                    "tracks": [
                        {
                            "track_id": track.track_id,
                            "title": track.title,
                            "genre": track.genre,
                            "duration": track.duration
                        }
                        for track in album.tracks
                    ]
                }
                for album in artist.albums
            ]
        }
        data.append(artist_data)

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    print(f"Данные сохранены в '{filename}'")


def load_from_json(filename: str = "information_artist.json"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
        print(f"Данные загружены из '{filename}'")
        return data
    except FileNotFoundError:
        print(f"Файла '{filename}' нет.")
        return []
    except json.JSONDecodeError:
        print(f"Ошибка чтения JSON-файла '{filename}'")
        return []
