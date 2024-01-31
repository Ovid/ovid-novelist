import uuid


class Chapter:
    def __init__(self, title, previous_chapter=None, next_chapter=None, contents=None):
        self.title = title
        self._uuid = uuid.uuid4()
        self.previous_chapter = previous_chapter
        self.next_chapter = next_chapter
        self.contents = contents

    def get_uuid(self):
        return self._uuid

    def __str__(self):
        return self.title
