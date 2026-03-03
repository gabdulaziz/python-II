## `Playlist`

A full-featured playlist with dunder methods everywhere.

- `__init__(self, name)` → empty list `songs` (each song is a dict with `"title"` and `"duration"` in seconds)
- `add(title, duration)`
- `__len__` → number of songs
- `__contains__(title)` → is a song with that title in the playlist
- `__getitem__(index)` → returns the song at that index
- `__add__` → merges two playlists into a new one called `"name1 + name2"`
- `__eq__` → same songs in same order
- `__str__` → formatted list with total duration in `MM:SS`

```python
rock = Playlist("Rock")
rock.add("Bohemian Rhapsody", 354)
rock.add("Stairway to Heaven", 482)

pop = Playlist("Pop")
pop.add("Blinding Lights", 200)

print(len(rock))                    # 2
print("Bohemian Rhapsody" in rock)  # True
print(rock[0])                      # {'title': 'Bohemian Rhapsody', 'duration': 354}

merged = rock + pop
print(len(merged))                  # 3
print(merged)
# 🎧 Rock + Pop (3 songs, 17:16)
#  1. Bohemian Rhapsody (5:54)
#  2. Stairway to Heaven (8:02)
#  3. Blinding Lights (3:20)
```

```python
class Playlist:
     def __init__(self, name):
        self.name = name
        self.songs = []

    def add(self, title, duration):
        pass

    def __len__(self):
        pass

    def __contains__(self, title):
        pass

    def __getitem__(self, index):
        pass

    def __add__(self, other):
        new = Playlist(f"{self.name} + {other.name}")
        new.songs = self.songs + other.songs
        return new

    def __eq__(self, other):
        pass

    @staticmethod
    def _fmt(seconds):
        return f"{seconds // 60}:{seconds % 60:02d}"

    def __str__(self):
        total = sum(s["duration"] for s in self.songs)
        lines = [f"🎧 {self.name} ({len(self)} songs, {self._fmt(total)})"]
        for i, s in enumerate(self.songs, 1):
            lines.append(f"  {i}. {s['title']} ({self._fmt(s['duration'])})")
        return "\n".join(lines)

```