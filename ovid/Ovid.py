import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
)
from PyQt6.QtGui import (
    QShortcut,
    QKeySequence,
)
from PyQt6.QtCore import Qt
from ovid.ui.OvidFont import OvidFont
from ovid.ui.OvidMenuBar import OvidMenuBar
from ovid.ui.OvidToolBar import OvidToolBar
from ovid.ui.OvidDockWidget import OvidDockWidget
from ovid.ui.OvidTextEdit import OvidTextEdit

from ovid.model.AuthorCollection import AuthorCollection


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
        self.novel = None

        # Create our font helpers
        self.fonts = OvidFont(self)
        self.fonts.setFontFamily(Ovid.defaultFontFamily)
        self.fonts.setFontSize(Ovid.defaultFontSize)

        # Create Menu Bar
        self.menuBar = OvidMenuBar(self)
        self.setMenuBar(self.menuBar)
        self.toolBar = OvidToolBar(self)
        self.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        # Shortcuts for text formatting
        QShortcut(QKeySequence("Ctrl+B"), self, self.fonts.setBoldText)
        QShortcut(QKeySequence("Ctrl+I"), self, self.fonts.setItalicText)
        QShortcut(QKeySequence("Ctrl+U"), self, self.fonts.setUnderlineText)
        QShortcut(QKeySequence("Ctrl+T"), self, self.fonts.setStrikeThroughText)
        QShortcut(QKeySequence("Ctrl+Shift+C"), self, self.fonts.clearFormatting)

        # Create the dockable sidebar
        self.sidebar = OvidDockWidget(self)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.sidebar)
        self.setWindowTitle(self.novel.title if self.novel else "Untitled")

        self.author_collection = AuthorCollection()

    def addChapter(self):
        # This function will be called when the button is clicked
        # Here, you can add logic to add a new chapter to the chapterList
        new_chapter_name = f"Chapter {self.chapterList.count() + 1}"
        self.chapterList.addItem(new_chapter_name)


def main():
    app = QApplication(sys.argv)
    ex = Ovid()
    ex.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
