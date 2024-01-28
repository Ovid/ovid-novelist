import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QInputDialog,
)
from PyQt6.QtCore import Qt
from ovid.ui.OvidFont import OvidFont
from ovid.ui.OvidMenuBar import OvidMenuBar
from ovid.ui.OvidToolBar import OvidToolBar
from ovid.ui.OvidDockWidget import OvidDockWidget
from ovid.ui.OvidTextEdit import OvidTextEdit
from ovid.ui.OvidShortCuts import add_shortcuts
from ovid.ui.OvidListWidgetChapter import OvidListWidgetChapter

from ovid.model.Novel import Novel
from ovid.model.Chapter import Chapter


class Ovid(QMainWindow):
    defaultFontFamily = "Times New Roman"
    defaultFontSize = 25
    defaultMargin = 20

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 1200, 800)

        # Create the text editor area
        self.textEditor = OvidTextEdit(self)
        self.setCentralWidget(self.textEditor)
        self.novel = Novel()
        self.textEditor.textChanged.connect(self.update_chapter_contents)

        # Create our font helpers
        self.fonts = OvidFont(self)
        self.fonts.setFontFamily(Ovid.defaultFontFamily)
        self.fonts.setFontSize(Ovid.defaultFontSize)

        # Create Menu Bar
        self.menuBar = OvidMenuBar(self)
        self.setMenuBar(self.menuBar)

        # Create the toolbar
        self.toolBar = OvidToolBar(self)
        self.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        # Create the dockable sidebar
        self.chapterList = None
        self.sidebar = OvidDockWidget(self)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.sidebar)
        self.setWindowTitle(self.novel.title if self.novel else "Untitled")
        # Connect the current item changed signal of the chapterList to the new slot
        self.chapterList.currentItemChanged.connect(self.load_chapter_contents)
        # Connect the itemDoubleClicked signal of the chapterList to the new slot
        self.chapterList.itemDoubleClicked.connect(self.rename_chapter)

        # Shortcuts for text formatting and manipulation
        add_shortcuts(self)

    def add_chapter(self):
        # This function will be called when the button is clicked
        # Here, you can add logic to add a new chapter to the chapterList
        chapter_name, ok = QInputDialog.getText(self, 'New Chapter', 'Enter chapter name:')
        if ok and chapter_name:
            new_chapter = Chapter(chapter_name)
            self.novel.add_chapter(new_chapter)
            new_item = OvidListWidgetChapter(new_chapter)
            self.chapterList.addItem(new_item)  # Store the chapter object with the item
            self.chapterList.setCurrentItem(new_item)
    
    def update_chapter_contents(self):
        # Get the currently selected OvidListWidgetChapter
        current_item = self.chapterList.currentItem()
        if isinstance(current_item, OvidListWidgetChapter):
            # Update the chapter.contents
            current_item.chapter.contents = self.textEditor.toHtml()
    
    def load_chapter_contents(self, current_item, previous_item):
        # This slot will be called whenever the current item of the chapterList changes
        if isinstance(current_item, OvidListWidgetChapter):
            # Set the contents of the text editor to the contents of the selected chapter
            self.textEditor.setHtml(current_item.chapter.contents)
    
    def rename_chapter(self, item):
        # This slot will be called whenever an item of the chapterList is double clicked
        if isinstance(item, OvidListWidgetChapter):
            # Open a QInputDialog to get the new name
            new_name, ok = QInputDialog.getText(self, 'Rename Chapter', 'Enter new chapter name:', text=item.chapter.title)
            if ok and new_name:
                # Rename the chapter
                item.chapter.title = new_name
                # Update the item text in the list
                item.setText(new_name)


def main():
    app = QApplication(sys.argv)
    ex = Ovid()
    ex.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
