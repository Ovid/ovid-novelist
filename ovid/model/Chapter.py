class Chapter:
    def __init__(self, title, previous_chapter=None, next_chapter=None, contents=None):
        self.title = title
        self.previous_chapter = previous_chapter
        self.next_chapter = next_chapter
        self.contents = contents
