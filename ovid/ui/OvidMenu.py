from PyQt6.QtWidgets import QMenuBar
from PyQt6.QtGui import QAction

class OvidMenu(QMenuBar):
    def __init__(self, ovid) -> None:
        super().__init__()
        self.ovid = ovid

    def setup(self) -> None:
        # Add menus
        ovid = self.ovid
        file_menu = self.addMenu("File")
        edit_menu = ovid.menubar.addMenu("Edit")
        view_menu = ovid.menubar.addMenu("View")

        # Add actions to File menu
        new_action = QAction("New", self)
        open_action = QAction("Open...", ovid)
        save_action = QAction("Save", ovid)
        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)

        # Add actions to Edit menu
        bold_action = QAction("Bold", ovid)
        italic_action = QAction("Italic", ovid)
        underline_action = QAction("Underline", ovid)
        strikethrough_action = QAction("Strikethrough", ovid)

        edit_menu.addAction(bold_action)
        edit_menu.addAction(italic_action)
        edit_menu.addAction(underline_action)
        edit_menu.addAction(strikethrough_action)