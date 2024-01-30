from PyQt6.QtWidgets import QMenuBar, QDialog, QMessageBox, QFileDialog
from PyQt6.QtGui import QAction

import gzip
import pickle

from ovid.ui.OvidListWidgetChapter import OvidListWidgetChapter
from ovid.ui.OvidNovelDialog import OvidNovelDialog

from ovid.model.Novel import Novel


class OvidMenuBar(QMenuBar):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setup()

    def setup(self):
        self.add_menu(
            "File",
            {
                "New": {"trigger": self.new_novel, "shortcut": "Ctrl+N"},
                "Open": {"trigger": self.load_novel, "shortcut": "Ctrl+O"},
                "Save": {"trigger": self.save_novel, "shortcut": "Ctrl+S"},
                "Save As": {"trigger": self.save_as_novel, "shortcut": "Ctrl+Shift+S"},
            },
        )
        self.add_menu(
            "Edit",
            {
                "Undo": {"trigger": self.parent.textEditor.undo, "shortcut": "Ctrl+Z"},
                "Redo": {"trigger": self.parent.textEditor.redo, "shortcut": "Ctrl+Y"},
                "Cut": {"trigger": self.parent.textEditor.cut, "shortcut": "Ctrl+X"},
                "Copy": {"trigger": self.parent.textEditor.copy, "shortcut": "Ctrl+C"},
                "Paste": {
                    "trigger": self.parent.textEditor.paste,
                    "shortcut": "Ctrl+V",
                },
                "Select All": {
                    "trigger": self.parent.textEditor.selectAll,
                    "shortcut": "Ctrl+A",
                },
            },
        )
        self.add_menu(
            "Format",
            {
                "Bold": {
                    "trigger": self.parent.fonts.setBoldText,
                    "shortcut": "Ctrl+B",
                },
                "Italic": {
                    "trigger": self.parent.fonts.setItalicText,
                    "shortcut": "Ctrl+I",
                },
                "Underline": {
                    "trigger": self.parent.fonts.setUnderlineText,
                    "shortcut": "Ctrl+U",
                },
                "Strikethrough": {
                    "trigger": self.parent.fonts.setStrikeThroughText,
                    "shortcut": "Ctrl+Shift+T",
                },
                "Clear Formatting": {
                    "trigger": self.parent.fonts.clearFormatting,
                    "shortcut": "Ctrl+Shift+C",
                },
            },
        )
        self.add_menu(
            "Show/Hide",
            {
                "Toggle Sidebar": {"trigger": self.toggleSidebar},
                "Toggle Toolbar": {"trigger": self.toggleToolbar},
                "Toggle Statusbar": {"trigger": self.toggleStatusbar},
                "Toggle All": {"trigger": self.toggleAll, "shortcut": "Ctrl+T"},
            },
        )

    def add_menu(self, menu_name, menu_triggers):
        menu = self.addMenu(menu_name)
        for label, behaviors in menu_triggers.items():
            action = QAction(label, self)
            if behaviors is not None:
                if "shortcut" in behaviors:
                    action.setShortcut(behaviors["shortcut"])
                action.triggered.connect(behaviors["trigger"])
            menu.addAction(action)

    def toggleAll(self):
        sidebar = self.parent.sidebar
        toolbar = self.parent.toolBar
        statusbar = self.parent.statusBar

        if sidebar.isVisible() or toolbar.isVisible() or statusbar.isVisible():
            # if any of them are visible, hide them all
            sidebar.setVisible(False)
            toolbar.setVisible(False)
            statusbar.setVisible(False)
        else:
            # none of them are visible, show them all
            sidebar.setVisible(True)
            toolbar.setVisible(True)
            statusbar.setVisible(True)

    def toggleToolbar(self):
        self.parent.toolBar.setVisible(not self.parent.toolBar.isVisible())

    def toggleSidebar(self):
        self.parent.sidebar.setVisible(not self.parent.sidebar.isVisible())

    def toggleStatusbar(self):
        self.parent.statusBar.setVisible(not self.parent.statusBar.isVisible())

    def new_novel(self):
        if self.parent.novel is not None:
            # dialog to tell the user that they will lose their work
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Icon.Warning)
            msgBox.setText("Creating a new novel will replace your current novel.")
            msgBox.setInformativeText("Do you want to continue?")
            msgBox.setStandardButtons(
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )
            returnValue = msgBox.exec()
            if returnValue == QMessageBox.StandardButton.No:
                return

        dialog = OvidNovelDialog(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            name = dialog.name_edit.text()
            genre = dialog.genre_edit.text()
            self.parent.setWindow: whileTitle(name)
            self.parent.novel = Novel(name, genre)
            # authors = [dialog.author_list.item(i).text() for i in range(dialog.author_list.count()) if dialog.author_list.item(i).isSelected()]
            # Now you have the name, genre, and authors. You can create a new Novel object and add it to your application.

    def save_novel(self):
        if self.parent.novel is None:
            # If there is no novel, prompt the user to save as a new novel
            self.save_as_novel()
        else:
            # Save the current novel to the current filename
            with gzip.open(self.parent.novel.filename, "wb") as f:
                pickle.dump(self.parent.novel, f)

    def save_as_novel(self):
        # Clear the current chapters in the novel
        self.parent.novel.clear_chapters()

        # Add all chapters from the sidebar to the novel
        for i in range(self.parent.chapterList.count()):
            chapter_item = self.parent.chapterList.item(i)
            self.parent.novel.add_chapter(chapter_item.chapter)

        # Prompt the user with a "Save" dialog to choose the filename to save the novel as
        default_filename = f"{self.parent.novel.title}.ovid"
        filename, _ = QFileDialog.getSaveFileName(
            self, "Save Novel", default_filename, "Ovid Files (*.ovid)"
        )

        if filename:
            self.parent.novel.filename = filename
            with gzip.open(filename, "wb") as f:
                pickle.dump(self.parent.novel, f)

    def load_novel(self):
        filename, _ = QFileDialog.getOpenFileName(
            self, "Open Novel", "", "Ovid Files (*.ovid)"
        )

        if filename:
            try:
                with gzip.open(filename, "rb") as f:
                    self.parent.novel = pickle.load(f)
            except Exception as e:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Icon.Critical)
                msgBox.setText("Error loading novel")
                msgBox.setInformativeText(str(e))
                msgBox.exec()
                return
            self.parent.novel.filename = filename

            # Clear the current items in the sidebar
            self.parent.chapterList.clear()

            # Add each chapter of the loaded novel to the sidebar
            for chapter in self.parent.novel.chapters:
                chapter_item = OvidListWidgetChapter(chapter)
                self.parent.chapterList.addItem(chapter_item)

            # Select the first chapter and display its contents in the main window
            if self.parent.novel.chapters:
                first_chapter = self.parent.novel.chapters[0]
                self.parent.chapterList.setCurrentItem(self.parent.chapterList.item(0))
                self.parent.textEditor.setText(first_chapter.contents)
