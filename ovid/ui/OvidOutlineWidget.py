from PyQt6.QtWidgets import QListWidget, QListWidgetItem, QTextEdit

class OvidOutlineWidget(QListWidget):
    def __init__(self, parent):
        super().__init__(parent)

    def setNovel(self, novel):
        self.clear()
        for chapter in novel.get_chapters():
            item = QListWidgetItem(chapter.title)
            self.addItem(item)

            text_edit = QTextEdit()
            text_edit.setText(novel.get_outline(chapter))
            text_edit.textChanged.connect(lambda: self.saveOutline(novel, chapter, text_edit))

            self.setItemWidget(item, text_edit)

            # Set the size hint of the item to the size hint of the text edit
            item.setSizeHint(text_edit.sizeHint())

    def saveOutline(self, novel, chapter, text_edit):
        novel.add_outline(chapter, text_edit.toPlainText())
