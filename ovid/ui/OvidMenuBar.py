from PyQt6.QtWidgets import QMenuBar, QDialog
from PyQt6.QtGui import QAction
from ovid.ui.NewNovelDialog import NewNovelDialog


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
        file_menu_trigger = {
            "New": self.new_novel,
            "Open": None,
            "Save": None
        }
        for label, trigger in file_menu_trigger.items():
            action = QAction(label, self)
            if trigger is not None:
                action.triggered.connect(trigger)
            file_menu.addAction(action)

        # Add actions to Edit menu
        edit_menu_trigger = {
            "Bold": self.parent.fonts.setBoldText,
            "Italic": self.parent.fonts.setItalicText,
            "Underline": self.parent.fonts.setUnderlineText,
            "Strikethrough": self.parent.fonts.setStrikeThroughText,
            "Clear Formatting": self.parent.fonts.clearFormatting,
        }
        for label, trigger in edit_menu_trigger.items():
            action = QAction(label, self)
            if trigger is not None:
                action.triggered.connect(trigger)
            edit_menu.addAction(action)

        # Add toggle action for sidebar in view menu
        toggleSidebarAction = QAction("Toggle Chapter List", self)
        toggleSidebarAction.triggered.connect(self.toggleSidebar)
        show_hide_menu.addAction(toggleSidebarAction)

        # Add toggle action for toolbar in view menu
        toggleToolbarAction = QAction("Toggle Toolbar", self)
        toggleToolbarAction.triggered.connect(self.toggleToolbar)
        show_hide_menu.addAction(toggleToolbarAction)

        toggleAllAction = QAction("Toggle All", self)
        toggleAllAction.triggered.connect(self.toggleAll)
        show_hide_menu.addAction(toggleAllAction)

    def toggleAll(self):
        sidebar = self.parent.sidebar
        toolbar = self.parent.toolBar

        if sidebar.isVisible() or toolbar.isVisible():
            # if any of them are visible, hide them all
            sidebar.setVisible(False)
            toolbar.setVisible(False)
        else:
            # none of them are visible, show them all
            sidebar.setVisible(True)
            toolbar.setVisible(True)

    def toggleToolbar(self):
        self.parent.toolBar.setVisible(not self.parent.toolBar.isVisible())

    def toggleSidebar(self):
        self.parent.sidebar.setVisible(not self.parent.sidebar.isVisible())

    def new_novel(self):
        dialog = NewNovelDialog(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            name = dialog.name_edit.text()
            genre = dialog.genre_edit.text()
            self.parent.setWindowTitle(name)
            # authors = [dialog.author_list.item(i).text() for i in range(dialog.author_list.count()) if dialog.author_list.item(i).isSelected()]
            # Now you have the name, genre, and authors. You can create a new Novel object and add it to your application.
