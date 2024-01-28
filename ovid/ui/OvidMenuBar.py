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
            {"New": self.new_novel, "Open": self.load_novel, "Save": self.save_novel},
        )
        self.add_menu(
            "Edit",
            {
                "Bold": self.parent.fonts.setBoldText,
                "Italic": self.parent.fonts.setItalicText,
                "Underline": self.parent.fonts.setUnderlineText,
                "Strikethrough": self.parent.fonts.setStrikeThroughText,
                "Clear Formatting": self.parent.fonts.clearFormatting,
            },
        )
        self.add_menu(
            "Show/Hide",
            {
                "Toggle Sidebar": self.toggleSidebar,
                "Toggle Toolbar": self.toggleToolbar,
                "Toggle All": self.toggleAll,
            },
        )

    def add_menu(self, menu_name, menu_triggers):
        menu = self.addMenu(menu_name)
        for label, trigger in menu_triggers.items():
            action = QAction(label, self)
            if trigger is not None:
                action.triggered.connect(trigger)
            menu.addAction(action)

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
            self.parent.setWindowTitle(name)
            self.parent.novel = Novel(name, genre)
            # authors = [dialog.author_list.item(i).text() for i in range(dialog.author_list.count()) if dialog.author_list.item(i).isSelected()]
            # Now you have the name, genre, and authors. You can create a new Novel object and add it to your application.

    def save_novel(self):
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
            # Save the novel to the chosen filename
            with gzip.open(filename, "wb") as f:
                pickle.dump(self.parent.novel, f)

    def load_novel(self):
        filename, _ = QFileDialog.getOpenFileName(
            self, "Open Novel", "", "Ovid Files (*.ovid)"
        )

        if filename:
            with gzip.open(filename, "rb") as f:
                self.parent.novel = pickle.load(f)

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
