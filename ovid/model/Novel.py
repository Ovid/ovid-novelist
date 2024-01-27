from ovid.model.Chapter import Chapter


class Novel:
    def __init__(self, title="Untitled", genre=None, chapters=None) -> None:
        self.title = title
        self.genre = genre
        if chapters is None:
            chapters = []
        self.chapters = chapters

    def add_chapter(self, title: str, contents=None) -> Chapter:
        previous_chapter = self.chapters[-1] if self.chapters else None
        new_chapter = Chapter(
            title, previous_chapter=previous_chapter, contents=contents
        )
        if previous_chapter:
            previous_chapter.next_chapter = new_chapter
        self.chapters.append(new_chapter)
        return new_chapter

    def delete_chapter(self, chapter):
        if chapter in self.chapters:
            index = self.chapters.index(chapter)
            if chapter.previous_chapter:
                chapter.previous_chapter.next_chapter = chapter.next_chapter
            if chapter.next_chapter:
                chapter.next_chapter.previous_chapter = chapter.previous_chapter
            self.chapters.remove(chapter)

    def get_chapters(self):
        return self.chapters
