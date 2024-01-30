from PyQt6.QtWidgets import QMenuBar, QDialog, QMessageBox, QFileDialog, QInputDialog
from PyQt6.QtGui import QAction

import gzip
import pickle

from ovid.ui.OvidNovelDialog import OvidNovelDialog
from ovid.ui.Utils import setNovel

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
                "Quit": {"trigger": self.quit, "shortcut": "Ctrl+Q"},
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
                "Rename Novel": {"trigger": self.rename_novel, "shortcut": "Ctrl+R"},
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

    def rename_novel(self):
        if self.parent.novel is None:
            return

        new_name, ok = QInputDialog.getText(
            self,
            "Rename Novel",
            "Enter new novel name:",
            text=self.parent.novel.title,
        )
        if ok and new_name:
            self.parent.novel.title = new_name
            self.parent.setWindowTitle(new_name)

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
        if self.parent.novel is None or self.parent.novel.filename is None:
            # If there is no novel, prompt the user to save as a new novel
            self.save_as_novel()
        else:
            # Save the current novel to the current filename
            with gzip.open(self.parent.novel.filename, "wb") as f:
                pickle.dump(self.parent.novel, f)
            self.parent.novel.saved = True

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
        # filename should have an .ovid extension at the end
        if not filename.endswith(".ovid"):
            filename += ".ovid"

        if filename:
            self.parent.novel.filename = filename
            with gzip.open(filename, "wb") as f:
                pickle.dump(self.parent.novel, f)
            self.parent.novel.saved = True

    def load_novel(self):
        filename, _ = QFileDialog.getOpenFileName(
            self, "Open Novel", "", "Ovid Files (*.ovid)"
        )

        if filename:
            try:
                with gzip.open(filename, "rb") as f:
                    novel = pickle.load(f)
            except Exception as e:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Icon.Critical)
                msgBox.setText("Error loading novel")
                msgBox.setInformativeText(str(e))
                msgBox.exec()
                return
            novel.filename = filename

            setNovel(self.parent, novel)

            # set this to true to ensure that if we close the novel immediately
            # after loading, we don't get prompted to save
            novel.saved = True

    def quit(self):
        # if novel is not saved, prompt the user to save
        if not self.parent.novel.saved:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Icon.Warning)
            msgBox.setText("You have unsaved changes.")
            msgBox.setInformativeText("Do you want to save before quitting?")
            msgBox.setStandardButtons(
                QMessageBox.StandardButton.Save
                | QMessageBox.StandardButton.Discard
                | QMessageBox.StandardButton.Cancel
            )
            msgBox.setDefaultButton(QMessageBox.StandardButton.Save)
            returnValue = msgBox.exec()
            if returnValue == QMessageBox.StandardButton.Save:
                self.save_novel()
            elif returnValue == QMessageBox.StandardButton.Cancel:
                return
        self.parent.close()
