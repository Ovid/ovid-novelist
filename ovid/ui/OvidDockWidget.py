from PyQt6.QtWidgets import QDockWidget, QListWidget, QPushButton, QVBoxLayout, QWidget
from ovid.model.Novel import Novel


class OvidDockWidget(QDockWidget):
    def __init__(self, parent=None):
        super().__init__("Chapters", parent)
        self.novel = Novel()
        self.setMaximumWidth(200)  # Set a preferred width for the sidebar

        # Create a widget to hold the list and the button
        self.sidebarWidget = QWidget()
        self.sidebarLayout = QVBoxLayout(self.sidebarWidget)

        # Create the QListWidget for chapters
        self.chapterList = QListWidget()
        self.sidebarLayout.addWidget(self.chapterList)

        # Create the button to add new chapters
        self.addChapterButton = QPushButton("Add Chapter")
        self.addChapterButton.clicked.connect(parent.addChapter)
        self.sidebarLayout.addWidget(self.addChapterButton)

        # Set the widget to the dock
        self.setWidget(self.sidebarWidget)
