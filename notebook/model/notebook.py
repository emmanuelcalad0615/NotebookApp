

from datetime import datetime
from dataclasses import dataclass, field
from typing import ClassVar


@dataclass
class Note:
    HIGH: ClassVar[str] = "HIGH"
    MEDIUM: ClassVar[str] = "MEDIUM"
    LOW: ClassVar[str] = "LOW"
    code: int
    title: str
    text: str
    importance: str
    creation_date: datetime = field(init= False, default_factory=datetime.now)
    tags: list[str] = field(init= False, default_factory= list[str])

    def __str__(self):
        return (f"Code: {self.code}\n"
                f"Creation date: {self.creation_date}\n"
                f"{self.title}: {self.text}\n")
    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)

class Notebook:
    def __init__(self):
        self.notes: dict[int, Note] = {}


    def add_note(self, title: str, text: str, importance: str) -> int:
        code: int = len(self.notes) +1
        note: Note = Note(code, title, text, importance)
        self.notes[code] = note
        return code

    def important_notes(self) -> list[Note]:
        important_notes: list[Note] = [important for important in self.notes.values() if important.importance == Note.HIGH or important.importance == Note.MEDIUM]
        return important_notes

    def tags_note_count(self) -> dict[str, int]:
        count_tags: dict[str, int] = {}
        for note in self.notes.values():
            for tag in note.tags:
                if tag in count_tags:
                    count_tags[tag] += 1
                else:
                    count_tags[tag] = 1
        return count_tags