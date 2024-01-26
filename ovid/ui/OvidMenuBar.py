from PyQt6.QtWidgets import QMenuBar
from PyQt6.QtGui import QAction

class OvidMenuBar(QMenuBar):
    def __init__(self, ovid):
        super().__init__()
        self.ovid = ovid
        self.setup()

    def setup(self):
        # Add menus
        file_menu = self.addMenu("File")
        edit_menu = self.addMenu("Edit")
        view_menu = self.addMenu("View")

        # Add actions to File menu
        new_action = QAction("New", self)
        open_action = QAction("Open...", self)
        save_action = QAction("Save", self)
        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)

        # Add actions to Edit menu
        bold_action = QAction("Bold", self)
        italic_action = QAction("Italic", self)
        underline_action = QAction("Underline", self)
        strikethrough_action = QAction("Strikethrough", self)

        # Connect actions
        bold_action.triggered.connect(self.ovid.fonts.setBoldText)
        italic_action.triggered.connect(self.ovid.fonts.setItalicText)
        underline_action.triggered.connect(self.ovid.fonts.setUnderlineText)
        strikethrough_action.triggered.connect(self.ovid.fonts.setStrikeThroughText)

        edit_menu.addAction(bold_action)
        edit_menu.addAction(italic_action)
        edit_menu.addAction(underline_action)
        edit_menu.addAction(strikethrough_action)
