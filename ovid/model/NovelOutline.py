class NovelOutline:
    def __init__(self, novel):
        self.novel = novel
        self.outline = {chapter.get_uuid(): None for chapter in novel.get_chapters()}

    def add_section(self, chapter, section):
        chapter_uuid = chapter.get_uuid()
        self.outline[chapter_uuid] = section

    def remove_section(self, chapter, section):
        chapter_uuid = chapter.get_uuid()
        if chapter_uuid in self.outline:
            del self.outline[chapter_uuid]

    def get_section(self, chapter):
        return self.outline.get(chapter.get_uuid(), None)

    def sync_with_novel(self):
        # Remove outline entries for chapters that have been deleted
        for chapter_uuid in list(self.outline.keys()):
            if chapter_uuid not in self.novel.chapters:
                del self.outline[chapter_uuid]

        # Add outline entries for new chapters
        for chapter_uuid in self.novel.chapters:
            if chapter_uuid not in self.outline:
                self.outline[chapter_uuid] = None
