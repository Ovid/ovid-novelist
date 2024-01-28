import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
)
from PyQt6.QtCore import Qt
from ovid.ui.OvidFont import OvidFont
from ovid.ui.OvidMenuBar import OvidMenuBar
from ovid.ui.OvidToolBar import OvidToolBar
from ovid.ui.OvidDockWidget import OvidDockWidget
from ovid.ui.OvidTextEdit import OvidTextEdit
from ovid.ui.OvidShortCuts import add_shortcuts

from ovid.model.Novel import Novel


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
        self.sidebar = OvidDockWidget(self)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.sidebar)
        self.setWindowTitle(self.novel.title if self.novel else "Untitled")

        # Shortcuts for text formatting and manipulation
        add_shortcuts(self)

    def add_chapter(self):
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
