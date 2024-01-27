from PyQt6.QtWidgets import QMenuBar
from PyQt6.QtGui import QAction

class OvidMenuBar(QMenuBar):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setup()

    def setup(self):
        # Add menus
        file_menu = self.addMenu("File")
        edit_menu = self.addMenu("Edit")
        show_hide_menu = self.addMenu("Show/Hide")

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
        clearformatting_action = QAction("Clear Formatting", self)

        # Connect actions
        bold_action.triggered.connect(self.parent.fonts.setBoldText)
        italic_action.triggered.connect(self.parent.fonts.setItalicText)
        underline_action.triggered.connect(self.parent.fonts.setUnderlineText)
        strikethrough_action.triggered.connect(self.parent.fonts.setStrikeThroughText)
        clearformatting_action.triggered.connect(self.parent.fonts.clearFormatting)

        edit_menu.addAction(bold_action)
        edit_menu.addAction(italic_action)
        edit_menu.addAction(underline_action)
        edit_menu.addAction(strikethrough_action)
        edit_menu.addAction(clearformatting_action)

        # Add toggle action for sidebar in view menu
        toggleSidebarAction = QAction("Toggle Chapter List", self)
        toggleSidebarAction.triggered.connect(self.toggleSidebar)
        show_hide_menu.addAction(toggleSidebarAction)

    def toggleSidebar(self):
        self.parent.sidebar.setVisible(not self.parent.sidebar.isVisible())