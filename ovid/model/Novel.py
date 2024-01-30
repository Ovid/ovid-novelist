from ovid.model.Chapter import Chapter


class Novel:
    def __init__(self, title=None, filename=None, genre=None, chapters=None) -> None:
        self.title = title
        self.genre = genre
        if chapters is None:
            chapters = []
        self.chapters = chapters
        self.filename = filename
        self.currentChapter = None

    def set_current_chapter(self, chapter: Chapter) -> None:
        self.currentChapter = chapter

    def add_chapter(self, chapter: Chapter) -> Chapter:
        previous_chapter = self.chapters[-1] if self.chapters else None
        chapter.previous_chapter = previous_chapter if previous_chapter else None
        if previous_chapter:
            previous_chapter.next_chapter = chapter
        self.chapters.append(chapter)
        return chapter

    def delete_chapter(self, chapter):
        if chapter in self.chapters:
            index = self.chapters.index(chapter)
            if chapter.previous_chapter:
                chapter.previous_chapter.next_chapter = chapter
            if chapter.next_chapter:
                chapter.next_chapter.previous_chapter = chapter.previous_chapter
            self.chapters.remove(chapter)

    def clear_chapters(self) -> None:
        self.chapters = []

    def get_chapters(self):
        return self.chapters

    def hasNoChapters(self):
        return len(self.chapters) == 0
