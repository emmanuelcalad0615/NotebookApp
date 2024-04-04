from datetime import datetime
from dataclasses import dataclass, field


@dataclass
class Note:
    code: int
    title: str
    text: str
    importance: str
    creation_date: datetime = field(default_factory=datetime.now)
    tags: list[str] = field(default_factory=list[str])

    def __str__(self):
        return f"Code: {self.code}" \
               f"Creation date: {self.creation_date}" \
               f"Title: {self.text}"

    def add_tag(self, tag):
        if tag not in self.tags:
            self.tags.append(tag)


class Notebook:
    def __init__(self, notes: list[Note]):
        self.notes: list[Note] = notes

    def add_note(self, title: str, text: str, importance: str):
        code_id: int = len(self.notes)
        nota: Note = Note(code_id, title, text, importance)
        self.notes.append(nota)

    def important_notes(self) -> list[Note]:
        important_list: list[Note] = [important for important in self.notes if
                                      important.importance == "HIGH" or important.importance == "MEDIUM"]
        return important_list

    def tags_note_count(self) -> dict[str, int]:
        tags_count: dict[str, int] = {}
        for note in self.notes:
            for tag in note.tags:
                if tag in tags_count:
                    tags_count[tag] += 1
                else:
                    tags_count[tag] = 1
        return tags_count
