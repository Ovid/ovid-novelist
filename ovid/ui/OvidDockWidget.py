from PyQt6.QtWidgets import QDockWidget, QListWidget, QPushButton, QVBoxLayout, QWidget
from ovid.model.Novel import Novel


class OvidDockWidget(QDockWidget):
    def __init__(self, parent=None):
        super().__init__("Chapters", parent)
        self.novel = Novel()
        self.setMaximumWidth(200)  # Set a preferred width for the sidebar

        # Create a widget to hold the list and the button
        self.sidebar_widget = QWidget()
        self.sidebar_layout = QVBoxLayout(self.sidebar_widget)

        # Assuming self.sidebar is the QDockWidget instance
        self.sidebar_layout.setContentsMargins(0, 0, 0, 0)  # Set the margins to 0

        # Create the QListWidget for chapters
        parent.chapterList = QListWidget()
        self.sidebar_layout.addWidget(parent.chapterList)

        # Create the button to add new chapters
        self.add_chapter_buttn = QPushButton("Add Chapter")
        self.add_chapter_buttn.clicked.connect(parent.add_chapter)
        self.sidebar_layout.addWidget(self.add_chapter_buttn)

        # Set the widget to the dock
        self.setWidget(self.sidebar_widget)
