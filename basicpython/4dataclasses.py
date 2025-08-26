from dataclasses import dataclass
from datetime import datetime

@dataclass
class Note:
    id: int
    title: str
    content: str
    created_at: datetime

n = Note(1, "My First Note", "This is the content of my first note.", datetime.now())
print(n.created_at)