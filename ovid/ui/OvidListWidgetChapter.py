from PyQt6.QtWidgets import QListWidgetItem

class OvidListWidgetChapter(QListWidgetItem):
    def __init__(self, chapter, parent=None) -> None:
        super().__init__(chapter.title, parent)
        self.chapter = chapter
