from PyQt6.QtWidgets import QListWidget

class OvidOutlineWidget(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

    def setNovel(self, novel):
        self.clear()
        for chapter in novel.chapters:
            self.addAction(novel.get_outline(chapter))
