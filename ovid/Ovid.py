import sys
from PyQt6.QtWidgets import (
    QTextEdit,
    QApplication,
    QMainWindow,
    QDockWidget,
    QListWidget,
    QPushButton,
    QVBoxLayout,
    QWidget,
)
from PyQt6.QtGui import (
    QAction,
    QShortcut,
    QKeySequence,
    QFont,
)
from PyQt6.QtCore import Qt
from ovid.ui.OvidFont import OvidFont
from ovid.ui.OvidMenuBar import OvidMenuBar
from ovid.ui.OvidToolBar import OvidToolBar

class Ovid(QMainWindow):
    defaultFontFamily = "Arial"
    defaultFontSize = 25
    defaultMargin = 20

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Ovid")
        self.setGeometry(100, 100, 1200, 800)
        # Create the text editor area
        self.textEditor = QTextEdit()
        self.textEditor.setFont(QFont(Ovid.defaultFontFamily, Ovid.defaultFontSize))
        self.textEditor.setStyleSheet("background-color: white;")
        self.textEditor.setViewportMargins(Ovid.defaultMargin, Ovid.defaultMargin, Ovid.defaultMargin, Ovid.defaultMargin)
        self.setCentralWidget(self.textEditor)
        self.fonts = OvidFont(self)
        self.fonts.setFontSize(Ovid.defaultFontSize)

        # Create Menu Bar
        self.setMenuBar(OvidMenuBar(self))
        self.addToolBar(Qt.ToolBarArea.TopToolBarArea, OvidToolBar(self))

        # Shortcuts for text formatting
        QShortcut(QKeySequence("Ctrl+B"), self, self.fonts.setBoldText)
        QShortcut(QKeySequence("Ctrl+I"), self, self.fonts.setItalicText)
        QShortcut(QKeySequence("Ctrl+U"), self, self.fonts.setUnderlineText)
        QShortcut(QKeySequence("Ctrl+T"), self, self.fonts.setStrikeThroughText)
        QShortcut(QKeySequence("Ctrl+Shift+C"), self, self.fonts.clearFormatting)

        # Create the dockable sidebar
        self.sidebar = QDockWidget("Chapters", self)
        self.sidebar.setMaximumWidth(200)  # Set a preferred width for the sidebar
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.sidebar)

        # Create a widget to hold the list and the button
        self.sidebarWidget = QWidget()
        self.sidebarLayout = QVBoxLayout(self.sidebarWidget)

        # Create the QListWidget for chapters
        self.chapterList = QListWidget()
        self.sidebarLayout.addWidget(self.chapterList)

        # Create the button to add new chapters
        self.addChapterButton = QPushButton("Add Chapter")
        self.addChapterButton.clicked.connect(self.addChapter)
        self.sidebarLayout.addWidget(self.addChapterButton)

        # Set the widget to the dock
        self.sidebar.setWidget(self.sidebarWidget)

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
