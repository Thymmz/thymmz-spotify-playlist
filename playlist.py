class Playlist:
    
    def __init__(self, name, id) -> None:
        self.name = name
        self.id = id

    def __str__(self) -> str:
        return f"Playlist:{self.name}"