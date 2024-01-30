import sys
from PyQt6.QtWidgets import (
    QApplication,
    QInputDialog,
    QLabel,
    QMainWindow,
    QMenu,
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction

from ovid.ui.OvidFont import OvidFont
from ovid.ui.OvidMenuBar import OvidMenuBar
from ovid.ui.OvidToolBar import OvidToolBar
from ovid.ui.OvidDockWidget import OvidDockWidget
from ovid.ui.OvidTextEdit import OvidTextEdit
from ovid.ui.OvidListWidgetChapter import OvidListWidgetChapter
from ovid.ui.Utils import setNovel

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
        self.textEditor.textChanged.connect(self.update_chapter_contents)
        self.novel = None

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
        title = self.novel.title if self.novel else None
        self.setWindowTitle(title if title else "Untitled")
        # Connect the current item changed signal of the chapterList to the new slot
        self.chapterList.currentItemChanged.connect(self.load_chapter_contents)
        # Connect the itemDoubleClicked signal of the chapterList to the new slot
        self.chapterList.itemDoubleClicked.connect(self.rename_chapter)
        # Set the context menu policy of the chapterList to custom
        self.chapterList.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        # Connect the customContextMenuRequested signal of the chapterList to the new slot
        self.chapterList.customContextMenuRequested.connect(self.show_context_menu)

        # Status bar
        self.statusBar = self.statusBar()
        self.wordCountLabel = QLabel()
        self.statusBar.addWidget(self.wordCountLabel)

        # Connect the textChanged signal of the text editor to the update_word_count method
        self.textEditor.textChanged.connect(self.update_word_count)

        novel = Novel()
        novel.add_chapter(Chapter("Chapter 1"))
        setNovel(self, novel)

    def add_chapter(self):
        # This function will be called when the button is clicked
        # Here, you can add logic to add a new chapter to the chapterList
        chapter_name, ok = QInputDialog.getText(
            self, "New Chapter", "Enter chapter name:"
        )
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
            new_name, ok = QInputDialog.getText(
                self,
                "Rename Chapter",
                "Enter new chapter name:",
                text=item.chapter.title,
            )
            if ok and new_name:
                # Rename the chapter
                item.chapter.title = new_name
                # Update the item text in the list
                item.setText(new_name)

    def show_context_menu(self, position):
        # This slot will be called whenever the context menu is requested on the chapterList
        menu = QMenu()

        # Create an action for the context menu
        rename_action = QAction("Rename", self)
        rename_action.triggered.connect(
            lambda: self.rename_chapter(self.chapterList.currentItem())
        )

        # Add the action to the context menu
        menu.addAction(rename_action)

        # Show the context menu at the requested position
        menu.exec(self.chapterList.mapToGlobal(position))

    def update_word_count(self):
        # This slot will be called whenever the text in the text editor changes
        word_count = len(self.textEditor.toPlainText().split())
        self.wordCountLabel.setText(f"Chapter Word Count: {word_count}")


def main():
    app = QApplication(sys.argv)
    ovid = Ovid()
    ovid.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
