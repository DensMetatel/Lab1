import json
from Class.Artist import Artist


def save_to_json(artists: list[Artist], filename: str = "Json/information_artist.json"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            existing_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        existing_data = []

    existing_by_id = {a["artist_id"]: a for a in existing_data}

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
                            "duration": track.duration,
                            "year": track.year
                        }
                        for track in album.tracks
                    ]
                }
                for album in artist.albums
            ],
            "tracks": [
                {
                    "track_id": track.track_id,
                    "title": track.title,
                    "genre": track.genre,
                    "duration": track.duration,
                    "year": track.year
                }
                for track in artist.tracks
                if all(track not in album.tracks for album in artist.albums)
            ]
        }

        existing_by_id[artist.artist_id] = artist_data

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(list(existing_by_id.values()), file, ensure_ascii=False, indent=4)

    print(f"Данные обновлены в '{filename}'")


def load_from_json(filename: str = "Json/information_artist.json"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print(f"'{filename}' не найден или повреждён.")
        return []

    artists = []
    for artist_data in data:
        artist = Artist(artist_data["artist_id"], artist_data["name"])

        for album_data in artist_data.get("albums", []):
            album = artist.create_album(album_data["album_id"], album_data["title"], album_data["year"])
            for track_data in album_data.get("tracks", []):
                track = artist.create_track(
                    int(track_data["track_id"]),
                    track_data["title"],
                    track_data["genre"],
                    int(track_data["duration"]),
                    int(track_data.get("year", 0))
                )
                album.add_track(track)

        for track_data in artist_data.get("tracks", []):
            artist.create_track(
                int(track_data["track_id"]),
                track_data["title"],
                track_data["genre"],
                int(track_data["duration"]),
                int(track_data.get("year", 0))
            )

        artists.append(artist)

    print(f"Данные загружены из '{filename}'")
    return artists

