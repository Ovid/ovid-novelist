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
        new_action = QAction("New", self)
        open_action = QAction("Open", self)
        save_action = QAction("Save", self)
        
        new_action.triggered.connect(self.new_novel)

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
            #authors = [dialog.author_list.item(i).text() for i in range(dialog.author_list.count()) if dialog.author_list.item(i).isSelected()]
            # Now you have the name, genre, and authors. You can create a new Novel object and add it to your application.
